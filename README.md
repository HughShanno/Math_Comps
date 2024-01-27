# Math_Comps

## About
This repository contains the code associated with the paper *Primes and Quadratic Forms* by Sophie Boileau, Alejandro González Argüelles, Grace Hanson, Ammy Lin, and Hugh Shanno. The user is encouraged to use the code to explore and gain a better understanding of the ideas presented in the paper.

### RBQF.py
This file contains code to obtain the equivalence classes from d = -3 up to a given negative discrimiant. 

The sample output is:
h(-d) = size = [(a,b,c), ..., (x,y,z)]

* -d is the discriminant in question.
* size is the number of reduced binary quadratic forms of discriminant -d.
* [(a,b,c), ..., (x,y,z)] is the list of reduced binary quadratic forms of discriminant -d.
* (a,b,c) is the reduced binary quadratic form ax^2 + bxy + cy^2.

## Reduce.py
This file contains the code to reduce a given binary quadratic form.