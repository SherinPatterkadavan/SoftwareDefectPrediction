import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

import csv
from imblearn.over_sampling import SMOTE
# Define the path to your CSV file
csv_file_path = "jm1.csv"

# Open the CSV file in read mode
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

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Normalize features
scaler = StandardScaler()
x = scaler.fit_transform(x)
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build and train the DNN model
dnn_model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    Dense(32, activation='relu'),
    Dense(16, activation='relu'),
    Dense(8, activation='relu'),
])

# Compile the DNN model
dnn_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the DNN model
dnn_model.fit(x, y, epochs=10, batch_size=64, validation_data=(X_test_scaled, y_test))

# Extract features using the trained DNN model
X_train_features = dnn_model.predict(x)
X_test_features = dnn_model.predict(X_test_scaled)

# Train the kNN classifier on the extracted features
k = 1  # Adjust the value of k as needed
knn_classifier = KNeighborsClassifier(n_neighbors=k)
knn_classifier.fit(X_train_features, y)

# Make predictions using the trained kNN classifier
y_pred = knn_classifier.predict(X_test_features)



# Evaluate the performance of the kNN classifier
accuracy = knn_classifier.score(X_test_features, y_test)
print("Accuracy of kNN classifier:", accuracy)
