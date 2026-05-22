(ns rna-transcription)

(def nucleotide->rna {\G \C, \C \G, \T \A, \A \U})

(defn to-rna
  "Returns the RNA complement of the given DNA string sequence."
  [dna]
  (apply str (map nucleotide->rna dna)))
