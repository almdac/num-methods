from sympy.solvers.solveset import linsolve
from sympy import *

def createPolynomial(order, A):
    p = 0
    i = 0
    t = Symbol('t')
    for a in reversed(A):
        p += a*(t**i)
        i += 1

    return p

def createPolynomialSystem(order, A, T, F):
    system = []
    for t, f in zip(T,F):
        i = 0
        p = 0
        for a in reversed(A):
            p += a*(t**i)
            i += 1
        p -= f
        system.append(p)
    
    return system
        
def adamsBashforthFormula(f, ypoints, t0, h, order):
    A = [Symbol('A'), Symbol('B'), Symbol('C'), Symbol('D'), Symbol('E'), Symbol('F'), Symbol('G'), Symbol('H')][0:order]
    T = [Symbol('tn'), Symbol('tn-1'), Symbol('tn-2'), Symbol('tn-3'), Symbol('tn-4'), Symbol('tn-5'), Symbol('tn-6'), Symbol('tn-7')][0:order]
    F = [Symbol('fn'), Symbol('fn-1'), Symbol('fn-2'), Symbol('fn-3'), Symbol('fn-4'), Symbol('fn-5'), Symbol('fn-6'), Symbol('fn-7')][0:order]

    p = createPolynomial(order, A)
    p = integrate(p, Symbol('t'))
    p = p.subs({'t': Symbol('tn+1')}) - p.subs({'t': Symbol('tn')})
    solutions = linsolve(createPolynomialSystem(order, A, T, F), A)

    for s in solutions:
        for a, r in zip(A,s):
            p = p.subs({a: r})

    i = 0
    fpoints = []
    for yp in ypoints:
        fpoints.append(f.evalf(subs={'y': yp, 't': t0+(i*h)}))

    i = 0
    for fp, t, f in zip(fpoints, reversed(T), reversed(F)):
        p = p.evalf(subs={t: t0+(i*h), f: fp})

    return ypoints[len(ypoints)-1] + p

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
