import tensorflow as tf
from tensorflow.keras import layers

def build_mlp(input_shape=(150, 150, 3), num_classes=6, learning_rate=1e-3):
    norm_layer = layers.Normalization(input_shape=input_shape)    
    model = tf.keras.Sequential([
        norm_layer,
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])

    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    model.compile(
        optimizer=optimizer, 
        loss='SparseCategoricalCrossentropy', 
        metrics=['accuracy']
    )

    return model, norm_layer
    