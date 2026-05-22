(ns eliuds-eggs)

(defn egg-count
  "Returns the number of 1 bits in the binary representation of the given number."
  [num]
  (loop [n num ones 0] (if (zero? n) ones (recur (quot n 2) (+ ones (mod n 2))))))
