import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

sns.set()


def clean_data(data):
    new_data = data.loc[:, [
        'long_name',
        'age',
        'height_cm',
        'weight_kg',
        'overall',
        'potential',
        'value_eur',
        'wage_eur',
        'player_positions',
        'preferred_foot',
        'international_reputation',
        'weak_foot',
        'release_clause_eur',
        'shooting',
        'passing',
        'dribbling',
        'defending',
        'physic',
        'league_rank'
        ]]
    return new_data


def potential_to_age(data):
    sns.relplot(kind='line', x='age', y='potential', data=data)
    plt.xlabel("Player's Age")
    plt.ylabel("Player's Potential")
    plt.title("Relationship Between Players' Potential and Their Age")
    plt.savefig('potential_age.png')


def potential_to_league_rank(data):
    sns.relplot(kind='line', x='league_rank', y='potential', data=data)
    plt.xlabel("League Level the Players Play at")
    plt.ylabel("Player's Potential")
    plt.title("Relationship Between Players' Potential and the League Level They Plat At")
    plt.savefig('league_rank_vs._Potential.png')


def main():
    data = pd.read_csv('dataset/players_21.csv')
    cleaned_data = clean_data(data)
    potential_to_age(cleaned_data)
    potential_to_league_rank(cleaned_data)


if __name__ == '__main__':
    main()
