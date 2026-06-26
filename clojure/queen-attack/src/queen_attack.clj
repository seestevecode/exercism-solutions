(ns queen-attack (:require [clojure.string :as str]))

(defn board-string [{[w-row w-col] :w [b-row b-col] :b}]
  (str 
   (str/join "\n" (for [row (range 8)]
    (str/join " " (for [col (range 8)] 
      (condp = [row col]
        [w-row w-col] "W"
        [b-row b-col] "B"
        "_")))))
   "\n"))

(defn can-attack [{[w-row w-col] :w [b-row b-col] :b}]
  (or
     (= w-row b-row)
     (= w-col b-col)
     (= (Math/abs (- w-row b-row)) (Math/abs (- w-col b-col)))))
