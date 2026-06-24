(ns run-length-encoding (:require [clojure.string :as str]))

(defn run-length-encode
  "Encodes a string with run-length encoding."
  [plaintext]
  (->>
    plaintext
    (partition-by identity)
    (map #(str (if (= 1 (count %)) "" (count %)) (first %)))
    (str/join)))

(defn run-length-decode
  "Decodes a run-length-encoded string."
  [ciphertext]
  (->> 
    ciphertext
    (re-seq #"(\d*)(\D)")
    (mapcat (fn [[_ n ch]] (repeat (if (str/blank? n) 1 (parse-long n)) ch)))
    (str/join)))
