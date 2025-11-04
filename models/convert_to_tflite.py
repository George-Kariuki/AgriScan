import tensorflow as tf
import os

MODEL_H5_PATH = os.path.join(os.path.dirname(__file__), "cassava_model.h5")
TFLITE_OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "cassava.tflite")

def convert_h5_to_tflite():
    if not os.path.exists(MODEL_H5_PATH):
        raise FileNotFoundError(f"Model file not found: {MODEL_H5_PATH}")
    
    print(f"Loading model from {MODEL_H5_PATH}...")
    model = tf.keras.models.load_model(MODEL_H5_PATH)
    
    print("Converting to TensorFlow Lite format...")
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()
    
    print(f"Saving TensorFlow Lite model to {TFLITE_OUTPUT_PATH}...")
    with open(TFLITE_OUTPUT_PATH, 'wb') as f:
        f.write(tflite_model)
    
    file_size = os.path.getsize(TFLITE_OUTPUT_PATH) / (1024 * 1024)
    print(f"✓ Conversion complete! Model size: {file_size:.2f} MB")

if __name__ == "__main__":
    try:
        convert_h5_to_tflite()
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

