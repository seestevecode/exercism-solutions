(ns perfect-numbers)

(defn- aliquot
  "Calculates the aliquot sum of a number."
  [n]
  (let [factors 
        (mapcat #(if (= % (/ n %)) [%] [% (/ n %)])
                (filter #(zero? (mod n %)) (range 1 (inc (int (Math/sqrt n))))))]
    (reduce + (disj (into #{} factors) n))))

(defn classify
  "Classifies the given number as perfect, abundant, or deficient."
  [num]
  (let [aliquot (aliquot num)]
    (cond
      (< num aliquot) :abundant
      (> num aliquot) :deficient
      :else :perfect)))
