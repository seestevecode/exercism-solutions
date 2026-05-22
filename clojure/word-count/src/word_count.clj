(ns word-count)

(defn word-count
  "Counts how many times each word occurs in the given string."
  [s]
  (frequencies (re-seq #"[a-z0-9]+(?:'[a-z0-9]+)?" (clojure.string/lower-case s))))
