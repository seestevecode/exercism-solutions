(ns sublist)

(defn- sublist?
  "Returns true if a is a sublist of b else false."
  [a b]
  (or
    (empty? a)
    (and (< (count a) (count b)) 
         (some #(= a %) (partition (count a) 1 b)))))

(defn classify
  "Returns:
  :equal if coll1 equals coll2,
  :superlist if coll1 is a superlist of coll2,
  :sublist if coll1 is a sublist of coll2,

  If none of these conditions is true, it returns :unequal."
  [coll1 coll2]
  (cond
    (= coll1 coll2) :equal
    (sublist? coll1 coll2) :sublist
    (sublist? coll2 coll1) :superlist
    :else :unequal))
