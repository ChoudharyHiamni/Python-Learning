#Scikit-learn is a Python machine learning library used for data analysis, machine learning, and predictive modeling. It provides simple and efficient tools for classification, regression, clustering, and model evaluation.

#It is built on NumPy, Pandas, and Matplotlib.

import sklearn

                  # Common Scikit-Learn Modules

# sklearn.linear_model

# sklearn.tree

# sklearn.neighbors

# sklearn.cluster

# sklearn.preprocessing

# sklearn.model_selection

# sklearn.metrics


                # Typical Machine Learning Workflow (Interview Favorite)

# Import dataset

# Preprocess data

# Split data into train & test

# Choose model

# Train model

# Make predictions

# Evaluate mode


           #TRAIN-TEST SPLIT
from sklearn.model_selection import train_test_split
X = df[['Age', 'Salary']]
y = df['Purchased']


X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42
)
 
          #LINEAR REGRESSION  :USED FOR CONTINUOUS VALUE PREDICTION
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


             #LOGISTIC REGRESSION:USED FOR BINARY CLASSIFICATION
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

               #KNN
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)

            #DECISION TREE
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

              #KMEAN CLUSTERING(UNSUPERVISED)
from sklearn.cluster import KMeans
model = KMeans(n_clusters=3)
model.fit(X)

                   #DATA PREPROCESSING
        #HANDLING MISSING VALUES
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)

       #FEATURE SCALING
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)


                 #MODEL EVALUATION MATRIX
# For Regression
      #  Mean Absolute Error (MAE)
      # Mean Squared Error (MSE)
      # R² Score
from sklearn.metrics import mean_squared_error, r2_score

# For Classification:
         # Accuracy
        # Precision
         # Recall
       # F1 Score
from sklearn.metrics import accuracy_score

    #CONFUSION MATRIX

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)

    #PIPELINE
from sklearn.pipeline import Pipeline


pipeline = Pipeline([
('scaler', StandardScaler()),
('model', LogisticRegression())
])


#CROSS-VALIDATION
from sklearn.model_selection import cross_val_score


scores = cross_val_score(model, X, y, cv=5)






# Scikit-learn is used for machine learning in Python

# It supports supervised and unsupervised learning

# Train-test split avoids overfitting

# Scaling improves model performance