import pandas as pd

# -----------------------------
# Load source data
# -----------------------------
actuals = pd.read_csv("data/actuals.csv")
budget = pd.read_csv("data/budget.csv")

# Rename columns for clarity
actuals = actuals.rename(columns={"amount": "actual"})
budget = budget.rename(columns={"amount": "budget"})

# -----------------------------
# Merge actuals and budget
# -----------------------------
df = pd.merge(
    actuals,
    budget,
    on=["month", "account"],
    how="inner"
)

# -----------------------------
# Variance calculations
# -----------------------------
df["variance"] = df["actual"] - df["budget"]
df["variance_pct"] = (df["variance"] / df["budget"]).round(4)

# -----------------------------
# Favorable / Unfavorable logic
# Revenue: higher is favorable
# Expenses: lower is favorable
# -----------------------------
def flag_variance(row):
    if row["account"] == "Revenue":
        return "Favorable" if row["variance"] > 0 else "Unfavorable"
    else:
        return "Favorable" if row["variance"] < 0 else "Unfavorable"

df["performance"] = df.apply(flag_variance, axis=1)

# -----------------------------
# Final formatting
# -----------------------------
df = df.sort_values(by=["month", "account"])

# -----------------------------
# Export output
# -----------------------------
output_path = "variance_output.csv"
df.to_csv(output_path, index=False)

print("Variance Analysis complete.")
print(f"Output saved to {output_path}")