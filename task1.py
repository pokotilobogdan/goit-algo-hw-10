import pulp
from colorama import Fore

model = pulp.LpProblem("Maximize_beverages_production", pulp.LpMaximize)

x = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
y = pulp.LpVariable('Fruit_juice', lowBound=0, cat='Integer')

model += x + y, "Number_of_beverages_to_maximize"

model += 2*x + y <= 100, "Water"
model += x <= 50, "Sugar"
model += x <= 30, "Limon_Juice"
model += 2*y <= 40, "Fruit_mix"

model.solve()
# pulp.LpStatus[model.status]

for variable in model.variables():
    print(Fore.YELLOW + f"{variable.name} = {variable.varValue}")

# Вартість цільової функції
print()    
print(f"Total number = {pulp.value(model.objective)}" + Fore.RESET)
print()
