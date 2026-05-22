(ns resistor-color)

(def color->code {"black" 0, "brown" 1, "red" 2, "orange" 3, "yellow" 4,
                  "green" 5, "blue" 6, "violet" 7, "grey" 8, "white" 9})

(def colors (keys (sort-by val color->code)))

(defn color-code
  "Returns the numerical value associated with the given color."
  [color]
  (color->code color))
