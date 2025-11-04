import tensorflow as tf
import os

MODEL_H5_PATH = os.path.join(os.path.dirname(__file__), "cassava_model.h5")

def create_dummy_model():
    print("Creating a dummy Cassava Leaf Disease Classification model...")
    print("Note: This is a placeholder. Replace with your trained model for production.")
    
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(224, 224, 3)),
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(5, activation='softmax')
    ])
    
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print(f"Saving model to {MODEL_H5_PATH}...")
    model.save(MODEL_H5_PATH)
    print(f"✓ Dummy model created at {MODEL_H5_PATH}")
    print("You can now run: python models/convert_to_tflite.py")

if __name__ == "__main__":
    try:
        create_dummy_model()
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

