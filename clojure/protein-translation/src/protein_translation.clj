(ns protein-translation)

(def acid->codons {"Methionine" ["AUG"]
                   "Phenylalanine" ["UUU" "UUC"]
                   "Leucine" ["UUA" "UUG"]
                   "Serine" ["UCU" "UCC" "UCA" "UCG"]
                   "Tyrosine" ["UAU" "UAC"]
                   "Cysteine" ["UGU" "UGC"]
                   "Tryptophan" ["UGG"]
                   :stop ["UAA" "UAG" "UGA"]})

(def codon->acid (into {} (for [[acid codons] acid->codons
                                codon codons]
                            [codon acid])))

(defn translate-rna
  "Translates an RNA string into amino acids."
  [rna]
  (loop [acc [] remaining rna]
    (cond
      (empty? remaining) acc
      (< (count remaining) 3) (throw (IllegalArgumentException. "Invalid codon")) 
      :else (let [candidate (codon->acid (subs remaining 0 3))]
              (cond
                (nil? candidate) (throw (IllegalArgumentException. "Invalid codon"))
                (= :stop candidate) acc
                :else (recur (conj acc candidate) (subs remaining 3)))))))
