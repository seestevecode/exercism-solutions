(ns kindergarten-garden)

(def students [:alice :bob :charlie :david :eve :fred
               :ginny :harriet :ileana :joseph :kincaid :larry])

(def plants {\G :grass \C :clover \R :radishes \V :violets})

(defn garden [s]
  (->> s
       clojure.string/split-lines
       (map #(partition 2 (map plants %)))
       (apply interleave)
       (apply concat)
       (partition 4)
       (zipmap students)))
