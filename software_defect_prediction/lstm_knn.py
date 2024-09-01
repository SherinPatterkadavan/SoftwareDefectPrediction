import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
# Load the dataset from CSV
import csv
from imblearn.over_sampling import SMOTE
# Define the path to your CSV file
csv_file_path = "jm1.csv"
defects=["Functional_Defects","Performance_Defect","Compatability_Defect","Usability_Defect","Security_Defect","Reliability_defect"]
# Open the CSV file in read mode

def type_det(row):
    s=len(row)//len(defects)
    r=[]

    for i in range(len(defects)):
        print(row[(i*int(s)):(i*int(s))+int(s)],"======================")
        xx=sum(row[(i*int(s)):(i*int(s))+int(s)])
        r.append(xx)
    max_value = max(r)
    max_index = r.index(max_value)
    print("*&*&*&*&*&*&*&*&*&*&&(&(&*(((**&&^^%$#@@")
    print(max_index)
    print(defects[max_index])
    return defects[max_index]

x=[]
y=[]
tc=0
fc=0
with open(r"C:\Users\sheri\OneDrive\Desktop\software_defect_prediction\software_defect_predictionn(2)\software_defect_prediction\sdp\jm1.csv", "r", newline="") as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Each row is a list representing the fields in that row
        # print(row)
        try:
            # print(len(row))
            r=row[:21]
            e1=[]
            for j in r:
                e1.append(float(j))
            if e1 not in x:
                if row[21]=="false":

                        y.append(0)
                        fc=fc+1
                        x.append(e1)
                else:
                    print(e1,"++++++++%%%%%%%%%%%%%%%%%%%%%%")
                    y.append(1)
                    tc=tc+1
                    x.append(e1)

        except:
            print("*************************************************")
smote = SMOTE(random_state=42)
print(len(x))
x, y = smote.fit_resample(x, y)
print(len(x))
print(x[0])
print(y[0])
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Normalize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(x)
X_test_scaled = scaler.transform(X_test)
print(X_train_scaled[0],"@@@@@@@@@@@@")
# Reshape data for LSTM input (assuming 2D input)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Normalize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(x)
X_test_scaled = scaler.transform(X_test)

# Reshape data for LSTM input (assuming 2D input)
X_train_lstm = X_train_scaled.reshape(X_train_scaled.shape[0], X_train_scaled.shape[1], 1)
X_test_lstm = X_test_scaled.reshape(X_test_scaled.shape[0], X_test_scaled.shape[1], 1)

# Build the LSTM model
lstm_model = Sequential([
    LSTM(64, input_shape=(X_train_lstm.shape[1], X_train_lstm.shape[2])),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')  # Output layer for binary classification
])

# Compile the LSTM model
lstm_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the LSTM model
lstm_model.fit(X_train_lstm, y, epochs=10, batch_size=64, validation_split=0.2)

# Extract features using the trained LSTM model
print(X_train_lstm[0],"%$%$%$%$%$%$%$%$%$%")
print(X_train_lstm[0],"*********************")
print(X_train_lstm[0],"*********************")
print(X_train_lstm[0],"*********************")
print(X_train_lstm[0],"*********************")
print(X_train_lstm[0],"*********************")
print(X_train_lstm[0],"*********************")
print(X_train_lstm[0],"*********************")
X_train_features = lstm_model.predict(X_train_lstm)
X_test_features = lstm_model.predict(X_test_lstm)
print(X_train_features[0],"------------------")
print(X_train_features[0],"------------------")
print(X_train_features[0],"------------------")
# Train the kNN classifier on the extracted features
k = 1  # Adjust the value of k as needed
knn_classifier = KNeighborsClassifier(n_neighbors=k)
knn_classifier.fit(x, y)

# Make predictions using the trained kNN classifier
# y_pred = knn_classifier.predict(X_test_features)

# Evaluate the performance of the kNN classifier
# accuracy = knn_classifier.score(X_test_features, y_test)
# print("Accuracy of kNN classifier:", accuracy)

def predictfn(row):
    # res=lstm_model.predict([[row]])
    res=row
    # for i in row:
    #     res.append(i[0])
    y_pred = knn_classifier.predict([res])
    print(y_pred[0],"+_+_+_+_+_+_+_+_++_+++++")
    print(y_pred[0],"+_+_+_+_+_+_+_+_++_+++++")
    print(y_pred[0],"+_+_+_+_+_+_+_+_++_+++++")
    print(y_pred[0],"+_+_+_+_+_+_+_+_++_+++++")
    print(y_pred[0],"+_+_+_+_+_+_+_+_++_+++++")

    if y_pred[0]==0:
        return type_det(res)
    return y_pred[0]