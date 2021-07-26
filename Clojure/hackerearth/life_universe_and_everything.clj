;; Problem Link: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/life-the-universe-and-everything/

;; Your program is to use the brute-force approach in order to find the Answer to Life, the Universe, and Everything. More precisely... 
;; rewrite small numbers from input to output. Stop processing input after reading in the number 42. All numbers at input are integers of one or two digits.

;; Sample Input
;; 1
;; 2
;; 88
;; 42
;; 99
;; Sample Output
;; 1
;; 2
;; 88

;; Method 1
(loop []
    (def x (read-line))
    (if (not= x "42")
        (do (println x)
            (recur))
    )
)


;; Method 2
(defn life-the-universe-and-everthing
    []
    (def x (read-line))
    (if (not= x "42")
        (do (println x)
            (life-the-universe-and-everthing))
    )
)
(life-the-universe-and-everthing)
