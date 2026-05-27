(ns armstrong-numbers)

(defn armstrong?
  "Returns true if the given number is an Armstrong number;
  otherwise, it returns false."
  [num]
  (let [digits (map #(- (int %) (int \0)) (str num))
        num-digits (count digits)]
    (= num (reduce + (map #(reduce *' (repeat num-digits %)) digits)))))
