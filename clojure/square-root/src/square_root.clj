(ns square-root)

(defn square-root
  "Calculates the square root of a number."
  [num]
  (loop [root 0]
    (if (> (* (inc root) (inc root)) num)
      root
      (recur (inc root)))))
