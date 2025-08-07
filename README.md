# quintic-polynomial-solver

This Python script solves **fifth-degree polynomial equations** using Newton's method, a powerful numerical technique for finding roots of equations.

##  How it works:
1. The user inputs 6 coefficients for a polynomial of the form:
 f(x) = c₅·x⁵ + c₄·x⁴ + c₃·x³ + c₂·x² + c₁·x + c₀
2. The user also provides an initial guess `x₀`.
3. The program calculates updated guesses using:
 xₙ₊₁ = xₙ − f(xₙ)/f′(xₙ)
4. The process repeats until the solution is accurate to at least 8 decimal places.

##  Concepts Demonstrated:
- Newton’s method for root approximation
- Polynomial evaluation from lists of coefficients
- Derivative coefficient generation

##  Sample Input:
- Enter x^0 coefficient: -10
- Enter x^1 coefficient: -3
- Enter x^2 coefficient: 0
- Enter x^3 coefficient: 0
- Enter x^4 coefficient: 2
- Enter x^5 coefficient: 1
- Enter guess: 1.1

- Approx answer: 1.4287159979621487

  
