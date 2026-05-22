(ns pangram)

(defn pangram?
  "Returns true if the given string is a pangram;
  otherwise, it returns false."
  [s]
  (let [cleaned (filter Character/isLetter (clojure.string/lower-case s))]
    (= (sort (set cleaned)) (sort (set "abcdefghijklmnopqrstuvwxyz")))))
