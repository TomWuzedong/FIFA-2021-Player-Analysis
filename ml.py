import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

sns.set()


def predict_position_ml(data):
    elim_gk = data['player_positions'] != 'GK'
    data = data[elim_gk]
    data = data.dropna()

    features = data.loc[:, data.columns != 'player_positions']
    features = pd.get_dummies(features)
    labels = data['player_positions']

    (features_train, features_test, labels_train, labels_test) = \
        train_test_split(features, labels, test_size=0.3,
                         random_state=1)

    accuracy_scores = []
    for i in range(1, 50, 5):
        model = DecisionTreeClassifier(max_depth=i, random_state=1)
        model.fit(features_train, labels_train)

        train_predictions = model.predict(features_train)
        train_accuracy = accuracy_score(labels_train, train_predictions)

        test_predictions = model.predict(features_test)
        test_accuracy = accuracy_score(labels_test, test_predictions)

        accuracy_scores.append({'depth assigned': i,
                                'train_accuracy': train_accuracy,
                                'test_accuracy': test_accuracy})

    accuracy_scores = pd.DataFrame(accuracy_scores)
    (fig, [ax1, ax2]) = plt.subplots(2, ncols=1)
    sns.lineplot(x='depth assigned', y='train_accuracy', ax=ax1,
                 data=accuracy_scores)
    ax1.set_title('Relationship Between Accuracy (Train&Test) and Max Depth'
                  )
    sns.lineplot(x='depth assigned', y='test_accuracy', ax=ax2,
                 data=accuracy_scores)
    plt.savefig('images/train_test_accuracy_predict_positions.png')