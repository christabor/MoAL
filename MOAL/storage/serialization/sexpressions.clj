; http://hitchhikersclojure.com/blog/hitchhikers-guide-to-clojure/

(ns cloj-sexpr
    (:gen-class))

(defn -main
    "Main!"
    [& args]
    (str "Hello!"))

(defn prefsuf [pref mid suff]
    (str pref mid suff))

(defn mrify [first last]
    (prefsuf "Mr. " first last))

(defn msify [first last]
    (prefsuf "Ms. " first last))

; Using raw data instead of evaluation via `

; (str ("foo" "bar")) ; Error
(str `("foo" "bar")) ; No error

(= 2 2)
(last ("foo" "foo2"))
(first ("foo" "foo2"))

(* 2 2) ; 4
(* 2 (* 2 2)) ; 8
(* 2 (* 2 (* 2 2))) ; 16

(+ 1 2 (* 3 4 (/ 5 6)))
(inc 3)
(dec 2)
(+ (inc 3) (dec 2))
(= (inc 3) (+ 3 1))
(< 3.14159 Math/PI)

(format "Hello, %s %s" "Chris" "Tabor")
(str "foo" "bar")

(range 0 10)
(filter odd? (range 0 10))
(map + (filter odd? (range 0 10)))
(map inc (filter odd? (range 0 20)))
(map dec (filter even? (range 0 20)))
(map = (map inc (filter odd? (range 0 20))))
(map even? (range -10 10))

; Code as data and function in the purest form
(:age :dob {:age 29 :dob "01/05/1986"})
(+ (:one {:one 10}) (:two {:two 20}))

(nil? (#{:foo :bar} :fo0))
