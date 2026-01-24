import tensorflow as tf
from tensorflow.keras import layers

def build_functional(input_shape = (150, 150, 3), num_classes=6, learning_rate=1e-3):
    norm_layer = layers.Normalization()
    hidden_layer1 = layers.Dense(64, activation='relu')
    hidden_layer2 = layers.Dense(64, activation='relu')
    concat_layer = layers.Concatenate()
    hidden_layer3 = layers.Dense(32, activation='relu')
    output_layer = layers.Dense(num_classes, activation='softmax')

    input_ = layers.Input(shape=input_shape)
    normalized = norm_layer(input_)
    hidden1 = hidden_layer1(normalized)
    hidden2 = hidden_layer2(hidden1)
    concat = concat_layer([hidden2, normalized])
    hidden3 = hidden_layer3(concat)
    output = output_layer(hidden3)

    model = tf.keras.Model(inputs=[input_], outputs=output)
    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)

    model.compile(
        optimizer=optimizer,
        loss='SparseCategoricalCrossentropy',
        metrics=['accuracy']
    )

    return model, norm_layer

