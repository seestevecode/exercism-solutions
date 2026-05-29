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
                  :when (= (get-in matrix [row col]) (row-maxes row) (col-mins col))]
            [(inc row) (inc col)])))))
