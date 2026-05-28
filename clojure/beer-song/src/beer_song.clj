(ns beer-song (:require [clojure.string :as str]))

(defn- amount [n] (if (zero? n) "no more" (str n)))

(defn- bottle-s [n] (str "bottle" (if (= n 1) "" "s")))

(defn- it-one [n] (if (= n 1) "it" "one"))

(defn verse
  "Returns the nth verse of the song."
  [num]
  (str 
   (str/capitalize (str 
                    (amount num) " " (bottle-s num) " of beer on the wall, "
                    (amount num) " " (bottle-s num) " of beer.\n"))
   (if (zero? num)
     "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
     (str "Take " (it-one num) " down and pass it around, "
          (amount (dec num)) " " (bottle-s (dec num)) " of beer on the wall.\n"))))

(defn sing
  "Given a start and an optional end, returns all verses in this interval. If
  end is not given, the whole song from start is sung."
  ([start] (sing start 0))
  ([start end] (str/join "\n" (map verse (range start (dec end) -1)))))
