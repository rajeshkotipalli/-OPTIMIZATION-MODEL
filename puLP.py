# Install PuLP first if you haven't:
# pip install pulp

from pulp import LpMaximize, LpProblem, LpVariable, value, LpStatus

# Define a Linear Programming problem to maximize profit
model = LpProblem("Maximize_Profit", LpMaximize)

# Decision Variables (how many units to produce)
A = LpVariable("Product_A", lowBound=0, cat='Continuous')
B = LpVariable("Product_B", lowBound=0, cat='Continuous')

# Objective Function: Maximize Profit = 30*A + 20*B
model += 30 * A + 20 * B, "Total_Profit"

# Constraints
model += 2 * A + 1 * B <= 100, "Labor Constraint"
model += 3 * A + 2 * B <= 120, "Raw Material Constraint"

# Solve the problem
model.solve()

# -----------------------------------------------
# 📊 Cleaned and Clear Output
# -----------------------------------------------
print("\n📈 OPTIMIZATION RESULT\n" + "-" * 30)

# Show Solver Status
print(f"✅ Status: {LpStatus[model.status]}")

# Show Optimal Values
print(f"🏭 Optimal Production Plan:")
print(f"   ➤ Product A: {A.varValue:.2f} units")
print(f"   ➤ Product B: {B.varValue:.2f} units")

# Show Profit
print(f"💰 Maximum Profit Achieved: ₹{value(model.objective):.2f}")

# Extra info (optional)
print("\n📌 NOTE:")
print("✔ All constraints have been satisfied.")
print("✔ This is the best combination to maximize your profit based on the resource limits.\n")
