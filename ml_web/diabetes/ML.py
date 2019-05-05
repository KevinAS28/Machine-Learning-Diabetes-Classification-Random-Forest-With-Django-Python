

def importModule():
    print("importing module from anaconda...")
    global csvcpp
    global RandomForestClassifier
    global train_test_split
    global plot
    global pandas
    global sb
    import csvcpp
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    import matplotlib.pyplot as plot
    import pandas
    import seaborn as sb

def generateDataFrame(csvFileName):
    df = pandas.DataFrame(csvcpp.listCsvRead(csvFileName))
    df.columns = df.iloc[0]
    df = df.reindex(df.index.drop(0))
    df = df.dropna()
    return df

def graphY(dataFrame):
    plot.figure()
    plot.title("Total Of Diabetes")
    sb.countplot(dataFrame["Outcome"], label="Count")
    plot.figtext(.02, -0.07, "1 = Diabetes | 0 = Healthy", color="m", size=15)
    plot.xlabel("Negative | Positive")
    plot.show()
    print("\n"*5)

def randomForest(dataFrame):
    rf = RandomForestClassifier(n_estimators=500, random_state=0)    
    return rf

#return [train_accuracy, test_accuracy]
def getAccuracy(rf, df):
    X_train, X_test, y_train, y_test = train_test_split(df.loc[:, df.columns != 'Outcome'], df['Outcome'], stratify=df['Outcome'], random_state=66)    
    fit = rf.fit(X_train, y_train)    
    return [fit, rf.score(X_train, y_train), rf.score(X_test, y_test)]
#    print("Accuracy on training set: {:.3f}".format(rf.score(X_train, y_train)))
#    print("Accuracy on test set: {:.3f}".format(rf.score(X_test, y_test))) 
    
def main(fileCSV):
    importModule()
    df = generateDataFrame(fileCSV)
    rf = randomForest(df)
    rf, train_score, test_score = getAccuracy(rf, df)
    print(rf.predict([[6, 148, 72, 35, 0, 33.6, 0.627, 50]]))
    print(rf.predict([[1, 85, 66, 29, 0, 26.6, 0.351, 31]]))
    print(test_score)
    return 0

def getResult(fileCSV, data):
    importModule()
    df = generateDataFrame(fileCSV)
    rf = randomForest(df)
    rf, train_score, test_score = getAccuracy(rf, df)
    return [(rf.predict([data]))[0], test_score]
    
if __name__=="__main__":
    csvFile = "/media/kevin/data/programming/AI/Diabetes/ml_web/diabetes/diabetes.csv"
    print("Machine Learning For Diabetes Classification By Kevin Agusto")
    print("Processing...")
    negative = [1, 85, 66, 29, 0, 26.6, 0.351, 31]
    positive = [6, 148, 72, 35, 0, 33.6, 0.627, 50]
    data = negative
    classification, accuracy = getResult(csvFile, data)
    df = generateDataFrame(csvFile)
    graphY(df)    
    print("This machine learning accuracy is {}%".format(accuracy*100))
    print("with the data: ", str(data))
    print("This machine learning classificate of diabetes is {}".format(bool(int(classification))))
    
    