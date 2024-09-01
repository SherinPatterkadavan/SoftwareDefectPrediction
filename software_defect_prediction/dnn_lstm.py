import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, LSTM, Input, Concatenate

# Load the dataset from CSV
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
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Normalize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Reshape data for LSTM input (assuming 2D input)
X_train_lstm = X_train_scaled.reshape(X_train_scaled.shape[0], X_train_scaled.shape[1], 1)
X_test_lstm = X_test_scaled.reshape(X_test_scaled.shape[0], X_test_scaled.shape[1], 1)

# Build the LSTM model
lstm_input = Input(shape=(X_train_lstm.shape[1], X_train_lstm.shape[2]))
lstm_layer = LSTM(64)(lstm_input)
lstm_output = Dense(32, activation='relu')(lstm_layer)
lstm_model = Model(inputs=lstm_input, outputs=lstm_output)

# Build the DNN model
dnn_input = Input(shape=(X_train_scaled.shape[1],))
dnn_layer = Dense(64, activation='relu')(dnn_input)
dnn_output = Dense(32, activation='relu')(dnn_layer)
dnn_model = Model(inputs=dnn_input, outputs=dnn_output)

# Concatenate outputs of LSTM and DNN models
concatenated = Concatenate()([lstm_output, dnn_output])

# Final classification layer
output = Dense(1, activation='sigmoid')(concatenated)

# Combine LSTM and DNN models into a single model
combined_model = Model(inputs=[lstm_input, dnn_input], outputs=output)

# Compile the combined model
combined_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the combined model
combined_model.fit([X_train_lstm, X_train_scaled], y_train, epochs=15, batch_size=64, validation_split=0.2)

# Evaluate the combined model
accuracy = combined_model.evaluate([X_test_lstm, X_test_scaled], y_test)
print("Test Accuracy:", accuracy[1])
