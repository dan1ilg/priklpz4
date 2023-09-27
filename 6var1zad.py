from pulp import *
problem1 = LpProblem("LP Problem", LpMaximize)
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
problem1 += 15*x1 + 21*x2 - 20
problem1 += -7*x1 + 2*x2 >= 14
problem1 += x1 +11*x2 <= 13
problem1 += x1 +x2 <= 3
problem1 += 4*x1 + 5*x2 >= 20
problem1.solve()
print("Максим: ", value(problem1.objective))
print("Оптимус x")
for v in problem1.variables():
    print(v.name, "=", value(v))
problem2 = LpProblem("LP Problem", LpMinimize)
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
problem2 += 15 * x1 + 21 * x2 - 20
problem2 += -7 * x1 + 2 * x2 >= 14
problem2 += x1 + 11 * x2 <= 13
problem2 += x1 + x2 <= 3
problem2 += 4 * x1 + 5 * x2 >= 20
problem2.solve()
print("Мина ", value(problem2.objective))
print("Оптимус x")
for v in problem2.variables():
    print(v.name, "=", value(v))