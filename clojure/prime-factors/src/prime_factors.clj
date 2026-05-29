(ns prime-factors)

(defn of
  "Returns the prime factors of the given number."
  [num]
  (loop [primes [] candidate 2 remaining num]
    (cond
      (= 1 remaining) primes
      (zero? (mod remaining candidate)) (recur 
                                         (conj primes candidate) 
                                         candidate 
                                         (quot remaining candidate))
      :else (recur 
             primes 
             (if (= 2 candidate) 3 (+ 2 candidate)) 
             remaining))))
