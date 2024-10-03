# UnwantedGesture-Prediction-Women-safety-
Women Safety Analytics
Background
The growing concern for the safety of women and the increase in crimes against women in various cities highlight the need for advanced surveillance and analytical solutions to protect women from various possible threats. This project aims to address these issues through real-time threat detection software.

Detailed Description

Women Safety Analytics leverages advanced analytics through real-time monitoring to create safer environments for women and assist law enforcement in effectively addressing and preventing crimes against women. The proactive approach of detecting anomalies and generating alerts can play a crucial role in enhancing public safety and fostering a secure atmosphere for women.

Key Features:

Person Detection with Gender Classification: Detect and classify the gender of individuals in the scene using YOLOv8.
Gender Distribution: Count the number of men and women present in the scene in real-time.
Identifying a Lone Woman at Night: Detect scenarios where a lone woman is present during nighttime.
Detection of a Woman Surrounded by Men: Identify situations where a woman is surrounded by men.
Recognizing SOS Situations through Gesture and Emotion Analytics: Analyze gestures and emotions to detect SOS signals using VGG16 and DeepFace.
Identifying Hotspots: Determine locations where incidents are more likely to occur based on past alerts.
Advantages:

Real-time Monitoring and Alerts: 
Helps create a safer environment for women by providing real-time monitoring and alerts.
Early Detection:
Enables law enforcement to intervene before situations escalate.
Continuous Analysis: 
Provides valuable data to identify hotspots and trends, aiding in strategic planning for city safety.
Expected Solution
Women Safety Analytics should include the following functionalities:

Person Detection along with Gender Classification: Using YOLOv8.
Gender Distribution: Count the number of men and women present in the scene.
Identifying a Lone Woman at Night
Detection of a Woman Surrounded by Men
Recognizing SOS Situations through Gesture and Emotion Analytics: Using VGG16 and DeepFace.
Identifying Hotspots: Based on past alerts.
Tech Stack
Programming Language: Python
Libraries:
OpenCV: For real-time image processing and computer vision tasks.
NumPy: For numerical operations and array manipulations.
Deep Learning Frameworks:
YOLOv8: For person detection and gender classification.
VGG16: For gesture recognition.
DeepFace: For emotion detection.
Tools:
argparse: For command-line argument parsing to enable flexible execution of the software.
Pre-trained Models: The system uses pre-trained models for face detection to reduce development time and increase accuracy.
and Here is Sample result-
![Alt text](https://github.com/Tanuja7897/UnwantedGesture-Prediction-Women-safety-/blob/main/result.jpg)

