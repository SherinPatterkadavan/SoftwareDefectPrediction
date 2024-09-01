import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load the dataset from CSV
data = pd.read_csv('software_defects_dataset.csv')

# Separate features and target
X = data.drop('target_column_name', axis=1)  # Adjust the column name
y = data['target_column_name']  # Adjust the column name

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build and train the DNN model for feature extraction
dnn_model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    Dense(32, activation='relu'),
    Dense(16, activation='relu'),
])

# Compile the DNN model
dnn_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the DNN model
dnn_model.fit(X_train_scaled, y_train, epochs=10, batch_size=64, validation_data=(X_test_scaled, y_test))

# Extract features using the trained DNN model
X_train_features = dnn_model.predict(X_train_scaled)
X_test_features = dnn_model.predict(X_test_scaled)

# Train the kNN classifier on the extracted features
k = 5  # Adjust the value of k as needed
knn_classifier = KNeighborsClassifier(n_neighbors=k)
knn_classifier.fit(X_train_features, y_train)

# Make predictions using the trained kNN classifier
y_pred = knn_classifier.predict(X_test_features)

# Evaluate the performance of the kNN classifier
accuracy = knn_classifier.score(X_test_features, y_test)
print("Accuracy of kNN classifier:", accuracy)
