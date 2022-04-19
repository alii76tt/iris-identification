import os
from pathlib import Path
import numpy as np
import pandas as pd
# test and training
from sklearn.model_selection import train_test_split
# modelling
from sklearn.neural_network import MLPClassifier
# model evaluation
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

BASE_DIR = Path(__file__).resolve().parent.parent


def getIris(sl, sw, pl, pw):
    # data preparation
    attribute_name = ["SL", "SW", "PL", "PW", "CLASS"]

    # data read
    iris = os.path.join(BASE_DIR, 'static', 'iris.data')
    data = pd.read_csv(iris, names=attribute_name)

    inputs = data.iloc[0:150, 0:4]
    target = data.iloc[:, -1:]

    # test - training
    x_train, x_test, y_train, y_test = train_test_split(
        inputs, target, test_size=0.3, random_state=2)

    # modelling
    nnc = MLPClassifier(solver='lbfgs', alpha=1e-5,
                        hidden_layer_sizes=(3, 3), random_state=1)

    nnc.fit(x_train.values, y_train)

    # predict
    predictions_test = nnc.predict(x_test)

    predictions_train = nnc.predict(x_train)

    # model evaluation
    acs_test = accuracy_score(y_test, predictions_test)
    acs_train = accuracy_score(y_train, predictions_train)

    print("acs_test:" + str(acs_test))
    print("acs_train:" + str(acs_train))

    cm_test = confusion_matrix(y_test, predictions_test)
    cm_train = confusion_matrix(y_train, predictions_train)

    print("cm_test:" + str(cm_test))
    print("cm_train:" + str(cm_train))

    # deployment
    new_input = [sl, sw, pl, pw]
    ni = np.array(new_input)
    ni = np.reshape(ni, (1, -1))

    _predict = nnc.predict(ni)

    return _predict
