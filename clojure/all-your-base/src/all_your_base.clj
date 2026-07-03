(ns all-your-base)

(defn- from-digits [digits base]
  (reduce (fn [acc digit] (+ (* acc base) digit)) 0 digits))

(defn- to-digits [number base]
  (if (zero? number) [0]
    (loop [n number result '()]
      (if (zero? n)
        (vec result)
        (recur (quot n base) (cons (mod n base) result))))))

(defn convert [from-base digits to-base]
  (when (and (> from-base 1)
             (> to-base 1)
             (every? #(<= 0 % (dec from-base)) digits))
    (if (empty? digits) []
      (to-digits (from-digits digits from-base) to-base))))

;; https://cs.stackexchange.com/a/10321
