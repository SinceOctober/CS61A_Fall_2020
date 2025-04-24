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

(define (sign num)
  'YOUR-CODE-HERE
)


(define (square x) (* x x))

(define (pow x y)
  'YOUR-CODE-HERE
)
