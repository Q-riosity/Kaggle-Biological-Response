import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def main():
    # create the training & test sets
    dataset = pd.read_csv('train.csv')

    target = dataset.Activity.values
    train = dataset.drop('Activity', axis=1).values

    test = pd.read_csv('test.csv').values

    # create and train the random forest
    rf = RandomForestClassifier(n_estimators=100, n_jobs=-1)
    rf.fit(train, target)
    predicted_probs = [x[1] for x in rf.predict_proba(test)]
    predicted_probs = pd.Series(predicted_probs)

    predicted_probs.to_csv('submission.csv', index=False,
                            float_format="%f")

   

if __name__ == "__main__":
    main()
