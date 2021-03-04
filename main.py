import pandas as pd
import seaborn as sns
import data_cleaning
import plotting_static
import plotting_interactive
import ml

sns.set()


def main():
    data = pd.read_csv('dataset/players_21.csv')
    cleaned_data = data_cleaning.clean_data(data)
    plotting_static.potential_to_age(cleaned_data)
    plotting_interactive.potential_to_age_interact(cleaned_data)

    plotting_static.potential_to_league_rank(cleaned_data)

    plotting_static.overall_to_wage(cleaned_data)

    position_data = data_cleaning.srbp_data_cleaning(cleaned_data)
    plotting_static.skills_ratings_by_positions_data_viz(position_data)
    plotting_interactive.srbp_interactive(position_data)

    ml.predict_position_ml(cleaned_data)


if __name__ == '__main__':
    main()