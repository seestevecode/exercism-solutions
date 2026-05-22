(ns collatz-conjecture)

(defn collatz
  "Returns the number of steps for num to reach 1
  according to the Collatz Conjecture."
  [num]
  (loop [steps 0
         n num]
    (if (= 1 n) 
      steps 
      (recur (inc steps) 
             (if (zero? (mod n 2)) 
               (quot n 2) 
               (inc (* 3 n)))))))
