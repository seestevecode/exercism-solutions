(ns list-ops)

(defn append 
  "Given two vectors, it adds all the items in the second vector to the
  end of the first vector."
  [coll1 coll2]
  (loop [remaining coll2 acc coll1]
    (if (empty? remaining) acc
      (recur (rest remaining) (conj acc (first remaining))))))

(defn concatenate 
  "Given a vector of vectors, it combines all the vectors into one flattened
  vector."
  [colls]
  (loop [outer colls inner [] acc []]
    (if (empty? inner)
      (if (empty? outer) 
        acc 
        (recur (rest outer) (first outer) acc))
      (recur outer (rest inner) (conj acc (first inner))))))

(defn select-if
  "Given a predicate and a vector, it returns the vector of all items for
  which predicate(item) is true."
  [pred coll]
  (for [item coll :when (pred item)] item))

(defn length 
  "Given a vector, it returns the number of items within it."
  [coll]
  (if (empty? coll) 0 (+ 1 (length (rest coll)))))

(defn apply-to-each 
  "Given a function and a vector, it returns the vector of the results of
  applying function(item) on all items."
  [f coll]
  (for [item coll] (f item)))

(defn foldl 
  "Given a function, a vector, and initial accumulator, it folds (reduces)
  each item into the accumulator from the left."
  [f coll acc]
  (loop [remaining coll result acc]
    (if (empty? remaining) result
      (recur (rest remaining) (f result (first remaining))))))

(defn foldr
  "Given a function, a vector, and an initial accumulator, it folds (reduces)
  each item into the accumulator from the right."
  [f coll acc]
  (loop [remaining coll result acc]
    (if (empty? remaining) result
      (recur (butlast remaining) (f result (last remaining))))))

(defn reverse-order 
  "Given a vector, it returns a vector with all the original items, but in
  reverse order."
  [coll]
  (if (empty? coll) [] (cons (last coll) (reverse-order (butlast coll)))))
