from propositional_logic import *

A = BoolVar('A')
B = BoolVar('B')
C = BoolVar('C')

# write code using A, B, and C, along with 
# the classes from propositional_logic.py
# and the .format() mathod to output the
# following expression:

# (((A => B) & (B => C)) => (A => C))

f1 = And(Implies(A, B), Implies(B,C))
f2 = Implies(f1, Implies(A, C))

print(f2.format())