(ns darts)

(defn score
  "Calculates the score of a dart throw."
  [x y]
  (condp < (+ (* x x) (* y y)) 100 0 25 1 1 5 10))
