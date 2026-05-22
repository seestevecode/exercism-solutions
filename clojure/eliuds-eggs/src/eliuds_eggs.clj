(ns eliuds-eggs)

(defn egg-count
  "Returns the number of 1 bits in the binary representation of the given number."
  [num]
  (if (zero? num) 0 (+ (if (zero? (mod num 2)) 0 1) (egg-count (quot num 2)))))
