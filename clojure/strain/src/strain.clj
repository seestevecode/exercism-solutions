(ns strain)

(defn retain
  "Keeps the items in coll for which (pred item) returns true."
  [pred coll]
  (for [item coll :when (pred item)] item))

(defn discard
  "Removes the items in coll for which (pred item) returns true."
  [pred coll]
  (for [item coll :when (not (pred item))] item))
