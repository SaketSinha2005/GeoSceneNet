# GeoSceneNet

This to-do list is designed to practice **Chapters 10 and 11 of *Hands-On Machine Learning*** using the **Intel Image Classification dataset**.  
The focus is on learning how to **build, train, and evaluate neural networks with Keras** (Chapter 10) and understanding **how to train deep networks effectively** using proper initialization, regularization, normalization, and optimization techniques (Chapter 11).

You will start with a simple baseline neural network and gradually move to a small custom CNN, observing how different training choices affect performance and stability.  
The goal is **conceptual understanding and hands-on experience**, not achieving state-of-the-art accuracy.
---

## To-Do List  
## Hands-On Machine Learning — Chapters 10 & 11  
## Intel Image Classification (Simple Custom NN / CNN)

---

## 🔹 Phase 1 — Chapter 10: Introduction to ANN with Keras

### 1 Dataset ingestion (Keras-style)
- [ ] Load Intel dataset using `image_dataset_from_directory`
- [ ] Set `image_size` and `batch_size`
- [ ] Inspect class names and batch shapes

---

### 2 First working Keras model (baseline MLP)
- [ ] Build model using **Sequential API**
- [ ] Layers:
  - `Flatten`
  - `Dense(128, activation="relu")`
  - `Dense(6, activation="softmax")`
- [ ] Compile with:
  - `SparseCategoricalCrossentropy`
  - `Adam`
  - `accuracy`

---

### 3️ Train, evaluate, and save the model
- [ ] Train model using `model.fit`
- [ ] Validate during training
- [ ] Evaluate on test set
- [ ] Save model using `model.save`
- [ ] Reload the model and re-evaluate

---

### 4️ Functional API practice
- [ ] Rebuild the same model using the **Functional API**
- [ ] Verify similar performance to Sequential model

---

### 5️ Customization basics (light)
- [ ] Try a different optimizer or loss function
- [ ] (Optional) Add a simple custom metric

---

## 🔹 Phase 2 — Chapter 11: Training Deep Neural Networks

### 6️ Simple CNN (custom, from scratch)
- [ ] Replace MLP with a small CNN:
  - `Conv2D → ReLU → MaxPooling`
  - Repeat 2–3 times
  - `Flatten → Dense → Softmax`
- [ ] Train and evaluate the CNN

---

### 7️ Initialization & activation experiments
- [ ] Compare default initialization vs **He initialization**
- [ ] Try different activations:
  - `ReLU`
  - `LeakyReLU`

---

### 8️ Regularization techniques
- [ ] Add **Dropout**
- [ ] Add **L2 weight regularization**
- [ ] Compare training vs validation curves

---

### 9️ Batch Normalization
- [ ] Insert `BatchNormalization` layers
- [ ] Observe training speed and stability changes

---

### 10 Optimizers & learning rate tuning
- [ ] Compare **SGD** vs **Adam**
- [ ] Add `ReduceLROnPlateau` callback
- [ ] Plot learning curves (loss vs epochs)

---

## 🔹 Phase 3 — Training Control & Evaluation

### 1️1 Early stopping
- [ ] Add `EarlyStopping` with best-weight restoration
- [ ] Observe effect on overfitting

---

### 1️2 Final comparison & reflection
- [ ] Compare:
  - MLP vs CNN
  - With vs without regularization
- [ ] Write brief notes:
  - What stabilized training?
  - What caused overfitting?

---

## Goal
By completing this checklist, one will:
- Understand **Keras basics** (Chapter 10)
- Learn how to **stabilize and train deep networks** (Chapter 11)
- Build and analyze a **simple custom CNN** for image classification