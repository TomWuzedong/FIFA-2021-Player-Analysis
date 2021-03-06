import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def potential_to_age_interact(data):
    """
    This function uses the plotly package and creates an interactive
    line plot and bar plot that shows the relationship between players' age
    and the number of players with above-mean potential.
    it involves a preprocessing step, which is grouping the dataset by age and
    making a new dataframe whose columns are the age values and the number of
    players with above-mean potential corresponding to each age.
    """
    mean_potential = data['potential'].mean()
    high_data = data[data['potential'] >= mean_potential]
    by_age = high_data.groupby('age')['potential'].count()

    dic = {'age': [],
           '# players have greater than or equal to avg potential': []}
    for i in range(16, 43, 1):
        dic['age'].append(i)
        dic['# players have greater than or equal to avg \
            potential'].append(by_age[i])
    new_data = pd.DataFrame(data=dic)

    fig = px.line(new_data, x='age',
                  y='# players have greater than or equal to avg potential',
                  title="Relationship Between Players' Potential and Their Age")
    fig1 = \
        px.bar(new_data, x='age',
               y='# players have greater than or equal to avg potential',
               title="Relationship Between Players' Potential and Their Age")

    fig.show()
    fig1.show()


def srbp_interactive(data):
    """
    This function makes use of the preprocessed (by the srbp_data_cleaning
    function in data_cleaning.py) position data and plots different skill
    ratings (shooting, passing, dribbling, defending) by position (ST, CM, CB)
    using bar plots, which are assigned into four subplots. The plots are
    and they make use of the plotly package.
    """
    fig = make_subplots(rows=2, cols=2)
    fig.add_trace(
        go.Bar(x=data['Position'], y=data['mean_shooting_rating'],
               name='mean_shooting_rating'), row=1, col=1)
    fig.add_trace(
        go.Bar(x=data['Position'], y=data['mean_passing_rating'],
               name='mean_passing_rating'), row=1, col=2)
    fig.add_trace(
        go.Bar(x=data['Position'], y=data['mean_dribbling_rating'],
               name='mean_dribbling_rating'), row=2, col=1)
    fig.add_trace(
        go.Bar(x=data['Position'], y=data['mean_defending_rating'],
               name='mean_defending_rating'), row=2, col=2)
    fig.update_layout(height=600, width=800,
                      title_text="mean_skills_ratings_by_positions")
    fig.show()
