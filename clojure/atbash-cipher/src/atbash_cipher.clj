(ns atbash-cipher (:require [clojure.string :as str]))

(def cipher
  (let [alphabet "abcdefghijklmnopqrstuvwxyz"
        numbers "0123456789"]
    (zipmap (concat alphabet numbers) (concat (reverse alphabet) numbers))))

(defn encode
  "Encodes text using the Atbash cipher."
  [plaintext]
  (->> 
    (str/lower-case plaintext)
    (map cipher)
    (filter some?)
    (partition-all 5)
    (map str/join)
    (str/join " ")))

(defn decode
  "Decodes text using the Atbash cipher."
  [ciphertext]
  (str/join (map cipher ciphertext)))
