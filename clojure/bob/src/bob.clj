(ns bob (:require [clojure.string :as str]))

(defn- question? [s] (str/ends-with? s "?"))

(defn- shouting? [s] (and (re-find #"[a-zA-Z]" s) (= s (str/upper-case s))))

(defn response-for [s]
  (let [cleaned (str/trim s)]
    (cond
      (empty? cleaned) "Fine. Be that way!"
      (and (shouting? cleaned) (question? cleaned)) "Calm down, I know what I'm doing!"
      (shouting? cleaned) "Whoa, chill out!"
      (question? cleaned) "Sure."
      :else "Whatever.")))
