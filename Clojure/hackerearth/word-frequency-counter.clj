; Problem Link: https://www.hackerearth.com/problem/algorithm/word-frequency-counter/

; You will be provided with a passage (no special characters, no punctuations). Your task is to
; find the frequency of the words occurring in the text, in other words find the number of times a
; word occurs in the given passage.
; Input
; A string with no special characters or punctuations.
; Output
; Output should be in the format:
; Word Count
; where Word is a string in the passage, and count is an integer representing number of times the
; Word has appeared in the passage. Word and the count must be separated by a space.
; Words and their count must be listed out in same order as given in the passage.
; Passage will be given as a single string, and not in paragraphs.
;
; Constrains
; 0 <= W <= 1000
; where W is the number of words in the passage.
; Note
; strings 'apple', 'APPLE', 'Apple' are all considered to be instances of the same word 'APPLE'.
; In Output, all letters of the words must be converted into UPPERCASE.(Refer Sample Input/Output)

; Sample Input
; My name is Xyz He is Abc Is he allright
; Sample Output
; MY 1
; NAME 1
; IS 3
; XYZ 1
; HE 2
; ABC 1
; ALLRIGHT 1

(require '[clojure.string :as s])
(def input-sentence (read-line))

(defn get-words-frequencies
      [sentence]
      (reduce (fn [words-frequencies-map word]
                  (if (empty? word)
                    words-frequencies-map
                    (let [key (s/upper-case word)]
                         (assoc words-frequencies-map
                                key (+ (get words-frequencies-map key 0) 1)))))
              {}
              (s/split sentence #" ")))

(map (fn [[key val]] (println key val)) (get-words-frequencies input-sentence))
