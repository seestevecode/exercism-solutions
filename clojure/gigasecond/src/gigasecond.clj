(ns gigasecond)

(defn- leap-year? 
  [year]
  (and (zero? (mod year 4)) (or (pos? (mod year 100)) (zero? (mod year 400)))))

(defn- days-to-next-month
  "Determines days to next calendar month."
  [year month day]
  (cond
    (contains? #{4 6 9 11} month) (inc (- 30 day)) ; 30 days hath September ...
    (contains? #{1 3 5 7 8 10 12} month) (inc (- 31 day)) ; all the rest have 31
    :else (inc (- (if (leap-year? year) 29 28) day)))) ; except February ...

(defn from
  "Determines the date one gigasecond after the given date."
  [year month day]
  (let [gigasecond-days (quot 1000000000 (* 60 60 24))]
    (loop [[y m d] [year month day]
           remaining gigasecond-days]
      (let [days-this-month (days-to-next-month y m d)]
        (if (< remaining days-this-month)
          [y m (+ d remaining)]
          (recur
           (if (= m 12) [(inc y) 1 1] [y (inc m) 1]) ; 1st of next month
           (- remaining days-this-month)))))))
