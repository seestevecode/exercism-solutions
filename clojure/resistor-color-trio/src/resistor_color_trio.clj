(ns resistor-color-trio)

(def color->code {"black" 0 "brown" 1 "red" 2 "orange" 3 "yellow" 4
                  "green" 5 "blue" 6 "violet" 7 "grey" 8 "white" 9})

(def prefixes [[1000000000 "giga"] [1000000 "mega"] [1000 "kilo"]])

(defn resistor-label
  "Returns the resistor label based on the given color bands."
  [colors]
  (let [[tens-band units-band multiplier-band] colors
        base (+ (* 10 (color->code tens-band)) (color->code units-band))
        multiplier (reduce * (repeat (color->code multiplier-band) 10))                
        ohms (* base multiplier)]
    (if (zero? ohms) 
      "0 ohms"
      (if-let [[scale prefix] (some (fn [[scale prefix]]
                                      (when (zero? (mod ohms scale))
                                        [scale prefix]))
                                    prefixes)]
        (str (/ ohms scale) " " prefix "ohms")
        (str ohms " ohms")))))
