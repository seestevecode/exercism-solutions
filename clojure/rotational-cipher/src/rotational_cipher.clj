(ns rotational-cipher)

(defn- rotater [ch cipher-key]
  (let [base (if (Character/isUpperCase ch) (int \A) (int \a))]
    (char (+ base (mod (+ (- (int ch) base) cipher-key) 26)))))

(defn rotate [s cipher-key]
  (clojure.string/replace s #"[a-zA-Z]" #(str (rotater (first %) cipher-key))))
