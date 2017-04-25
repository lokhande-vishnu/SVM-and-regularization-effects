import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_score, KFold
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier

def read_data():
    data =  pd.read_csv('test.csv')
    data.replace(np.nan,0)
    #print(data.head(5))
    return data

def extract_features(data):
    # Text to vectors
    vectorizer = CountVectorizer()
    X_vectors = vectorizer.fit_transform(data.Text)
    #print(X_vectors.shape)

    # vectors to tfidf scores
    tfidf_transformer = TfidfTransformer()
    X = tfidf_transformer.fit_transform(X_vectors)
    #print(X.shape)

    # Labels
    y =  data.Label
    #print(y.shape)

    return X,y

def classify(X,y):
    # Choose the classifier
    #    clf1 = MuAltinomialNB()
    clf1 = SGDClassifier()


    # Training accuracy
    clf1_trained = clf1.fit(X, y)
    y_pred = clf1_trained.predict(X)
    print('training accuracy')
    print(metrics.classification_report(y, y_pred))
    print(metrics.confusion_matrix(y, y_pred))

    # Cross-validation
    n_folds = 3
    precision = cross_val_score(clf1, X, y, cv=n_folds, n_jobs=1, scoring='precision')
    recall = cross_val_score(clf1, X, y, cv=n_folds, n_jobs=1, scoring='recall')
    print('average precision-recall for cross-validation')
    print('precision', precision)
    print('recall', recall)
    print(np.mean(precision),np.std(precision))
    print(np.mean(recall),np.std(recall))

    # Cross-validation2
    print('individual precision-recall for cross-validation')
    k_fold = KFold(n_splits=n_folds)
    for train, test in k_fold.split(X):
        clf1_trained = clf1.fit(X[train],y[train])
        y_pred = clf1_trained.predict(X[test])
        print(metrics.classification_report(y[test], y_pred))
        print(metrics.confusion_matrix(y[test], y_pred))

def grid_search(data):
    text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB()),
                         ])

if __name__ == '__main__':
    data = read_data();
    grid_search(data);
    
    X,y = extract_features(data);
    classify(X,y);
