import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

# Load the gesture prediction model
model_path = 'C:\\Users\\FLEX\\SIH\\gesture_immotion\\harassment_detection_model.h5'  
gesture_model = load_model(model_path)

def preprocess_for_gesture(face_roi):
    # Resize the face ROI to (224, 224) exactly as required by the model
    resized_face = cv2.resize(face_roi, (224, 224), interpolation=cv2.INTER_AREA)  # Exact resizing
    img_array = img_to_array(resized_face)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the image
    return img_array

def predict_gesture(face_roi):
    # Preprocess the face ROI for gesture model prediction
    img_array = preprocess_for_gesture(face_roi)
    prediction = gesture_model.predict(img_array)
    
    # Interpret the result (Assuming binary classification: 0 = Unwanted, 1 = Wanted)
    if prediction[0] > 0.5:
        return 'Wanted (Normal)'
    else:
        return 'Unwanted (Harassed)'

# The gesture module processes the ROI from the emotion module
