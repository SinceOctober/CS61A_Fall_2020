(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
)

(define (caddr s)
  'YOUR-CODE-HERE
)


(define (sign num)
  'YOUR-CODE-HERE
)


(define (square x) (* x x))

(define (pow x y)
  'YOUR-CODE-HERE
)

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)


(define (sign num)
  (cond ((> num 0) 1)
        ((< num 0) -1)
        (else 0))
)


(define (pow x y)
  (if (= y 0)
      1
      (* x (pow x (- y 1))))
)

