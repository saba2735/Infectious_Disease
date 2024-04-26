import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in the data
neg_data = pd.read_csv("HW4_Q3_neg.csv", header=None, names=["Value"])
pos_data = pd.read_csv("HW4_Q3_pos.csv", header=None, names=["Value"])
field_data = pd.read_csv("HW4_Q3_data.csv", header=None, names=["Value"])

# Calculate number of data points in each category
num_neg = len(neg_data)
num_pos = len(pos_data)
num_field = len(field_data)

# Calculate jitter offsets
jitter_neg = np.random.normal(0, 0.05, size=num_neg)
jitter_pos = np.random.normal(1, 0.05, size=num_pos)
jitter_field = np.random.normal(2, 0.05, size=num_field)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot negative controls in red with jitter
ax.scatter(jitter_neg, neg_data["Value"], color='red', alpha=0.5, label="Negative Controls")

# Plot positive controls in black with jitter
ax.scatter(jitter_pos, pos_data["Value"], color='black', alpha=0.5, label="Positive Controls")

# Plot field data in blue with jitter
ax.scatter(jitter_field, field_data["Value"], color='blue', alpha=0.5, label="Field Data")

# Add legend and labels
ax.legend()
ax.set_xlabel("Category", fontsize=12)
ax.set_ylabel("Values", fontsize=12)
ax.set_title("ELISA DATA", fontsize=14)

# Set x-axis ticks and labels
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(["Negative Controls", "Positive Controls", "Field Data"], fontsize=10)

# Show plot
plt.tight_layout()
plt.show()
