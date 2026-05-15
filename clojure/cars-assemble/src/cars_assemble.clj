(ns cars-assemble)

(def base-rate
  221)

(defn production-rate
  "Returns the assembly line's production rate per hour,
   taking into account its success rate"
  [speed]
  (* speed base-rate 1/100 (cond
                             (= speed 0) 0.0
                             (<= 1 speed 4) 100.0
                             (<= 5 speed 8) 90.0
                             (= speed 9) 80.0
                             :else 77.0)))

(defn working-items
  "Calculates how many working cars are produced per minute"
  [speed]
  (int (/ (production-rate speed) 60)))
