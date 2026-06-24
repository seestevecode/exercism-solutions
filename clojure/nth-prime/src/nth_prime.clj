(ns nth-prime)

(defn- prime? [n]
  (not-any? #(zero? (mod n %)) (range 2 (Math/sqrt (inc n)))))

(defn nth-prime [n]
  (nth (filter prime? (iterate inc 2)) (dec n)))
