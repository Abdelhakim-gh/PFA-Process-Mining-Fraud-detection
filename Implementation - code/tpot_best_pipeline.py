import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

# Load data
tpot_data = pd.read_csv('dataset/Insurance_claims_ML_blanced.csv', sep=',', dtype=np.float64)

# Split features and target
features = tpot_data.drop('State', axis=1)
target = tpot_data['State']

# Split the dataset into training and testing sets
training_features, testing_features, training_target, testing_target = train_test_split(
    features, target, random_state=42
)

# Initialize the best pipeline
exported_pipeline = XGBClassifier(
    learning_rate=1.0, 
    max_depth=4, 
    min_child_weight=5, 
    n_estimators=100, 
    n_jobs=1, 
    subsample=0.6, 
    verbosity=0
)

# Fix random state in the exported estimator
if hasattr(exported_pipeline, 'random_state'):
    setattr(exported_pipeline, 'random_state', 42)

# Train the pipeline
exported_pipeline.fit(training_features, training_target)

# Predict on the testing set
results = exported_pipeline.predict(testing_features)

# Optionally, you can include additional code to save or return results if needed
