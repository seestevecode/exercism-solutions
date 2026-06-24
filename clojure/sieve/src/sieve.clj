(ns sieve (:require [clojure.set :as set]))

(defn sieve
  "Returns the primes that are less than or equal to num."
  [num]
  (loop [remaining (set (range 2 (inc num))) primes #{}]
    (if (empty? remaining) (sort primes)
      (let [next-prime (apply min remaining)]
        (recur
         (set/difference remaining (set (range next-prime (inc num) next-prime)))
         (conj primes next-prime))))))
