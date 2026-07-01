(ns transpose (:require [clojure.string :as str]))

(defn- max-width [lines] (if (seq lines) (apply max (map count lines)) 0))

(defn- last-row-with-column
  [lines col]
  (last (keep-indexed (fn [row line] (when (< col (count line)) row)) lines)))

(defn- char-at [line col] (if (< col (count line)) (nth line col) \space))

(defn transpose
  "Returns the transposed version of the given string."
  [s]
  (let [lines (str/split-lines s)
        width (max-width lines)
        transposed-lines (for [col (range width)]
                           (let [last-row (last-row-with-column lines col)]
                             (apply str (for [row (range (inc last-row))]
                                          (char-at (nth lines row) col)))))]
    (str/join "\n" transposed-lines)))
