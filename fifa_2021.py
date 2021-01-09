import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

sns.set()


def clean_data(data):
    new_data = data.loc[:, [
        'age',
        'height_cm',
        'weight_kg',
        'overall',
        'potential',
        'value_eur',
        'wage_eur',
        'player_positions',
        'international_reputation',
        'release_clause_eur',
        'shooting',
        'passing',
        'dribbling',
        'defending',
        'physic',
        'league_rank',
        ]]
    return new_data


def potential_to_age(data):
    sns.relplot(kind='line', x='age', y='potential', data=data)
    plt.xlabel("Player's Age")
    plt.ylabel("Player's Potential")
    plt.title("Relationship Between Players' Potential and Their Age")
    plt.savefig('images/potential_age.png')


def potential_to_league_rank(data):
    fig, [ax1, ax2] = plt.subplots(2, ncols=1, figsize=(10, 8))

    sns.lineplot(x='league_rank', y='potential', data=data, ax=ax1)
    plt.xlabel('League Level the Players Play at')
    plt.ylabel("Player's Potential")
    ax1.set_title("Players' Potential By League Level They Plat At")

    new_data = data.groupby('league_rank')
    potential_mean = new_data['potential'].mean()
    print(new_data)
    pot_by_lea = {'league_rank': [1, 2, 3, 4], 'potential_mean': potential_mean}
    pot_by_lea = pd.DataFrame(pot_by_lea)

    sns.barplot(x='league_rank', y='potential_mean', data=pot_by_lea, ax=ax2)
    plt.xlabel('League Level the Players Play at')
    plt.ylabel("Player's Potential")

    plt.savefig('images/league_rank_vs_potential.png')


def overall_to_wage(data):
    data['wage_eur'] = data['wage_eur'] // 100000
    sns.relplot(kind='line', x='overall', y='wage_eur', data=data)
    plt.xlabel("Player's Overall Rating")
    plt.ylabel("Player's Salary in Million")
    plt.title("Relationship Between Players' Wage and Their Overall Ratings"
              )
    plt.savefig('images/overall_to_wage.png')


def skills_ratings_by_positions_data_cleaning(data):
    position_mask = (data['player_positions'] == 'ST') \
                    | (data['player_positions'] == 'CM') \
                    | (data['player_positions'
                    ] == 'CB')
    new_data = data[position_mask]

    new_data = new_data.loc[:, ['shooting', 'passing', 'dribbling',
                            'defending', 'player_positions']]
    new_data = new_data.dropna()

    by_position = new_data.groupby('player_positions')

    d = {'Position': ['CB', 'CM', 'ST']}
    skills = ['shooting', 'passing', 'dribbling', 'defending']

    for element in skills:
        mean_val_name = 'mean_' + element + "_rating"
        skills_mean = list(by_position[element].mean())
        d[mean_val_name] = skills_mean

    df = pd.DataFrame(data=d)
    return df


def skills_ratings_by_positions_data_viz(data):
    (fig, [[ax1, ax2], [ax3, ax4]]) = plt.subplots(2, ncols=2,
                                                   figsize=(9.5, 9.5))

    sns.barplot(x='Position', y='mean_shooting_rating', data=data,
                ax=ax1)
    plt.ylabel('Shooting Ratings')
    ax1.set_title('shooting skills by positions')

    sns.barplot(x='Position', y='mean_passing_rating', data=data,
                ax=ax2)
    plt.ylabel('Passing Rating')
    ax2.set_title('passing skills by positions')

    sns.barplot(x='Position', y='mean_dribbling_rating', data=data,
                ax=ax3)
    plt.ylabel('Dribbling Rating')
    ax3.set_title('dribbling skills by positions')

    sns.barplot(x='Position', y='mean_defending_rating', data=data,
                ax=ax4)
    plt.ylabel('Defending Rating')
    ax4.set_title('defending skills by positions')
    plt.savefig('images/skill_rating_by_position.png')


def predict_position_ml(data):
    elim_gk = data['player_positions'] != 'GK'
    data = data[elim_gk]
    data = data.dropna()

    features = data.loc[:, data.columns != 'player_positions']
    features = pd.get_dummies(features)
    labels = data['player_positions']

    (features_train, features_test, labels_train, labels_test) = \
        train_test_split(features, labels, test_size=0.2,
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
    ax1.set_title('Relationship Between Accuracy (Train&Test) and Max Depth')
    sns.lineplot(x='depth assigned', y='test_accuracy', ax=ax2,
                 data=accuracy_scores)
    plt.savefig('images/train_test_accuracy_predict_positions.png')


def main():
    data = pd.read_csv('dataset/players_21.csv')
    cleaned_data = clean_data(data)
    potential_to_age(cleaned_data)
    potential_to_league_rank(cleaned_data)
    overall_to_wage(cleaned_data)

    position_data = \
        skills_ratings_by_positions_data_cleaning(cleaned_data)
    skills_ratings_by_positions_data_viz(position_data)

    predict_position_ml(cleaned_data)


if __name__ == '__main__':
    main()
