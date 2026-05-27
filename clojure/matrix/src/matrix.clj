(ns matrix (:require [clojure.string :as str]))

(defn- parse
  "Parses a matrix string into nested vectors."
  [matrix]
  (mapv #(mapv parse-long (str/split % #"\s+")) (str/split matrix #"\n")))

(defn get-row
  "Returns the i-th row of the matrix."
  [matrix i]
  (nth (parse matrix) (dec i)))

(defn get-column
  "Returns the i-th column of the matrix."
  [matrix i]
  (nth (apply mapv vector (parse matrix)) (dec i)))
