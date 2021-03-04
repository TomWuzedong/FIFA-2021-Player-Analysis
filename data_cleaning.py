import pandas as pd
import seaborn as sns

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


def srbp_data_cleaning(data):
    position_mask = (data['player_positions'] == 'ST') \
        | (data['player_positions'] == 'CM') | (data['player_positions'
            ] == 'CB')
    new_data = data[position_mask]

    new_data = new_data.loc[:, ['shooting', 'passing', 'dribbling',
                            'defending', 'player_positions']]
    new_data = new_data.dropna()

    by_position = new_data.groupby('player_positions')

    d = {'Position': ['CB', 'CM', 'ST']}
    skills = ['shooting', 'passing', 'dribbling', 'defending']

    for element in skills:
        mean_val_name = 'mean_' + element + '_rating'
        skills_mean = list(by_position[element].mean())
        d[mean_val_name] = skills_mean

    df = pd.DataFrame(data=d)
    return df
