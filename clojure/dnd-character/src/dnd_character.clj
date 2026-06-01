(ns dnd-character)

(defn score-modifier
  "Calculates the modifier of the given score."
  [score]
  (clojure.math/floor-div (- score 10) 2))

(defn rand-ability
  "Generates a random ability."
  []
  (reduce + (rest (sort (repeatedly 4 #(inc (rand-int 6)))))))

(defrecord DndCharacter
  [strength dexterity charisma wisdom intelligence constitution hitpoints])

(defn rand-character
  "Generates a random character."
  []
  (let [ability-scores (repeatedly 6 rand-ability)
        [strength dexterity charisma wisdom intelligence constitution] ability-scores
        hitpoints (+ 10 (score-modifier constitution))]
    (->DndCharacter strength dexterity charisma wisdom intelligence constitution hitpoints)))
