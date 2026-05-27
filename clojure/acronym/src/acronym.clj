(ns acronym (:require [clojure.string :as str]))

(defn acronym
  "Converts phrase to its acronym."
  [phrase]
  (let [cleaned (str/replace (str/upper-case phrase) #"[^A-Z\-\s]" "")]
    (str/join (map first (str/split cleaned #"[\s\-]")))))
