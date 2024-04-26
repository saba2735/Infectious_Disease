import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import norm
from sklearn.linear_model import LinearRegression

# Load data from CSV file
data = pd.read_csv('all_weeks.csv')

# Filter data for weeks 1 to 15
filtered_data = data[data['Week'].between(1, 15)]

# Adjust for the ascertainment rate by increasing reported cases
filtered_data['Adjusted_New_Cases'] = filtered_data['New Cases'].clip(lower=1)  # Set minimum value to 1

# Plotting the weekly incidence of BRUH disease for weeks 1 to 15
plt.figure(figsize=(12, 6))

# Scatter plot of actual data points
plt.scatter(filtered_data['Week'], filtered_data['Adjusted_New_Cases'], color='b', label='Actual Data')

# Fit a linear regression model to estimate the slope (m) for exponential growth
X = filtered_data['Week'].values.reshape(-1, 1)
y = np.log(filtered_data['Adjusted_New_Cases'])
reg = LinearRegression().fit(X, y)

# Extract slope from the regression
slope = reg.coef_[0]

# Estimate R0
gamma = 1 / 2  # duration of infection
mu = 1 / 100   # typical life expectancy
R0 = 1 + (slope / (gamma + mu))

# Calculate Confidence Interval for the Slope Estimate
n = len(filtered_data)
y_pred = reg.predict(X)
residuals = y - y_pred
mse = np.sum(residuals ** 2) / (n - 2)  # Mean squared error
se_slope = np.sqrt(mse / np.sum((X - np.mean(X)) ** 2))  # Standard error of the slope
t = 2.262  # t-value for 95% confidence interval with n-2 degrees of freedom
slope_lower_bound = slope - t * se_slope
slope_upper_bound = slope + t * se_slope

# Calculate 95% confidence interval for R0 based on the confidence interval of the slope (R0)
R0_lower_bound = 1 + (slope_lower_bound / (gamma + mu))
R0_upper_bound = 1 + (slope_upper_bound / (gamma + mu))

# Generate points for the fitted exponential growth curve
fitted_weeks = np.linspace(filtered_data['Week'].min(), filtered_data['Week'].max(), 100)
fitted_cases = np.exp(reg.predict(fitted_weeks.reshape(-1, 1)))

# Plot the fitted exponential growth curve
plt.plot(fitted_weeks, fitted_cases, linestyle='--', color='r', label='Exponential Fit')

plt.xlabel('Week')
plt.ylabel('Number of New Cases')
plt.title('Weekly Incidence of BRUH Disease (Weeks 1-15)')
plt.legend()
plt.grid(True)
plt.show()

# Print estimated R0 and its confidence interval
print(f"Estimated R0: {R0:.4f}")
print(f"95% Confidence Interval for R0: ({R0_lower_bound:.4f}, {R0_upper_bound:.4f})")
