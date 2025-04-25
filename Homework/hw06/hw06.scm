(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (sign num)
  (cond ((> num 0) -1)
        ((= num 0) 0)
        ((< num 0) 1))
)

(define (abs num)
  (cond ((> num 0) num)
        ((= num 0) 0)
        ((< num 0) (- num)))
)
(define (square x) (* x x))

(define (pow x y)
  (cond ((= y 0) 1)
        ((even? y) (square (pow x (/ y 2))))
        (else (* x (square (pow x (/ (- y 1) 2))))))
)