#******************************************************************************
# quintic.py
#******************************************************************************
# Eduardo E
#
#
#
#ask for coefficient inputs
x0 = int(input('Enter x^0 coefficient: '))
x1 = int(input('Enter x^1 coefficient: '))
x2 = int(input('Enter x^2 coefficient: '))
x3 = int(input('Enter x^3 coefficient: '))
x4 = int(input('Enter x^4 coefficient: '))
x5 = int(input('Enter x^5 coefficient: '))
guess = float(input('Enter guess: '))

#put coefficients into a list
coefs= [x0,x1,x2,x3,x4,x5]

#list of the coefficients for the derivative
devs = [x0*0,x1*1,x2*2,x3*3,x4*4,x5*5]


#polynomial function, plugs in a value for x
def poly (a,b):
#broke one of Evan's laws, sorryyyy
    if a == coefs:
        suma = a[0]
        for element in range(1,6):
            suma+= (b**element)*a[element]
    else:
        suma = a[1]
        for element in range(2,6):
            suma += b**(element-1) * a[element]
    return suma


#initial result
result = poly(coefs,guess)


#while loop applies the Newton method that stops once the error is smaller than 10^-8
while abs(result) > 0.00000001:
    guess = guess - (poly(coefs,guess)/poly(devs,guess))
    result = poly(coefs,guess)

print(f'Aprox answer: {guess}')







