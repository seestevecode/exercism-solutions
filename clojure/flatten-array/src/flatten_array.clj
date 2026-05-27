(ns flatten-array)

(defn flatten
  "Flattens the given sequential collection.
  Nil values are excluded from the result."
  [coll]
  (remove nil? (clojure.core/flatten coll)))
