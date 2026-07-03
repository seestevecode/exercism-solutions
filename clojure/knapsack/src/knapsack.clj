(ns knapsack)

(defn maximum-value [maximum-weight items]
  (if (empty? items)
    0
    (let [next-weight (:weight (first items))
          next-value (:value (first items))]
      (max
       (if (<= next-weight maximum-weight)
         (+ next-value (maximum-value (- maximum-weight next-weight) (rest items)))
         0)
       (maximum-value maximum-weight (rest items))))))
