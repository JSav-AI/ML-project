import pandas as pd



#load files 
df = pd.read_csv('/Users/jacksavage/fpl_ml/2024_25_merged_clean.csv')
teams = pd.read_csv("/Users/jacksavage/Downloads/Fantasy-Premier-League-master/data/2021-22/teams.csv")


#filter and create dictionary 
teams__cols = teams.filter(items=['id', 'name'], axis=1)
team_dict = dict(zip(teams__cols['id'], teams__cols['name']))

#map dictionary 
df['opponent_team'] = df['opponent_team'].map(team_dict)


#feature engineering 
df['win'] = (df['was_home'] == True ) & (df['team_a_score'] < df['team_h_score'])
df['score_difference'] = abs(df['team_h_score'] - df['team_a_score'])

df.to_csv('24_25_final.csv', index=False)









