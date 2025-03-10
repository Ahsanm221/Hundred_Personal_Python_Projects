"""
To run this code simply run the  command pyhton Assignment2.py in command line.
"""


# Re-importing necessary libraries after the reset
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import LeaveOneOut, cross_val_score
from sklearn.metrics import mean_squared_error

# Load the dataset
data_path = 'A2data.tsv'
data = pd.read_csv(data_path, delimiter='\t')
data.drop(columns=['InstanceID'], inplace=True)


# Assuming the last column is the target variable and the rest are features
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Initialize the model
model = LinearRegression()

# Perform Leave-One-Out cross-validation
loo = LeaveOneOut()
mse_scores = cross_val_score(model, X, y, scoring='neg_mean_squared_error', cv=loo)

# Convert MSE to RMSE
rmse_scores = np.sqrt(-mse_scores)

# Calculate the average RMSE
average_rmse = np.mean(rmse_scores)

print(average_rmse)














import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import mean_squared_error

# Load the dataset
data_path = 'A2data.tsv'
data = pd.read_csv(data_path, delimiter='\t')
data.drop(columns=['InstanceID'], inplace=True)


# Assuming the last column is the target variable and the rest are features
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Initialize the model
model = LinearRegression()
n_splits = 5

# Initialize the K-Fold cross-validation
kf = KFold(n_splits=n_splits, shuffle=True, random_state=1)

mse_scores = cross_val_score(model, X, y, scoring='neg_mean_squared_error', cv=kf)

# Convert MSE to RMSE
rmse_scores = np.sqrt(-mse_scores)

# Calculate the average RMSE
average_rmse = np.mean(rmse_scores)

print(average_rmse)














from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import KFold, cross_val_score
import matplotlib.pyplot as plt

# Preprocess the features with StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Initialize the Linear Regression model
model = LinearRegression()
n_splits = 5

# Initialize the K-Fold cross-validation
kf = KFold(n_splits=n_splits, shuffle=True, random_state=1)

# Use Leave-One-Out cross-validation to generate predictions
y_pred = cross_val_predict(model, X_scaled, y, cv=kf)

# Evaluate and compare performances using a scatter plot (Actual vs Predicted)
plt.figure(figsize=(8, 6))
plt.scatter(y, y_pred, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)  # Plot a line y=x for reference
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs. Predicted Outputs')
plt.show()










from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import KFold, cross_val_score

# Initialize the Decision Tree Regressor
tree_model = DecisionTreeRegressor()
n_splits = 5

# Initialize the K-Fold cross-validation
kf = KFold(n_splits=n_splits, shuffle=True, random_state=1)
# Use Leave-One-Out cross-validation to generate predictions for the Decision Tree model
y_pred_tree = cross_val_predict(tree_model, X_scaled, y, cv=kf)

# Plotting Actual vs. Predicted for Decision Tree Regressor
plt.figure(figsize=(8, 6))
plt.scatter(y, y_pred_tree, alpha=0.5, color='orange')  # Using a different color for distinction
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)  # Reference line y=x
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Decision Tree Regressor: Actual vs. Predicted Outputs')
plt.show()

# Note: This plot represents the actual vs. predicted values using a Decision Tree Regressor.
# Different colors are used for different models to help in visual comparison.







from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
import numpy as np

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
n_splits = 5

# Initialize the K-Fold cross-validation
kf = KFold(n_splits=n_splits, shuffle=True, random_state=1)

# Initializing models
linear_model = LinearRegression()
tree_model = DecisionTreeRegressor()
# Cross-validation with KFold
scores_linear = cross_val_score(linear_model, X_scaled, y, scoring='neg_mean_squared_error', cv=kf)
scores_tree = cross_val_score(tree_model, X_scaled, y, scoring='neg_mean_squared_error', cv=kf)

# Calculate RMSE and its standard deviation
rmse_linear = np.sqrt(-scores_linear)
rmse_tree = np.sqrt(-scores_tree)

# Average RMSE and Standard Deviation
avg_rmse_linear = np.mean(rmse_linear)
std_rmse_linear = np.std(rmse_linear)

avg_rmse_tree = np.mean(rmse_tree)
std_rmse_tree = np.std(rmse_tree)

# Creating a table for visualization
table_data = {
    'Model': ['Linear Regression', 'Decision Tree'],
    'Average RMSE': [avg_rmse_linear, avg_rmse_tree],
    'Standard Deviation': [std_rmse_linear, std_rmse_tree]
}
table_df = pd.DataFrame(table_data)

print(table_df)