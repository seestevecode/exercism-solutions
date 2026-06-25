(ns luhn)

(defn- luhn-digit [idx digit]
  (if (odd? idx) 
    (let [doubled (* 2 digit)] (if (> doubled 9) (- doubled 9) doubled)) 
    digit))

(defn valid?
  "Returns true if the given string is a valid number;
  otherwise, it returns false."
  [s]
  (let [cleaned (clojure.string/replace s #" " "")]
    (cond
      (re-find #"[^0-9]" cleaned) false
      (<= (count cleaned) 1) false
      :else
      (let [digits (map #(- (int %) (int \0)) cleaned)
            checksum (reduce + (map-indexed luhn-digit (reverse digits)))]
        (zero? (mod checksum 10))))))
