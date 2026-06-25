(ns matching-brackets)

(def pairs {\[ \], \{ \}, \( \)})

(defn valid?
  "Returns true if the given string has properly matched brackets;
  otherwise, it returns false."
  [s]
  (let [cleaned (clojure.string/replace s #"[^\[\]{}\(\)]" "")]
    (loop [remaining cleaned stack []]
      (cond
        (empty? remaining) (empty? stack)
        (contains? pairs (first remaining)) 
          (recur (rest remaining) (conj stack (first remaining)))
        (= (first remaining) (pairs (peek stack)))
          (recur (rest remaining) (pop stack))
        :else false))))
