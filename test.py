import cv2
from deepface import DeepFace
from gesture import predict_gesture  # Import your gesture prediction function

# Define the analyze_frame function
def analyze_frame(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = DeepFace.analyze(frame_rgb, actions=['emotion'], enforce_detection=False)
    emotion = result[0]['dominant_emotion']
    gesture_output = predict_gesture(frame_rgb)
    results = {
        "emotion": emotion,
        "gesture": gesture_output
    }
    return results

# Define wanted emotions and gesture states
wanted_emotions = ['happy', 'excited', 'surprise', 'neutral']
wanted_gesture = 'Wanted'
unwanted_gesture = 'Unwanted'

def determine_final_output(emotion, gesture):
    if gesture == wanted_gesture:
        if emotion in wanted_emotions:
            return "Wanted"
        else:
            return "Wanted"
    else:  # gesture == unwanted_gesture
        if emotion in wanted_emotions:
            return "Wanted"
        else:
            return "Unwanted"

# Load the YOLO model for both gender detection and tracking
from ultralytics import YOLO

model = YOLO("C:\\Users\\FLEX\\SIH\\gesture_immotion\\best (1).pt")  # Path to your YOLO model

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        
        for result in results:
            boxes = result.boxes
            for box in boxes:
                gender = box.cls[0]

                if gender == 1:  # Check if the detected gender is female
                    print("Female detected. Running emotion and gesture detection...")

                    emotion_gesture_results = analyze_frame(frame)

                    if emotion_gesture_results:
                        emotion = emotion_gesture_results['emotion']
                        gesture = emotion_gesture_results['gesture']

                        final_output = determine_final_output(emotion, gesture)

                        # Display gender, emotion, gesture, and final output on the frame
                        cv2.putText(frame, f"Gender: Female", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        cv2.putText(frame, f"Emotion: {emotion}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        cv2.putText(frame, f"Gesture: {gesture}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        cv2.putText(frame, f"Result: {final_output}", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:
                    # If gender is not female, just display that no female is detected
                    cv2.putText(frame, "No Female Detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow('Gender, Emotion, and Gesture Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
