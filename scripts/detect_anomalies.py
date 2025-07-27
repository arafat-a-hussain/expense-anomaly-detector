import pandas as pd
import os

# Load the expense data
df = pd.read_csv("data/expenses.csv")

# Rule: Flag expenses above $400 as anomalies
df["Anomaly"] = df["Amount"] > 400

# Filter the anomalies
flagged = df[df["Anomaly"]]

# Save the result
os.makedirs("outputs", exist_ok=True)
flagged.to_csv("outputs/flagged_expenses.csv", index=False)

print("✅ Done! Anomalies saved to outputs/flagged_expenses.csv")

