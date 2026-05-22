(ns space-age)

(def earth-year-seconds 31557600)

(def planet->orbit-years
  "Maps a planet to its orbit time in Earth years."
  {:mercury 0.2408467, :venus 0.61519726, :earth 1.0, :mars 1.8808158,
   :jupiter 11.862615, :saturn 29.447498, :uranus 84.016846, :neptune 164.79132})

(defn- age-on
  "Returns someone's age on specified planet based on the given age in seconds."
  [planet seconds]
  (/ seconds (* (planet planet->orbit-years) earth-year-seconds)))

(defn on-mercury
  "Returns someone's age on Mercury based on the given age in seconds."
  [seconds]
  (age-on :mercury seconds))

(defn on-venus
  "Returns someone's age on Venus based on the given age in seconds."
  [seconds]
  (age-on :venus seconds))

(defn on-earth
  "Returns someone's age on Earth based on the given age in seconds."
  [seconds]
  (age-on :earth seconds))

(defn on-mars
  "Returns someone's age on Mars based on the given age in seconds."
  [seconds]
  (age-on :mars seconds))

(defn on-jupiter
  "Returns someone's age on Jupiter based on the given age in seconds."
  [seconds]
  (age-on :jupiter seconds))

(defn on-saturn
  "Returns someone's age on Saturn based on the given age in seconds."
  [seconds]
  (age-on :saturn seconds))

(defn on-uranus
  "Returns someone's age on Uranus based on the given age in seconds."
  [seconds]
  (age-on :uranus seconds))

(defn on-neptune
  "Returns someone's age on Neptune based on the given age in seconds."
  [seconds]
  (age-on :neptune seconds))
