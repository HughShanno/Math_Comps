# Math_Comps

## About
This repository contains the code associated with the paper *Primes and Quadratic Forms* by Sophie Boileau, Alejandro González Argüelles, Grace Hanson, Ammy Lin, and Hugh Shanno. The user is encouraged to use the code to explore and gain a better understanding of the ideas presented in the paper.

We encourage the user to create a program in main.py that calls the functions of interest to the user. We have provided a sample program with some examples we hope illustrate how to use the program. We will now provide a brief description of the files in the repository and the functions they contain. Note that we will not cover every single function in the repsitory, helper functions that are not intended for user use will not be covered in the README.

## RBQF.py
This file contains code to obtain the equivalence classes from d = -3 up to a given negative discrimiant. It also contains a function to compute the reduced binary quadratic forms of a given negative discriminant. There is also a function to check whether a discriminant is fundamental or not.

Functions included:
#### bqfUpTo(lim)
This function returns a list of all the reduced binary quadratic forms of discriminant d from d = -3 up to the given limit.

**Required input:**
* lim: A negative intger. The negative discriminant of the binary quadratic forms to be considered

**Sample output:**
h(-3) = size = [(a,b,c), ..., (x,y,z)]
.
.
.
h(-d) = size = [(a,b,c), ..., (x,y,z)]

* -d is the discriminant input.
* size is the number of reduced binary quadratic forms of discriminant -d.
* [(a,b,c), ..., (x,y,z)] is the list of reduced binary quadratic forms of discriminant -d.
* (a,b,c) is the reduced binary quadratic form ax^2 + bxy + cy^2.

#### bqfOfD(d)
This function returns a list of all the reduced binary quadratic forms of given negative discriminant d.

**Required input:**
* d: A negative integer. The negative discriminant of the binary quadratic forms to be considered.

**Sample output:**

h(-d) = size = [(a,b,c), ..., (x,y,z)]

* -d is the discriminant input.
* size is the number of reduced binary quadratic forms of discriminant -d.
* [(a,b,c), ..., (x,y,z)] is the list of reduced binary quadratic forms of discriminant -d.
* (a,b,c) is the reduced binary quadratic form ax^2 + bxy + cy^2.

#### isFundamental(d)
This function returns a boolean value indicating whether the given negative discriminant is fundamental or not.

**Required input:**
* d: An integer. The negative discriminant to be checked.

**Sample output:**
* True if the discriminant is fundamental.
* False if the discriminant is not fundamental.

## Reduce.py
This file contains the code to reduce a given binary quadratic form.

#### reduceBQF(a, b, c)
This function returns the reduced binary quadratic form of the given binary quadratic form.

**Required input:**
* a: An integer. The coefficient of x^2 in the binary quadratic form.
* b: An integer. The coefficient of xy in the binary quadratic form.
* c: An integer. The coefficient of y^2 in the binary quadratic form.

**Sample output:**

[a, b, c]: A list of integers. The list contains the coefficients of the reduced binary quadratic form.

## Dirichlet_Composition.py
This file contains the code to compute the Dirichlet composition of two binary quadratic forms.

**Required input:**

* f1: A list of integers of the form [a, b, c]. The coefficients of the first binary quadratic form.
* f2: A list of integers of the form [a, b, c]. The coefficients of the second binary quadratic form.

**Sample output:**
[a, b, c]: A list of integers. The list contains the coefficients of the reduced binary quadratic form equivalent to the Dirichlet Composition of f1 with f2.
