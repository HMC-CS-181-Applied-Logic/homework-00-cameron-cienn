## Part a

### Describe what the code in `z3-test.py` is doing in a paragraph or two.

 It sets up some variables (a & b are bools, x & y are ints), and defines f to be a clause consisting of conditions on those variables. Then it initializes a Solver, which is used to evaluate the satisfiability of given clauses. It checks the satisfiability of f. It adds another clause, then checks the satisfiability of the conjunction of the clauses.

 The program outputs the clauses it evaluates, and then whether they are satisfiable ("sat") or not ("unsat"). If satisfiable, it also prints an example.
