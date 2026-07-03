(ns all-your-base)

(defn- from-coll [coll base]
  (reduce (fn [acc item] (+ (* acc base) item)) 0 coll))

(defn- to-coll [number base]
  (if (zero? number) [0]
    (loop [n number result '()]
      (if (zero? n)
        (vec result)
        (recur (quot n base) (cons (mod n base) result))))))

(defn convert [from-base coll to-base]
  (when (and (> from-base 1)
             (> to-base 1)
             (every? #(<= 0 % (dec from-base)) coll))
    (if (empty? coll) []
      (to-coll (from-coll coll from-base) to-base))))

;; https://cs.stackexchange.com/a/10321
