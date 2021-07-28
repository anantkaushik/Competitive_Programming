;; Problem Link: https://www.hackerrank.com/challenges/solve-me-first/problem

;; Complete the function solveMeFirst to compute the sum of two integers.

;; Example
;; a = 7
;; b = 3
;; Return 10.

;; Function Description

;; Complete the solveMeFirst function in the editor below.

;; solveMeFirst has the following parameters:

;; int a: the first value
;; int b: the second value
;; Returns
;; - int: the sum of a and b

;; Sample Input
;; a = 2
;; b = 3

;; Sample Output
;; 5

;; Method 1

(defn solveMeFirst 
    [x y]    
    (+ x y)
)


(def a (read-line))
(def b (read-line))

(println (solveMeFirst (Integer/parseInt a) (Integer/parseInt b)))

;; Method 2
(println (#(+ %1 %2) (Integer/parseInt (read-line)) (Integer/parseInt (read-line))))
