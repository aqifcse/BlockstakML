import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

def readData():
    df = pd.read_excel('bank_data.xlsx')
    return df

def preProcessData():
    df = readData()

    encoder = LabelEncoder()
    df['job'] = encoder.fit_transform(df['job'])
    df['marital'] = encoder.fit_transform(df['marital'])
    df['education'] = encoder.fit_transform(df['education'])
    df['default'] = encoder.fit_transform(df['default'])
    df['housing'] = encoder.fit_transform(df['housing']) 
    df['loan'] = encoder.fit_transform(df['loan']) 
    df['contact'] = encoder.fit_transform(df['contact'])
    df['month'] = encoder.fit_transform(df['month'])
    df['poutcome'] = encoder.fit_transform(df['poutcome']) 
    df['y'] = encoder.fit_transform(df['y']) 

    return df

def gaussianNaiveBayes():
    df = preProcessData()

    # Split the data into features and target variable
    X = df.drop('y', axis=1)
    y = df['y']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Naive Bayes Classifier
    naive_bayes = GaussianNB()
    naive_bayes.fit(X_train, y_train)

    # Make predictions
    naive_bayes_predictions = naive_bayes.predict(X_test)

    naive_bayes_accuracy_score = accuracy_score(y_test, naive_bayes_predictions)

    nBOutput = { 
        'accuracy': "{:.2f}%".format(naive_bayes_accuracy_score * 100),
        'classification_report': classification_report(y_test, naive_bayes_predictions)
    }

    return nBOutput


def decisionTree():
    
    df = preProcessData()

    # Split the data into features and target variable
    X = df.drop('y', axis=1)
    y = df['y']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Decision Tree Classifier
    decision_tree = DecisionTreeClassifier(random_state=42)
    decision_tree.fit(X_train, y_train)

    decision_tree_predictions = decision_tree.predict(X_test)

    decision_tree_accuracy_score = accuracy_score(y_test, decision_tree_predictions)

    dTOutput = { 
        'accuracy': "{:.2f}%".format(decision_tree_accuracy_score * 100),
        'classification_report': classification_report(y_test, decision_tree_predictions)
    }

    return dTOutput


























