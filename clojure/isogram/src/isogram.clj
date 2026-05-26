(ns isogram)

(defn isogram?
  "Returns true if the given string is an isogram;
  otherwise, it returns false."
  [s]
  (apply distinct? ::dummy (filter Character/isLetter (clojure.string/lower-case s))))
