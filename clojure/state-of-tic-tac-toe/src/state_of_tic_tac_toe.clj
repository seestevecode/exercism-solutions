(ns state-of-tic-tac-toe)

(def impossible-exception
  (IllegalArgumentException. "Impossible board: game should have ended after the game was won"))

(defn- row-wins [board player] (count (filter #(every? #{player} %) board)))

(defn- diag-wins [board player]
  (let [winning-diagonal?
        (fn [board]
          (let [diag (map-indexed #(nth %2 %1) board)]
            (every? #{player} diag)))]
    (count (filter winning-diagonal? [board (map reverse board)]))))

(defn gamestate
  "Returns the gamestate of a tic-tac-toe board."
  [board]
  (let [counts (frequencies (apply str board))
        xs (get counts \X 0)
        os (get counts \O 0)
        spaces (get counts \space 0)
        transposed (map #(apply str %) (apply map vector board))
        x-wins (+ (row-wins board \X) (row-wins transposed \X) (diag-wins board \X))
        o-wins (+ (row-wins board \O) (row-wins transposed \O) (diag-wins board \O))]
    (cond
      (> os xs) (throw (IllegalArgumentException. "Wrong turn order: O started"))
      (> (- xs os) 1) (throw (IllegalArgumentException. "Wrong turn order: X went twice"))
      (and (pos? x-wins) (pos? o-wins)) (throw impossible-exception) ; both have won
      (and (pos? x-wins) (= xs os)) (throw impossible-exception) ; O has moved after X won
      (and (pos? o-wins) (> xs os)) (throw impossible-exception) ; X has moved after O won
      (and (zero? spaces) (zero? x-wins) (zero? o-wins)) :draw
      (or (pos? x-wins) (pos? o-wins)) :win
      :else :ongoing)))