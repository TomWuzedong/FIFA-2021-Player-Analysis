# FIFA-2021-Player-Analysis
This project focuses on analyzing the data of the players that are included in the newest EA FIFA 2021 video game. The factors of interests are 
mainly each player's wage, market value, release clause, potential, overall rating, and the different skill ratings including shooting, passing, 
tackling, etc. This project also is going to use certain machine learning algorithm to predict a player's position on field using these different 
skill ratings.

### Data Visualization
This is the first and most important part of the analysis. It takes a number of factors such as a player's market value, potential and different 
skills ratings into account and plot the relationship between them.

### Machine Learning
The second part of the analysis uses the DecisionTreeClassifier Model from the python scikit-learn package. It adapts features such as the players' 
shooting, dribbling, passing and defending ratings and predict the position each individual player plays. A plot that shows the correlation between 
the maximum depth of the decision tree and the train and test accuracy is also shown.

