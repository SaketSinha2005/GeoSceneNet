import tensorflow as tf
from tensorflow.keras import layers

def build_functional(input_shape = (150, 150, 3), num_classes=6, learning_rate=1e-3):
    input_ = layers.Input(shape=input_shape)
    norm_layer = layers.Normalization()
    x = norm_layer(input_)

    flatten = layers.Flatten()(x)
    hidden_layer1 = layers.Dense(64, activation='relu')(flatten)
    hidden_layer2 = layers.Dense(64, activation='relu')(hidden_layer1)
    concat_layer = layers.Concatenate()([hidden_layer2, flatten])
    hidden_layer3 = layers.Dense(32, activation='relu')(concat_layer)
    output_layer = layers.Dense(num_classes, activation='softmax')(hidden_layer3)

    model = tf.keras.Model(inputs=[input_], outputs=output_layer)
    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)

    model.compile(
        optimizer=optimizer,
        loss='SparseCategoricalCrossentropy',
        metrics=['accuracy']
    )

    return model, norm_layer

