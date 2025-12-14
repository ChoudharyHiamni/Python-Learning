
# ## 1. What is TensorFlow?

     # TensorFlow is an **open-source deep learning framework** developed by Google. It is used to build, train, and deploy **machine learning and deep learning models**, especially neural networks.

     # 👉 TensorFlow is mainly used for **Deep Learning, Neural Networks, and AI applications**.

# ---

# ## 2. Why Use TensorFlow?

# * Supports **deep neural networks**
# * Scalable (runs on CPU, GPU, TPU)
# * Used in real-world AI applications
# * Strong industry demand

# ---

# ## 3. Installing and Importing TensorFlow

# ```python
# pip install tensorflow
# ```

# ```python
# import tensorflow as tf
# print(tf.__version__)
# ```

# ---

# ## 4. Key Concepts in TensorFlow

                 # ###             4.1 Tensors

# A **tensor** is a multi-dimensional array (similar to NumPy array).

# ```python
# t = tf.constant([1, 2, 3])
# print(t)
# ```

# ---

                                  # ### 4.2 Computational Graph

# TensorFlow represents computations as a **graph of operations** (used internally for optimization).

# ---

# ## 5. TensorFlow vs Keras

# | Feature     | TensorFlow     | Keras          |
# | ----------- | -------------- | -------------- |
# | Level       | Low-level      | High-level API |
# | Ease of use | Complex        | Easy           |
# | Usage       | Backend engine | Model building |

# 📌 Keras is now **integrated inside TensorFlow** (`tf.keras`).

# ---

                         # ## 6. TensorFlow Workflow (Very Important for Interview)

# 1. Import libraries
# 2. Load dataset
# 3. Preprocess data
# 4. Build model
# 5. Compile model
# 6. Train model
# 7. Evaluate model
# 8. Make predictions

# ---

                           # ## 7. Building First Neural Network (Using Keras)

# ```python
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense

# model = Sequential([
#     Dense(64, activation='relu', input_shape=(10,)),
#     Dense(1, activation='sigmoid')
# ])
# ```

# ---

#                        ## 8. Compiling the Model

# ```python
# model.compile(
#     optimizer='adam',
#     loss='binary_crossentropy',
#     metrics=['accuracy']
# )
# ```

# ---

                          # ## 9. Training the Model

# ```python
# model.fit(X_train, y_train, epochs=10, batch_size=32)
# ```

# ---

                           # ## 10. Model Evaluation

# ```python
# model.evaluate(X_test, y_test)
# ```

# ---

                             # ## 11. Making Predictions

# ```python
# predictions = model.predict(X_test)
# ```

# ---

                          # ## 12. Activation Functions

# * ReLU – most commonly used
# * Sigmoid – binary classification
# * Softmax – multi-class classification

# ---

                           # ## 13. Loss Functions

# * Mean Squared Error – regression
# * Binary Crossentropy – binary classification
# * Categorical Crossentropy – multi-class

# ---

                                # ## 14. Optimizers

# * SGD
# * Adam (most popular)
# * RMSprop

# ---

                           # ## 15. Overfitting & Underfitting

# * **Overfitting**: model performs well on training but poorly on testing
# * **Underfitting**: model performs poorly on both

# ### Solution:

# * More data
# * Regularization
# * Dropout

# ---

                                     # ## 16. Dropout Layer

# ```python
# from tensorflow.keras.layers import Dropout

# model.add(Dropout(0.5))
# ```

# ---

                                  # ## 17. CNN (Basic Idea)

# Used for **image data**.

# Layers:

# * Convolution
# * Pooling
# * Fully Connected

# ---

                        # ## 18. RNN (Basic Idea)

# Used for **sequence data** like text and time-series.

# ---

                     # ## 19. Advantages of TensorFlow

# * Production-ready
# * Supports large-scale models
# * Strong ecosystem

# ---

                       # ## 20. Limitations of TensorFlow

# * Steep learning curve
# * Debugging is complex

# ---

                    # ## 21. One-Line Interview Answers

# * TensorFlow is used for deep learning
# * Tensors are multi-dimensional arrays
# * Keras simplifies neural network creation
# * Adam optimizer is commonly used

# ---

