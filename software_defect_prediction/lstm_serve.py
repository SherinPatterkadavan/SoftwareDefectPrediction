import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
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
print(len(x))
print(x[0])
print(y[0])
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)

# Normalize features
scaler = StandardScaler()
x = scaler.fit_transform(x)
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Reshape data for LSTM input (assuming 2D input)
x = x.reshape(x.shape[0], x.shape[1], 1)
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)
#
# # Build the LSTM model
# model = Sequential([
#     LSTM(64, input_shape=(X_train.shape[1], 1)),
#     Dropout(0.5),
#     Dense(32, activation='relu'),
#     Dropout(0.5),
#     Dense(2, activation='sigmoid')  # Adjust output units based on your problem
# ])
#
# # Compile the model
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
#
# # Train the model
# model.fit(X_train, y_train, epochs=10, batch_size=64, validation_data=(X_test, y_test))
#
#
# res=model.predict(X_test)
#
# print(res)


# Reshape data for LSTM input (assuming 2D input)
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# Build the LSTM model
model = Sequential([
    LSTM(64, input_shape=(X_train.shape[1], 1)),
    Dropout(0.5),
    Dense(32, activation='relu'),
    Dropout(0.5),
    Dense(2, activation='softmax')  # For binary classification with two classes
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x, y, epochs=10, batch_size=64, validation_data=(X_test, y_test))

res=model.predict(X_test)
print(res)
count=0
for i in range(len(y_test)):
    op=1
    if res[i][0]>res[i][1]:
        op=0
    print(op,y_test[i])
    if op==y_test[i]:
        count=count+1
print(count/len(y_test))