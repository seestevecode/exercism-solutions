(ns matching-brackets)

(def pairs {\[ \], \{ \}, \( \)})

(def openings (set (keys pairs)))
(def closings (set (vals pairs)))

(defn valid?
  "Returns true if the given string has properly matched brackets;
  otherwise, it returns false."
  [s]
  (let [result 
        (reduce (fn [stack ch] 
                  (cond 
                    (openings ch) (conj stack ch)
                    (closings ch) (if (= ch (pairs (peek stack))) (pop stack) (reduced ::invalid))
                    :else stack))
                [] s)]
    (= result [])))
