(ns nucleotide-count)

(def valid-nucleotides #{\A \C \G \T})

(defn count-of-nucleotide-in-strand [nucleotide strand]
  (when-not (contains? valid-nucleotides nucleotide) 
    (throw (IllegalArgumentException. "invalid nucleotide")))
  (get (frequencies strand) nucleotide 0))

(defn nucleotide-counts [strand]
  (merge (zipmap valid-nucleotides (repeat 0)) (frequencies strand)))
