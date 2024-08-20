import pulp

problem = pulp.LpProblem("Optimization_of_Beverage_Production", pulp.LpMaximize)

lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Continuous')

problem += lemonade + fruit_juice

problem += 2 * lemonade + 1 * fruit_juice <= 100 # Water
problem += 1 * lemonade <= 50 # Sugar
problem += 1 * lemonade <= 30 # Lemon Juice
problem += 2 * fruit_juice <= 40 # Fruit Puree

problem.solve()

print(f"Status: {pulp.LpStatus[problem.status]}")
print(f"Lemonade amount: : {lemonade.varValue}")
print(f"Fruit Juice amount: {fruit_juice.varValue}")
print(f"Total amount: {pulp.value(problem.objective)}")