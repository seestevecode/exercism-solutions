(ns series)

(defn slices
  "Returns all contiguous substrings of length n from the string s."
  [s n]
  (when (empty? s) 
    (throw (IllegalArgumentException. "series cannot be empty")))
  (when (> n (count s)) 
    (throw (IllegalArgumentException. "slice length cannot be greater than series length")))
  (when (zero? n) 
    (throw (IllegalArgumentException. "slice length cannot be zero")))
  (when (neg? n) 
    (throw (IllegalArgumentException. "slice length cannot be negative")))
  (map #(apply str %) (partition n 1 s)))
