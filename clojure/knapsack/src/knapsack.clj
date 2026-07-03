(ns knapsack)

(defn- best-values-with-item [max-weight old-best-values item]
  (let [item-weight (:weight item)
        item-value  (:value item)]
    (mapv
      (fn [capacity]
        (if (< capacity item-weight)
          (old-best-values capacity)
          (max 
           (old-best-values capacity) 
           (+ (old-best-values (- capacity item-weight)) item-value))))
      (range (inc max-weight)))))

(defn maximum-value
  "Calculates the maximum value that can be packed."
  [maximum-weight items]
  (let [initial-best-values (vec (repeat (inc maximum-weight) 0))
        final-best-values (reduce
                           (fn [best-values-acc item]
                             (best-values-with-item maximum-weight best-values-acc item))
                           initial-best-values
                           items)]
    (final-best-values maximum-weight)))
