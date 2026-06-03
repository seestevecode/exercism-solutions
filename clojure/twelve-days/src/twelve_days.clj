(ns twelve-days (:require [clojure.string :as str]))

(def ordinals {1 "first" 2 "second" 3 "third" 4 "fourth" 5 "fifth" 6 "sixth"
               7 "seventh" 8 "eighth" 9 "ninth" 10 "tenth" 11 "eleventh" 12 "twelfth"})

(def gifts {2 "two Turtle Doves,"
            3 "three French Hens,"
            4 "four Calling Birds,"
            5 "five Gold Rings,"
            6 "six Geese-a-Laying,"
            7 "seven Swans-a-Swimming,"
            8 "eight Maids-a-Milking,"
            9 "nine Ladies Dancing,"
            10 "ten Lords-a-Leaping,"
            11 "eleven Pipers Piping,"
            12 "twelve Drummers Drumming,"})

(defn- recite-verse
  "Returns the lyrics of a specified verse."
  [verse]
  (str "On the " (ordinals verse) " day of Christmas my true love gave to me: "
       (let [a-partridge "a Partridge in a Pear Tree."]
         (if (= verse 1) a-partridge 
           (str (str/join " " (map gifts (range verse 1 -1))) " and " a-partridge)))))

(defn recite
  "Returns the lyrics of the song: 'The Twelve Days of Christmas.'"
  [start-verse end-verse]
  (str/join "\n" (map recite-verse (range start-verse (inc end-verse)))))
