from sympy import Symbol

y = Symbol('y')
t = Symbol('t')

def eulerFormula(f, yn, tn, h):
    fn = f.evalf(subs={y: yn, t: tn})
    return yn+(fn*h)

def backwardEulerFormula(f, yn, tn, h):
    fn1 = f.evalf(subs={y: eulerFormula(f, yn, tn, h), t: tn+h})
    return yn+(fn1*h)

def improvedEulerFormula(f, yn, tn, h):
    fn = f.evalf(subs={y: yn, t: tn})
    fn1 = f.evalf(subs={y: eulerFormula(f, yn, tn, h), t: tn+h})
    return yn + (fn+fn1)*(h/2)

def rungeKuttaFormula(f, yn, tn, h):
    kn1 = f.evalf(subs={y: yn, t: tn})
    kn2 = f.evalf(subs={y: yn+((h*kn1)/2), t: tn+(h/2)})
    kn3 = f.evalf(subs={y: yn+((h*kn2)/2), t: tn+(h/2)})
    kn4 = f.evalf(subs={y: yn+(h*kn3), t: tn+h})
    return yn + (kn1+(2*kn2)+(2*kn3)+kn4)*(h/6)
