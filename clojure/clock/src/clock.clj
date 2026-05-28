(ns clock)

(defn clock [hours minutes]
  (let [minutes-after-midnight (mod (+ minutes (* 60 hours)) (* 24 60))
        hour-out (mod (quot minutes-after-midnight 60) 24)
        minute-out (mod minutes-after-midnight 60)]
    {:hour hour-out :minute minute-out}))

(defn clock->string [clock]
  (format "%02d:%02d" (:hour clock) (:minute clock)))

(defn add-time [clock-in time-minutes]
  (clock (:hour clock-in) (+ time-minutes (:minute clock-in))))
