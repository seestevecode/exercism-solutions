(ns diamond (:require [clojure.string :as str]))

(def alphabet "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

(defn- diamond-row [row-char col-heads]
  (apply str (for [col-char col-heads] (if (= row-char col-char) row-char \space))))

(defn diamond
  "Returns a diamond shape pattern for the given letter."
  [letter]
  (let [sub-alpha (subs alphabet 0 (inc (str/index-of alphabet letter)))
        rev-alpha (str/reverse sub-alpha)
        row-heads (str sub-alpha (subs rev-alpha 1))
        col-heads (str rev-alpha (subs sub-alpha 1))]
    (str/join "\n" (map #(diamond-row % col-heads) row-heads))))
