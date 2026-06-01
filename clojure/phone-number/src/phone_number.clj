(ns phone-number (:require [clojure.string :as str]))

(defn number
  [s]
  (let [cleaned (str/replace (str/replace s #"\D" "") #"^1" "")]
    (if (re-matches #"1?[2-9]\d{2}[2-9]\d{6}" cleaned) cleaned "0000000000")))
