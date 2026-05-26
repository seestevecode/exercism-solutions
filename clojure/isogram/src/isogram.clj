(ns isogram)

(defn isogram?
  "Returns true if the given string is an isogram;
  otherwise, it returns false."
  [s]
  (let [cleaned (filter Character/isLetter (clojure.string/lower-case s))] 
    (= (count (set cleaned)) (count cleaned))))
