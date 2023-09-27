from pulp import *
problem = LpProblem("LP Problem", LpMaximize)
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
x3 = LpVariable("x3", lowBound=0)
x4 = LpVariable("x4", lowBound=0)
problem += x1 + x2 +x3 - x4
problem += x1 + x2 + 2*x3 + x4 == 12
problem += x1 + 2*x2 + x3 <= 20
problem += x1 + x2 + x3 <= 20
problem.solve()
print("Максим: ", value(problem.objective))
print("Оптимус x:")
for v in problem.variables():
    print(v.name, "=", value(v))