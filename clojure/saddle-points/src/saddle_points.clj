(ns saddle-points)

(defn saddle-points
  "Returns the saddle points of a matrix."
  [matrix]
  (if (empty? matrix) 
    #{}
    (let [row-maxes (mapv #(apply max %) matrix)
          col-mins (mapv #(apply min %) (apply map vector matrix))]
      (into #{}
            (for [row (range (count matrix))
                  col (range (count (first matrix)))
                  :let [target (get-in matrix [row col])]
                  :when (and (= target (row-maxes row)) (= target (col-mins col)))]
            [(inc row) (inc col)])))))
