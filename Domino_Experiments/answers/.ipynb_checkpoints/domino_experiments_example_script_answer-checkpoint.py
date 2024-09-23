# import MLflow library
import mlflow
import time
import os

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor


# create and set a new experiment
# Define the experiment name
username = os.environ['DOMINO_STARTING_USERNAME']
experiment_name = f"random-forest-gen-{username}"


# Check if the experiment already exists
experiment = mlflow.get_experiment_by_name(experiment_name)

if experiment is None:
    # Create a new experiment if it doesn't exist
    experiment_id = mlflow.create_experiment(experiment_name)
else:
    # Use the existing experiment
    experiment_id = experiment.experiment_id
    
    
# Define hyperparameters for RandomForestRegressor
n_estimators = 100
max_depth = 6
max_features = 3


# Get the current timestamp
timestamp = time.time()

# Create a descriptive run name that includes the hyperparameters and timestamp
run_name = f"rf_n_estimators={n_estimators}_max_depth={max_depth}_max_features={max_features}_{timestamp}"

# Enable auto-logging
mlflow.autolog()

# Start the run with the custom run name
with mlflow.start_run(experiment_id=experiment_id, run_name=run_name):
    db = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)
    rf = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, max_features=max_features)
    
    # Train the model
    rf.fit(X_train, y_train)
    
    # Score the model
    rf.score(X_test, y_test)

# End the run
mlflow.end_run()