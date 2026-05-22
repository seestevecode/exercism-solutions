(ns grains)

(defn square
  "Returns the number of grains on the n-th chessboard square."
  [n]
  (reduce *' (repeat (dec n) 2)))

(defn total
  "Returns the total number of grains on the chessboard."
  []
  (dec (square 65)))
