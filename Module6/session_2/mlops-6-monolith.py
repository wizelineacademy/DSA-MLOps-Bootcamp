import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.datasets import make_regression

# Monolithic, difficult-to-understand code
def run_entire_workflow():
    # Generating a large dataset with unnecessary complexity
    X, y = make_regression(n_samples=100, n_features=1, noise=0.1)
    print("Dataset Generated - X shape: {}, y shape: {}".format(X.shape, y.shape))

    # Splitting the dataset in a standard way
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    print("Dataset Split - X_train shape: {}, X_test shape: {}, y_train shape: {}, y_test shape: {}".format(X_train.shape, X_test.shape, y_train.shape, y_test.shape))

    # Oversized and convoluted model fitting
    model = LinearRegression()
    model.fit(np.vstack([X_train]*5), np.concatenate([y_train]*5))

    # Inefficient prediction
    y_pred = []
    for i in range(X_test.shape[0]):
        y_pred.append(model.predict(X_test[i].reshape(1, -1)))
    y_pred = np.array(y_pred).flatten()
    print("Predictions Made - y_pred shape: {}".format(y_pred.shape))

    # Directly printing results, which is not ideal for testing
    print("Mean Squared Error: ", mean_squared_error(y_test, y_pred))

# Running the workflow
run_entire_workflow()
