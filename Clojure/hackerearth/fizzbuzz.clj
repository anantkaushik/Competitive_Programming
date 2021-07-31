;; Problem Link: https://www.hackerearth.com/problem/algorithm/fizzbuzz/
;; Write a program that prints the numbers from 1 to 100. But for
;; multiples of three print “Fizz” instead of the number
;; and for the multiples of five print “Buzz”. For numbers which are
;; multiples of both three and five print “FizzBuzz”.
;; Print a new line after each string or number.

(defn fizz-buzz
  [number]
  (map
    (fn [n]
      (let [result
            (str
              (if (zero? (mod n 3))
                "Fizz")
              (if (zero? (mod n 5))
                "Buzz"))]
        (println (if (empty? result)
                   n
                   result))))
    (range 1 (inc number))))


(def x (Integer/parseInt (read-line)))
(fizz-buzz x)
