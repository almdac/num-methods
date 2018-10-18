from sympy import *
import math

def calculateAdamsBashforthCoeffs(order, j):
    k = 0
    product = 1
    while k < order:
        if (k != order-j-1):
            product *= (Symbol('x')+k)
        k += 1
    return (((-1)**(order-j-1))/(math.factorial(j)*math.factorial(order-j-1)))*integrate(product, (Symbol('x'), 0, 1))

def calculateAdamsBashforthIntegral(order, coeffs):
    j = 0
    eq = 0
    for c in coeffs:
        eq += c*Symbol('fn+{}'.format(j))
        j += 1
    return eq

def buildRecurrenceRelation(order, h, coeffs):
    return Symbol('yn+{}'.format(order-1)) + h*calculateAdamsBashforthIntegral(order, coeffs)

def adamsBashforthFormula(f, ypoints, tn, h, order, recurrence_relation):
    j = 0
    for yp in ypoints:
        recurrence_relation = recurrence_relation.subs('fn+{}'.format(j), f.subs({'y': yp, 't': tn+(j*h)}))
        j += 1
        
    return recurrence_relation.subs('yn+{}'.format(order-1), ypoints[len(ypoints)-1])

def eulerFormula(f, yn, tn, h):
    fn = f.evalf(subs={'y': yn, 't': tn})

    return yn+(fn*h)

def backwardEulerFormula(f, yn, tn, h):
    fn1 = f.evalf(subs={'y': eulerFormula(f, yn, tn, h), 't': tn+h})

    return yn+(fn1*h)

def improvedEulerFormula(f, yn, tn, h):
    fn = f.evalf(subs={'y': yn, 't': tn})
    fn1 = f.evalf(subs={'y': eulerFormula(f, yn, tn, h), 't': tn+h})

    return yn + (fn+fn1)*(h/2)

def rungeKuttaFormula(f, yn, tn, h): # Considering 4th order
    kn1 = f.evalf(subs={'y': yn, 't': tn})
    kn2 = f.evalf(subs={'y': yn+((h*kn1)/2), 't': tn+(h/2)})
    kn3 = f.evalf(subs={'y': yn+((h*kn2)/2), 't': tn+(h/2)})
    kn4 = f.evalf(subs={'y': yn+(h*kn3), 't': tn+h})

    return yn + (kn1+(2*kn2)+(2*kn3)+kn4)*(h/6)
