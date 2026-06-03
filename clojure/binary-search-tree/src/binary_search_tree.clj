(ns binary-search-tree)

(defn value [[_ v _]] v)

(defn singleton [v] [nil v nil])

(defn left [[v _ _]] v)

(defn right [[_ _ v]] v)

(defn insert [v tree]
  (cond
    (nil? tree) (singleton v)
    (<= v (value tree)) [(insert v (left tree)) (value tree) (right tree)]
    :else [(left tree) (value tree) (insert v (right tree))]))

(defn from-list [vs] (reduce #(insert %2 %1) nil vs))

(defn to-list [tree] (remove nil? (flatten tree)))
