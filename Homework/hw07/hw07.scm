(define (filter-lst fn lst)
  (cond ((null? lst) nil)
        ((fn (car lst)) (cons (car lst) (filter-lst fn (cdr lst))))
        (else (filter-lst fn (cdr lst))) 
  )
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)

(define (interleave first second)
  (cond ((null? first) second)
        ((null? second) first)
        (else (cons (car first) (cons (car second) (interleave (cdr first) (cdr second)))))
  )
)

(interleave (list 1 3 5) (list 2 4 6))
; expect (1 2 3 4 5 6)

(interleave (list 1 3 5) nil)
; expect (1 3 5)

(interleave (list 1 3 5) (list 2 4))
; expect (1 2 3 4 5)


(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (accumulate combiner (combiner start (term n)) (- n 1) term))
  )
)

(define (no-repeats lst)
  (define (helper seen rest)
    (cond ((null? rest) nil)
          ((member (car rest) seen) (helper seen (cdr rest)))
          (else (cons (car rest) (helper (cons (car rest) seen) (cdr rest))))))
  (helper nil lst)
)

