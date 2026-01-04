import tensorflow as tf 

def load_dataset(
	data_dir,
	img_size = (150, 150),
	seed = 42,
	batch_size = 32,
	validation_split=0.2
):
	train_df = tf.keras.utils.image_dataset_from_directory(
		data_dir,
		validation_split=validation_split,
		seed=seed,
		subset="training",
		batch_size=batch_size,
		image_size=img_size,
		label_mode = "int"
	)

	val_df = tf.keras.utils.image_dataset_from_directory(
		data_dir,
		validation_split=validation_split,
		seed=seed,
		subset="validation",
		batch_size=batch_size,	
		image_size=img_size,
		label_mode = "int"
	)
	class_names = train_df.class_names

	AUTOTUNE = tf.data.AUTOTUNE

	train_ds = train_df.cache().shuffle(1000).prefetch(AUTOTUNE)
	val_ds = val_df.cache().prefetch(AUTOTUNE)
    

	return train_ds, val_ds, class_names