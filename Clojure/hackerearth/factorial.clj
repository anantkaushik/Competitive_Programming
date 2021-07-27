;; Problem Link: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-factorial/

;; Problem
;; You have been given a positive integer N. You need to find and print the Factorial of this number. The Factorial of a positive integer N refers to the product of 
;; all number in the range from 1 to N. You can read more about the factorial of a number here.

;; Input Format:
;; The first and only line of the input contains a single integer N denoting the number whose factorial you need to find.

;; Output Format
;; Output a single line denoting the factorial of the number N.

;; Constraints

;; Sample Input
;; 2
;; Sample Output
;; 2

;; Method 1
(defn factorial
    [n fact]
    (if (= n 1)
        fact
        (factorial (- n 1) (* fact n))
    )
)
(def x (Integer/parseInt (read-line)))
(println (factorial x 1))

;; Method 2
(println (reduce * (range 1 (inc (Integer/parseInt (read-line))))))
