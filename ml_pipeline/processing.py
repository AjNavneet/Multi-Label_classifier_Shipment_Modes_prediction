# Import necessary functions and libraries
from .utils import *
from sklearn import model_selection

# Define a function to read and process raw data into a processed dataset
def read_and_process_data():
    # Execute the query and load the results into a Pandas dataframe
    processed_data = read_query(query)

    # Separate features (x) and labels (y) from the processed data
    x = processed_data.drop(columns=labels).astype("float32")
    y = processed_data[labels]

    # Create cross-validation folds for model evaluation
    cv_folds = list(model_selection.KFold(n_splits=5, shuffle=True, random_state=42).split(x))

    # Return the processed data, features, labels, and cross-validation folds
    return processed_data, x, y, cv_folds
