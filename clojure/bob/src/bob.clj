(ns bob (:require [clojure.string :as str]))

(defn- question? [s] (str/ends-with? (str/trim s) "?"))

(defn- shouting? [s] (and (some Character/isLetter s) (= s (str/upper-case s))))

(defn response-for [s]
  (cond
    (str/blank? s) "Fine. Be that way!"
    ((every-pred shouting? question?) s) "Calm down, I know what I'm doing!"
    (shouting? s) "Whoa, chill out!"
    (question? s) "Sure."
    :else "Whatever."))
