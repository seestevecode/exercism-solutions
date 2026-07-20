(ns collatz-conjecture)

(defn collatz
  "Returns the number of steps for num to reach 1
  according to the Collatz Conjecture."
  [num]
  (cond
    (= 1 num) 0
    (even? num) (inc (collatz (quot num 2)))
    :else (inc (collatz (inc (* 3 num))))))
