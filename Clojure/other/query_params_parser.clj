;; Given a query string "param1=v1&param2=v2&param3=v3" generate a map of the form:
;; {:param1 "v1", param2 "v2", :param3 "v3"} for now you can try it with simple string values.

(require '[clojure.string :as s])

(defn convert-key-value
    [key-value]
    (vector (keyword (first key-value)) (second key-value))
)

(defn generate-params-map
    [params-str]
    (into {} (map #(convert-key-value (s/split % #"=")) (s/split params-str #"&")))
)
(println (generate-params-map "param1=v1&param2=v2&param3=v3"))
