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


def skills_ratings_by_positions_data_cleaning(data):
    position_mask = (data['player_positions'] == 'ST') \
        | (data['player_positions'] == 'CM') | (data['player_positions'] == 'CB')
    new_data = data[position_mask]

    new_data = new_data.loc[:, ['shooting', 'passing', 'dribbling',
                                'defending', 'player_positions']]
    new_data = new_data.dropna()

    by_position = new_data.groupby('player_positions')

    shooting_skills = list(by_position['shooting'].mean())
    passing_skills = list(by_position['passing'].mean())
    dribbling_skills = list(by_position['dribbling'].mean())
    defending_skills = list(by_position['defending'].mean())

    d = {'Position': ['CB', 'CM', 'ST'],
         'Mean_Shooting_Rating': [element for element in shooting_skills],
         'Mean_Passing_Rating': [element for element in passing_skills],
         'Mean_Dribbling_Rating': [element for element in dribbling_skills],
         'Mean_Defending_Rating': [element for element in defending_skills]
         }

    df = pd.DataFrame(data=d)
    return df


def skills_ratings_by_positions_data_viz(data):
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, ncols=2, figsize=(7, 7))

    sns.barplot(x='Position', y='Mean_Shooting_Rating', data=data, ax=ax1)
    plt.ylabel('Shooting Ratings')

    sns.barplot(x='Position', y='Mean_Passing_Rating', data=data, ax=ax2)
    plt.ylabel('Passing Rating')

    sns.barplot(x='Position', y='Mean_Dribbling_Rating', data=data, ax=ax3)
    plt.ylabel('Dribbling Rating')

    sns.barplot(x='Position', y='Mean_Defending_Rating', data=data, ax=ax4)
    plt.ylabel('Defending Rating')

    plt.savefig('Skill_Ratings_By_Positions')


def main():
    data = pd.read_csv('dataset/players_21.csv')
    cleaned_data = clean_data(data)
    potential_to_age(cleaned_data)
    potential_to_league_rank(cleaned_data)
    position_data = skills_ratings_by_positions_data_cleaning(cleaned_data)
    skills_ratings_by_positions_data_viz(position_data)


if __name__ == '__main__':
    main()
