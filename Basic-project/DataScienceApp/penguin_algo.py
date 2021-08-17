import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

penguins = pd.read_csv(
    '/media/nagachi/Nagachi/Datasets/data-master/penguins_cleaned.csv')

df = penguins.copy()
target = 'species'
encode = ['island', 'sex']

print(df.head())

# Encode categoricacl column
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df, dummy], axis=1)
    del df[col]

target_mapper = {'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}


def target_encode(numValue):
    return target_mapper[numValue]


df['species'] = df['species'].apply(target_encode)

X = df.drop('species', axis=1)
y = df['species']

clf = RandomForestClassifier()
clf.fit(X, y)
pickle.dump(clf, open('Basic-project/DataScienceApp/penguins_clf.pkl', 'wb'))
