(ns yacht)

(defn- score-minor [die-val dice] (reduce + (filter #{die-val} dice)))

(defn- score-n-of-a-kind [n dice]
  (let [match (first (filter #(>= (second %) n) (frequencies dice)))]
    (if match (* n (first match)) 0)))

(defn score
  "Given five dice and a category, it returns the score of the dice
  for that category."
  [dice category]
  (let [die-freqs (frequencies dice)
        dice-total (reduce + dice)]
    (condp = category
      "ones" (score-minor 1 dice)
      "twos" (score-minor 2 dice)
      "threes" (score-minor 3 dice)
      "fours" (score-minor 4 dice)
      "fives" (score-minor 5 dice)
      "sixes" (score-minor 6 dice)
      "little straight" (if (= '(1 2 3 4 5) (sort dice)) 30 0)
      "big straight" (if (= '(2 3 4 5 6) (sort dice)) 30 0)
      "full house" (if (= '(2 3) (sort (vals die-freqs))) dice-total 0)
      "three of a kind" (score-n-of-a-kind 3 dice)
      "four of a kind" (score-n-of-a-kind 4 dice)
      "choice" dice-total
      "yacht" (if (= 1 (count die-freqs)) 50 0))))
