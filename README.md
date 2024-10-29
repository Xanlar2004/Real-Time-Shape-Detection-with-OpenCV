<!DOCTYPE html>
<html>

<head>
  <h1>Real-Time Shape Detection with OpenCV</h1>
</head>

<body>
  <h2>Introduction</h2>
  <p>This project implements a real-time shape detection system in Python using OpenCV. It captures live video feed, identifies shapes like rectangles, triangles, and circles, and displays them       on the screen. Real-time shape recognition is highly useful in robotics, AR applications, and industries utilizing drones for object detection and interaction. Here are the features:<br>
     1. Real-time Detection: Detects and tracks shapes in live video.<br>
     2. Dynamic Parameters: Allows real-time adjustment of edge detection thresholds and contour area.<br>
     3. Image Stacking: Uses an image stacking function to arrange multiple frames for display.<br></p>
  
  <h2>Requirements</h2>
  <p>Python Libraries:<br>
     Numpy: For numerical computation.<br>
     cv2 (OpenCV): For image processing and shape recognition.<br></p>

  <h2>Installation</h2>
  <p>To set up the environment:<br>
     - Download and install Visual Studio Code (or your preferred IDE).<br>
     - Ensure Python is installed.<br>
     - Install required packages: <code>pip install numpy opencv-python</code><br>
     - Open Visual Studio Code or any preferred IDE and create a file named <code>shape-detection.py</code>.<br>
     - Run the application.<br></p>
     
      
  <h2>Code Explanation</h2>
  <p>This Python script enables real-time shape detection through webcam input. Here is a breakdown of the code:<br>
     1. Imports: Import required libraries (OpenCV for computer vision and NumPy for array handling).<br>
     2. Webcam Initialization: Set up video capture using <code>cv2.VideoCapture(0)</code> and adjust frame width and height.<br>
     3. Trackbar Setup: Create adjustable trackbars to set edge detection thresholds and minimum contour area dynamically.<br>
     4. Contour Detection: Identify contours, approximate their shape, and draw bounding boxes on the detected shapes.<br>
     5. Image Stacking: Stack the original, mask, and final images horizontally for display, allowing for easy shape analysis.<br>
     6. Main Loop: Capture and process frames continuously, using edge detection, contour finding, and drawing functions for real-time detection.<br>
     7. Exit Condition: Press 'q' to exit the program and release resources.<br></p>

</body>

</html>
