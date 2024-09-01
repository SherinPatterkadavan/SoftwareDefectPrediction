import csv
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, Dropout

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

            if row[21]=="false":
                if fc>2780:
                    pass
                else:
                    y.append(0)
                    fc=fc+1
                    x.append(e1)
            else:
                y.append(1)
                tc=tc+1
                x.append(e1)

        except:
            print("*************************************************")

print(x)
print(y)
print(tc,fc)
print(tc,fc)
print(tc,fc)
print(tc,fc)
print("#############################################################33")

from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

# Create the RFE object and rank features
estimator = LogisticRegression()
selector = RFE(estimator, n_features_to_select=15, step=1)
selector = selector.fit(x, y)
print(selector.support_)
x1=[]
for i in x:
    r=[]
    for k in range(0,len(i)):
        if selector.support_[k]:
            r.append(i[k])
    x1.append(r)

# import pandas as pd
import numpy as np
# from keras.models import Sequential
# from keras.layers import LSTM, Dense
#
# # Load data from CSV file using pandas
# data = pd.read_csv(r'C:\Users\sheri\OneDrive\Desktop\software_defect_prediction\software_defect_predictionn(2)\software_defect_prediction\sdp\jm1.csv')
#
# # Convert data to numpy array
# data = data.values
#
# # Split the data into input (X) and output (y) variables
# X =np.array(x) # Input features
X=np.array(x1)
y = np.array(y)   # Output variable
#
# # Normalize the input data (optional but recommended for neural networks)
# X = X / np.max(X)
#
# # Reshape input data into 3D array [samples, time steps, features]
# X = X.reshape(X.shape[0], 1, X.shape[1])
#
# # Define the LSTM model
# model = Sequential()
# model.add(LSTM(50, input_shape=(X.shape[1], X.shape[2])))
# model.add(Dense(1))
# model.compile(loss='mean_squared_error', optimizer='adam')
#
# # Train the model
# model.fit(X, y, epochs=100, batch_size=1, verbose=1)
#
# # Make predictions
# predictions = model.predict(X)
#
# # Print predictions
# print(predictions)


# import pandas as pd
# import numpy as np
# from keras.models import Sequential
# from keras.layers import LSTM, Dense
# from sklearn.metrics import accuracy_score
# from sklearn.model_selection import train_test_split
#
# # Load data from CSV file using pandas
# # data = pd.read_csv('data.csv')
# #
# # # Convert data to numpy array
# # data = data.values
# #
# # # Split the data into input (X) and output (y) variables
# # X = data[:, 0:-1]  # Input features
# # y = data[:, -1]    # Output variable
#
# # Normalize the input data (optional but recommended for neural networks)
# X = X / np.max(X)
#
# # Reshape input data into 3D array [samples, time steps, features]
# X = X.reshape(X.shape[0], 1, X.shape[1])
#
# # Split data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # Define the LSTM model
# model = Sequential()
# model.add(LSTM(50, input_shape=(X_train.shape[1], X_train.shape[2])))
# model.add(Dense(1))
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#
# # Train the model
# model.fit(X_train, y_train, epochs=195, batch_size=1, verbose=1)
#
# # Evaluate the model on the test set
# _, accuracy = model.evaluate(X_test, y_test, verbose=0)
# print('Accuracy:', accuracy)
#
# # Make predictions
# predictions = model.predict_classes(X_test)
#
# # Calculate accuracy score
# accuracy = accuracy_score(y_test, predictions)
# print('Accuracy Score:', accuracy)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

import math
from tensorflow.keras.callbacks import LearningRateScheduler
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train[0],"==========================================")
print(X_train[0],"==========================================")
print(len(X_train[0]),"==========================================")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define the model
# model = Sequential([
#     Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
#     Dense(64, activation='relu'),
#     Dense(1, activation='sigmoid')  # Output layer for binary classification
# ])
#
# # Compile the model
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
#
# # Train the model
# model.fit(X_train_scaled, y_train, epochs=64, batch_size=64, validation_split=0.1)
#
# # Evaluate the model
# loss, accuracy = model.evaluate(X_test_scaled, y_test)
# print('Test Loss:', loss)
# print('Test Accuracy:', accuracy)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define the model
# model = Sequential([
#     Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
#     Dense(32, activation='relu'),
#     Dense(1, activation='sigmoid')  # Output layer for binary classification
# ])
#
# # Compile the model
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
#
# # Learning rate scheduler
# def lr_scheduler(epoch, lr):
#     if epoch % 10 == 0:
#         return lr * math.exp(-0.1)
#     else:
#         return lr
#
# lr_schedule = LearningRateScheduler(lr_scheduler)
#
# # Train the model with learning rate scheduler
# model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.1, callbacks=[lr_schedule])
#
# # Evaluate the model
# loss, accuracy = model.evaluate(X_test, y_test)
# print('Test Loss:', loss)
# print('Test Accuracy:', accuracy)
#
# def create_model(input_shape, num_classes):
#     model = Sequential()
#
#     # Convolutional layers for feature extraction
#     model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
#     model.add(MaxPooling2D((2, 2)))
#     model.add(Conv2D(64, (3, 3), activation='relu'))
#     model.add(MaxPooling2D((2, 2)))
#     model.add(Conv2D(64, (3, 3), activation='relu'))
#     model.add(Flatten())
#
#     # Fully connected layers for classification
#     model.add(Dense(64, activation='relu'))
#     model.add(Dropout(0.5))
#     model.add(Dense(num_classes, activation='softmax'))
#
#     return model


# Compile the model
# model=create_model((1,1,21),2)
# # model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
#
# # Train the model
# model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))
#
# # Evaluate the model
# test_loss, test_accuracy = model.evaluate(X_test, y_test)
# print("Test Accuracy:", test_accuracy)

print(X_train.shape[1], 1,"++++++++++++++++++")
print(X_train.shape[1], 1,"++++++++++++++++++")
print(X_train.shape[1], 1,"++++++++++++++++++")
print(X_train.shape[1], 1,"++++++++++++++++++")
print(X_train.shape[1], 1,"++++++++++++++++++")
print(X_train.shape[1], 1,"++++++++++++++++++")

# Build the CNN model
model = Sequential([
    Conv1D(12, kernel_size=3, activation='relu', input_shape=(1,X_train.shape[1])),
    MaxPooling1D(pool_size=2),
    Conv1D(64, kernel_size=3, activation='relu'),
    MaxPooling1D(pool_size=2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')  # Adjust output units based on your problem
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=64, validation_data=(X_test, y_test))
