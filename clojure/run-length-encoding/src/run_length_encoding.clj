(ns run-length-encoding)

(defn run-length-encode
  "Encodes a string with run-length encoding."
  [plaintext]
  (->>
    plaintext
    (partition-by identity)
    (mapcat #(str (if (= 1 (count %)) "" (count %)) (first %)))
    (apply str)))

(defn run-length-decode
  "Decodes a run-length-encoded string."
  [ciphertext]
  (->> 
    ciphertext
    (re-seq #"(\d*)(\D)")
    (mapcat (fn [[_ n ch]] (repeat (or (parse-long n) 1) ch)))
    (apply str)))
