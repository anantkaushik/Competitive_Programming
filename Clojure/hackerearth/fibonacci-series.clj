;; Problem Statement: https://www.hackerearth.com/problem/algorithm/fibonacci-seris/

;; Write a program to display nth term of fibonacci series of n terms.
;; Sample Input
;; 13
;; Sample Output
;; 144
;; Explanation
;; Here, the given input is 13, so 13th term of fibonacci series is 144 and it will be printed
;; out as the answer.

(def x (Integer/parseInt (read-line)))


(defn generate-fibonacci-number
  ([number previous current]
   (if (= number 1)
     (str current)
     (recur (- number 1) current (+ current previous))))
  ([number]
   (generate-fibonacci-number (- number 1) (bigint 0) (bigint 1))))


(println (generate-fibonacci-number x))
