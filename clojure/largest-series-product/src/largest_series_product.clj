(ns largest-series-product)

(defn largest-product
  "Returns the largest product of any consecutive digits of length span
  in the string s."
  [span s]
  (when (neg? span) 
    (throw (IllegalArgumentException. "span must not be negative")))
  (when (> span (count s)) 
    (throw (IllegalArgumentException. "span must not exceed string length")))
  (when (re-find #"\D" s) 
    (throw (IllegalArgumentException. "digits input must only contain digits")))
  (let [digits (map #(- (int %) (int \0)) s)]
    (apply max (map #(apply * %) (partition span 1 digits)))))
