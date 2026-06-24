(ns roman-numerals)

(def arabic->roman [[1000 "M"] [900 "CM"] [500 "D"] [400 "CD"] [100 "C"] [90 "XC"] 
                    [50 "L"] [40 "XL"] [10 "X"] [9 "IX"] [5 "V"] [4 "IV"] [1 "I"]])

(defn numerals
  "Converts a number to its roman numeral(s)."
  [num]
  (loop [remaining num numerals arabic->roman result ""]
    (if (zero? remaining) result
      (let [[candidate-value candidate-symbol] (first numerals)]
        (if (>= remaining candidate-value)
          (recur (- remaining candidate-value) numerals (str result candidate-symbol))
          (recur remaining (rest numerals) result))))))
