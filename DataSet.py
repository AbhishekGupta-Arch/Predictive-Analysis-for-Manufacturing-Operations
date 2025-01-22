import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
n_samples = 1000
data = {
    "Machine_ID": np.arange(1, n_samples + 1),
    "Temperature": np.random.uniform(50, 150, n_samples),
    "Run_Time": np.random.uniform(100, 1000, n_samples),
    "DownTime_Flag": np.random.choice([0, 1], n_samples, p=[0.8, 0.2]),  # 80% no downtime, 20% downtime
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("Machine Downtime.csv", index=False)

print("Synthetic data generated and saved as 'Machine Downtime.csv'.")
