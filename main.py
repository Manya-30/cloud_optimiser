import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Define available cloud resources (simulated dataset)
data = {
    "Provider": ["AWS", "Azure", "GCP", "DigitalOcean", "IBM Cloud"],
    "vCPUs": [4, 8, 6, 4, 8],
    "RAM_GB": [16, 32, 24, 16, 32],
    "Cost_per_hour($)": [0.20, 0.40, 0.35, 0.25, 0.38]
}

# Create DataFrame
df = pd.DataFrame(data)
print(df)

# Step 2: Calculate Performance Score (higher = more efficient)
df["Performance_Score"] = (df["vCPUs"] * df["RAM_GB"]) / df["Cost_per_hour($)"]
print(df)

# Step 3: Identify the best cloud provider
best_option = df.loc[df["Performance_Score"].idxmax()]

print("\n✅ Recommended Cloud Provider for Best Cost Optimization:\n")
print(f"Provider: {best_option['Provider']}")
print(f"vCPUs: {best_option['vCPUs']}")
print(f"RAM: {best_option['RAM_GB']} GB")
print(f"Cost per hour: ${best_option['Cost_per_hour($)']}")
print(f"Performance Score: {best_option['Performance_Score']:.2f}")

# Step 4: Visualize performance-cost efficiency across providers
plt.figure(figsize=(8, 5))
plt.bar(df["Provider"], df["Performance_Score"])
plt.title("Cloud Providers vs Performance-Cost Efficiency")
plt.xlabel("Cloud Provider")
plt.ylabel("Performance Score (Higher = Better)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig("performance_chart.png")  # Saves the chart as a file
