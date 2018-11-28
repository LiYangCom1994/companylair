import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import learning_curve

from sklearn.metrics import fbeta_score, make_scorer

from sklearn.metrics import r2_score, mean_squared_error, make_scorer
from sklearn.grid_search import GridSearchCV
def plot_learning_curve(clf, title):
    train_sizes, train_scores, test_scores = learning_curve(clf, 
                                                            X, 
                                                            Y, 
                                                            cv=10, 
                                                            n_jobs=-1, 
                                                            train_sizes=np.linspace(.1, 1., 10), 
                                                            verbose=0)

    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)

    plt.figure()
    plt.title(title)
    plt.xlabel("Training examples")
    plt.ylabel("Score")

    # Plot the average training and test score lines at each training set size
    plt.plot(train_sizes, train_scores_mean, 'o-', color="b", label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="r", label="Test score")

    # Plot the std deviation as a transparent range at each training set size
    plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std,  alpha=0.1, color="b")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std, alpha=0.1, color="r")
    plt.legend(loc="best")
def encode(x):
    if (x.dtype is np.dtype('O') and x.name != 'sales') or  x.name == 'date':
        return x.astype('category').cat.codes

    return x

df_tmp = df_tmp.apply(encode)

x_col = df_tmp.columns.values[df_tmp.columns.values != 'sales']

X = df_tmp[x_col].values
Y = df_tmp['sales'].values

display(X)
display(Y)  

dsr = DecisionTreeRegressor(random_state = 0, min_samples_split = 15,  max_depth = 10)

scores = cross_val_score(dsr, X, Y, cv = 15)
display(scores)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

rfr = RandomForestRegressor(n_estimators = 10)

scores = cross_val_score(rfr, X, Y, cv = 10)
display(scores)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
dsr.fit(X, Y)
pre_y_by_dsr = dsr.predict(X)

rfr.fit(X, Y)
pre_y_by_rfr = rfr.predict(X)
f = pd.DataFrame(index=df_tmp.index)
df['month'] = list(map(lambda x: x.month, df_tmp.index.date))

df['pred_by_decision_tree_regressor'] = pre_y_by_dsr
df['pred_by_random_forest_regressor'] = pre_y_by_rfr

df['country'] = df_tmp['country']
df['actual'] = Y

m = df.groupby(['country', 'date'])['pred_by_decision_tree_regressor', 'pred_by_random_forest_regressor', 'actual'].mean()
v = df.groupby(['country', 'date'])['pred_by_decision_tree_regressor', 'pred_by_random_forest_regressor', 'actual'].var()

fig, axes = plt.subplots(len(countries), 2, figsize=(20, 25)) 
for i in range(3):
    m.xs(i).plot(title = countries[i] + " (Mean)", ax = axes[i, 0])
    v.xs(i).plot(title = countries[i] + " (Variance)", ax = axes[i, 1])

    
plt.legend(loc='best')



plot_learning_curve(dsr, "Decision_Tree_Regressor")
plot_learning_curve(rfr, "Random_Forest_Regressor")