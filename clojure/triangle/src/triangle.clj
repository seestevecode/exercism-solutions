(ns triangle)

(defn- triangle? [a b c] 
  (and (every? pos? [a b c]) (>= (+ a b) c) (>= (+ b c) a) (>= (+ a c) b)))

(defn equilateral?
  "Returns true if the triangle with sides a, b, and c is equilateral;
  otherwise, it returns false."
  [a b c]
  (and (triangle? a b c) (= a b c)))

(defn isosceles?
  "Returns true if the triangle with sides a, b, and c is isosceles;
  otherwise, it returns false."
  [a b c]
  (and (triangle? a b c) (>= 2 (count (set [a b c])))))

(defn scalene?
  "Returns true if the triangle with sides a, b, and c is scalene;
  otherwise, it returns false."
  [a b c]
  (and (triangle? a b c) (distinct? a b c)))
