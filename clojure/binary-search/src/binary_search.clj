(ns binary-search)

(defn search-for
  "Returns the index of num in coll, or -1 if num is not found."
  [num coll]
  (loop [low-idx 0 high-idx (dec (count coll))]
    (if (> low-idx high-idx) 
      -1
      (let [mid-idx (quot (+ low-idx high-idx) 2)
            mid-val (nth coll mid-idx)]
        (cond
          (< num mid-val) (recur low-idx (dec high-idx))
          (> num mid-val) (recur (inc low-idx) high-idx)
          :else mid-idx)))))
