(ns scrabble-score)

(def score->letters
  {1 [\A \E \I \O \U \L \N \R \S \T]
   2 [\D \G]
   3 [\B \C \M \P]
   4 [\F \H \V \W \Y]
   5 [\K]
   8 [\J \X]
   10 [\Q \Z]})

(def letter->score 
  (into {} 
        (for [[score letters] score->letters
              letter letters] 
          [letter score])))

(defn score-word
  "Returns the scrabble score of a word."
  [word]
  (reduce + (map letter->score (clojure.string/upper-case word))))
