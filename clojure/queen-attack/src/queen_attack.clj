(ns queen-attack (:require [clojure.string :as str]))

(defn board-string [queen-positions]
  (str 
   (str/join "\n" (for [row (range 8)]
    (str/join " " (for [col (range 8)] 
      (condp = [row col]
        (:w queen-positions) "W"
        (:b queen-positions) "B"
        "_")))))
   "\n"))

(defn can-attack [queen-positions]
  (let [[w-row w-col] (:w queen-positions)
        [b-row b-col] (:b queen-positions)]
    (or
      (= w-row b-row)
      (= w-col b-col)
      (= (Math/abs (- w-row b-row)) (Math/abs (- w-col b-col))))))
