;; Problem Link: https://www.hackerrank.com/challenges/simple-array-sum/problem

;; Given an array of integers, find the sum of its elements.

;; Function Description
;; Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.
;; simpleArraySum has the following parameter(s):
;; ar: an array of integers

;; Input Format
;; The first line contains an integer, n, denoting the size of the array. 
;; The second line contains n space-separated integers representing the array's elements.

;; Output Format
;; Print the sum of the array's elements as a single integer.

;; Sample Input
;; 6
;; 1 2 3 4 10 11

;; Sample Output
;; 31

(defn simpleArraySum 
    [ar]
    (reduce + ar)
)

(def fptr (get (System/getenv) "OUTPUT_PATH"))

(def ar-count (Integer/parseInt (clojure.string/trim (read-line))))

(def ar (vec (map #(Integer/parseInt %) (clojure.string/split (clojure.string/trimr (read-line)) #" "))))

(def result (simpleArraySum ar))

(spit fptr (str result "\n") :append true)
