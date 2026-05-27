(ns proverb)

(defn recite [items]
  (if (empty? items) 
    ""
    (clojure.string/join "\n" (conj
     (mapv #(str "For want of a " (first %) " the " (last %) " was lost.") (partition 2 1 items))
     (str "And all for the want of a " (first items) ".")))))
