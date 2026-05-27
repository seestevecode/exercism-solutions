(ns pascals-triangle)

(defn- next-row [prev-row]
  (mapv + (cons 0 prev-row) (conj prev-row 0)))

(def triangle (iterate next-row [1]))

(defn row [num] (nth triangle (dec num)))
