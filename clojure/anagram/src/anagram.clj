(ns anagram (:require [clojure.string :refer [lower-case]]))

(defn anagrams-for
  "Returns all words from candidates that are anagrams of the given word."
  [word candidates]
  (filter #(and (not= (lower-case word) (lower-case %))
                (= (sort (lower-case word)) (sort (lower-case %)))) candidates))
