(ns robot-name)

(def used-names (atom #{}))

(defn robot []
  (atom nil))

(defn- generate-name []
  (format "%c%c%d%d%d"
          (char (+ (int \A) (rand-int 26)))
          (char (+ (int \A) (rand-int 26)))
          (rand-int 10)
          (rand-int 10)
          (rand-int 10)))

(defn- generate-unique-name []
  (loop [new-name (generate-name)]
    (if (contains? @used-names new-name)
      (recur (generate-name))
      (do
        (swap! used-names conj new-name)
        new-name))))

(defn robot-name [robot]
  (if-let [current-name @robot]
    current-name
    (let [new-name (generate-unique-name)]
      (reset! robot new-name)
      new-name)))

(defn reset-name [robot]
  (when-let [current-name @robot]
    (swap! used-names disj current-name))
  (reset! robot nil))
