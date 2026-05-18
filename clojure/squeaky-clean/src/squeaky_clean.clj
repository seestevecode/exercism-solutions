(ns squeaky-clean
  (:require [clojure.string :as str]))

(defn- space->underscore [s]
  (str/replace s " " "_"))

(defn- replace-ctrl [s]
  (str/replace s #"\p{IsControl}" "CTRL"))

(defn- kebab->camel [s]
  (str/replace s #"-\p{L}" #(str/upper-case (second %))))

(defn- only-letters [s]
  (apply str (filter #(or (Character/isLetter %) (= \_ %)) s)))

(defn- no-greek [s]
  (apply str (remove #(<= (int \u03B1) (int %) (int \u03C9)) s)))

(defn clean
  [s]
  (no-greek (only-letters (kebab->camel (replace-ctrl (space->underscore s))))))
