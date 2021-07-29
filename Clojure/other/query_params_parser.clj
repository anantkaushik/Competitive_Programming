;; Given a query string "param1=v1&param2=v2&param3=v3" generate a map of the form:
;; {:param1 "v1", param2 "v2", :param3 "v3"} for now you can try it with simple string values.

(require '[clojure.string :as s])

;Method 1
(defn convert-key-value
    [key-value]
    (vector (keyword (first key-value)) (second key-value))
)

(defn generate-params-map
    [params-str]
    (into {} (map #(convert-key-value (s/split % #"=")) (s/split params-str #"&")))
)
(println (generate-params-map "param1=v1&param2=v2&param3=v3"))


;Method 2
(defn generate-params-map
      "Function to convert query param string to map"
      [params-str]
      (reduce (fn [params-map param-key-val]
                  (conj params-map
                        (#((fn [key-value]
                               (hash-map (keyword (first key-value)) (second key-value)))
                           (s/split % #"="))
                            param-key-val)))
              {}
              (s/split params-str #"&")
              )
      )

(println (generate-params-map "param1=v1&param2=v2&param3=v3"))
