(ns game-of-life)

(defn- get-cell [[row col] cells]
  "Returns the given cell value, or nil if out of bounds."
  (when
    (and (<= 0 row (dec (count cells))) (<= 0 col (dec (count (first cells)))))
    (get-in cells [row col])))

(defn- neighbour-count [[row col] cells]
  "Returns the count of 1s neigbouring the given cell."
  (reduce + 
    (keep #(get-cell % cells)
          [[(dec row) (dec col)] [(dec row) col] [(dec row) (inc col)]
           [row       (dec col)]                 [row       (inc col)]
           [(inc row) (dec col)] [(inc row) col] [(inc row) (inc col)]])))

(defn- tick-cell [[row col] cells]
  "Returns the next generation of the given cell."
  (let [cell-value (get-cell [row col] cells)
        cell-neighbours (neighbour-count [row col] cells)]
    (cond
      (and (= 1 cell-value) (<= 2 cell-neighbours 3)) 1
      (and (= 0 cell-value) (= 3 cell-neighbours)) 1
      :else 0)))

(defn tick
  "Returns the next generation of the cells."
  [cells]
  (mapv (fn [row]
          (mapv (fn [col]
                  (tick-cell [row col] cells))
                (range (count (first cells)))))
        (range (count cells))))
