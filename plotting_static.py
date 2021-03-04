import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()


def potential_to_age(data):
    sns.relplot(kind='line', x='age', y='potential', data=data)
    plt.xlabel("Player's Age")
    plt.ylabel("Player's Potential")
    plt.title("Relationship Between Players' Potential and Their Age")
    plt.savefig('images/potential_age.png')


def potential_to_league_rank(data):
    (fig, [ax1, ax2]) = plt.subplots(2, ncols=1, figsize=(10, 8))

    sns.lineplot(x='league_rank', y='potential', data=data, ax=ax1)
    plt.xlabel('League Level the Players Play at')
    plt.ylabel("Player's Potential")
    ax1.set_title("Players' Potential By League Level They Plat At")

    new_data = data.groupby('league_rank')
    potential_mean = new_data['potential'].mean()
    pot_by_lea = {'league_rank': [1, 2, 3, 4],
                  'potential_mean': potential_mean}
    pot_by_lea = pd.DataFrame(pot_by_lea)

    sns.barplot(x='league_rank', y='potential_mean', data=pot_by_lea,
                ax=ax2)
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