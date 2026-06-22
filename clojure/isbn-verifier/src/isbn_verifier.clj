(ns isbn-verifier)

(defn isbn?
  "Returns true if the given isbn is valid;
  otherwise, it returns false."
  [isbn]
  (if (re-matches #"[^0-9X-]" isbn) false
    (let [cleaned (clojure.string/replace isbn #"-" "")]
      (boolean (and
        (re-matches #"\d{9}[\dX]" cleaned)
        (zero? (mod (reduce + (map-indexed 
                               #(* (- 10 %1) (if (= %2 \X) 10 (- (int %2) (int \0)))) 
                               cleaned)) 
                    11)))))))
