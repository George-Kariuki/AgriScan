import os
import numpy as np
import tensorflow as tf

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
MODEL_PATH = os.path.join(BASE_DIR, "models", "cassava.tflite")

class TFLiteModel:
    def __init__(self, model_path=MODEL_PATH):
        # load tflite model via full TF interpreter
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self._input_details = self.interpreter.get_input_details()
        self._output_details = self.interpreter.get_output_details()

    def predict(self, img_array: np.ndarray):
        """
        img_array: numpy array shaped [H, W, C] float32 normalized to [0,1]
        """
        # resize/check shape as required by model input
        input_index = self._input_details[0]['index']

        # if model expects shape (1,224,224,3)
        if len(self._input_details[0]['shape']) == 4:
            # ensure batch dimension
            if img_array.ndim == 3:
                input_data = np.expand_dims(img_array, axis=0).astype(np.float32)
            else:
                input_data = img_array.astype(np.float32)
        else:
            input_data = img_array.astype(np.float32)

        # set tensor and invoke
        self.interpreter.set_tensor(input_index, input_data)
        self.interpreter.invoke()
        output = self.interpreter.get_tensor(self._output_details[0]['index'])

        return output  # raw logits / probabilities
