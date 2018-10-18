from sympy import *

def AdamsPolynomialProductory(order, i):
    j = 0
    eq = 1
    while j < order:
        if j != i:
            eq *= (Symbol('t')-Symbol('tn+{}'.format(j)))/(Symbol('tn+{}'.format(i))-Symbol('tn+{}'.format(j)))
        j += 1
    return eq

def aproxIntegral(order):
    i = 0
    eq = 0
    while i < order:
        eqp = integrate(AdamsPolynomialProductory(order, i), Symbol('t'))
        eqp = eqp.evalf(subs={'t': 'tn+{}'.format(order)})-eqp.evalf(subs={'t': 'tn+{}'.format(order-1)})
        eqp *= Symbol('fn+{}'.format(i))
        eq += eqp
        i += 1
    return eq

def adamsBashforthFormula(f, ypoints, t, h, order):
    aprox_integral = aproxIntegral(order)

    i = 0
    fpoints = []
    for yp in ypoints:
        fpoints.append(f.evalf(subs={'y': yp, 't': t+(h*i)}))
        i += 1

    i = 0
    for fp in fpoints:
        aprox_integral = aprox_integral.evalf(subs={'tn+{}'.format(i): t+(h*i),'fn+{}'.format(i): fp})
        i += 1
    
    return ypoints[len(ypoints)-1] + aprox_integral

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
