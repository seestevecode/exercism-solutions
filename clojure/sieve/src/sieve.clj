(ns sieve (:require [clojure.set :as set]))

(defn sieve
  "Returns the primes that are less than or equal to num."
  [num]
  (let [limit (Math/sqrt num)]
    (loop [n 2 composites #{}]
      (cond
        (> n limit) (remove composites (range 2 (inc num)))
        (composites n) (recur (inc n) composites)
        :else (recur (inc n) (into composites (range (* n n) (inc num) n)))))))
