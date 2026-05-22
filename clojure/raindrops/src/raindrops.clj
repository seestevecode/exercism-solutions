(ns raindrops)

(def drops {3 "Pling" 5 "Plang" 7 "Plong"})

(defn convert
  "Converts a number to its corresponding string of raindrop sounds."
  [num]
  (or 
   (not-empty (apply str (for [[div drop] drops :when (zero? (mod num div))] drop))) 
   (str num)))
