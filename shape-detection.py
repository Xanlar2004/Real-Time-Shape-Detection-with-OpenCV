import cv2
import numpy as np

# Set the dimensions for the video frame
frame_width = 640
frame_height = 480

# Capture video from the default camera
video_capture = cv2.VideoCapture(0)
video_capture.set(3, frame_width)
video_capture.set(4, frame_height)

# Placeholder function for trackbars
def trackbar_placeholder(value):
    pass

# Create a window for parameters and trackbars
cv2.namedWindow("Control Panel")
cv2.resizeWindow("Control Panel", frame_width, frame_height // 2)
cv2.createTrackbar("Threshold1", "Control Panel", 23, 255, trackbar_placeholder)
cv2.createTrackbar("Threshold2", "Control Panel", 20, 255, trackbar_placeholder)
cv2.createTrackbar("Minimum Area", "Control Panel", 5000, 30000, trackbar_placeholder)

def combine_images(scale, images):
    rows = len(images)
    cols = len(images[0])
    has_multiple_rows = isinstance(images[0], list)
    width = images[0][0].shape[1]
    height = images[0][0].shape[0]

    if has_multiple_rows:
        for i in range(rows):
            for j in range(cols):
                if images[i][j].shape[:2] == images[0][0].shape[:2]:
                    images[i][j] = cv2.resize(images[i][j], (0, 0), None, scale, scale)
                else:
                    images[i][j] = cv2.resize(images[i][j], (images[0][0].shape[1], images[0][0].shape[0]), None, scale, scale)
                if len(images[i][j].shape) == 2:
                    images[i][j] = cv2.cvtColor(images[i][j], cv2.COLOR_GRAY2BGR)
        
        blank_image = np.zeros((height, width, 3), np.uint8)
        horizontal_images = [blank_image] * rows
        for i in range(rows):
            horizontal_images[i] = np.hstack(images[i])
        final_image = np.vstack(horizontal_images)
    else:
        for i in range(rows):
            if images[i].shape[:2] == images[0].shape[:2]:
                images[i] = cv2.resize(images[i], (0, 0), None, scale, scale)
            else:
                images[i] = cv2.resize(images[i], (images[0].shape[1], images[0].shape[0]), None, scale, scale)
            if len(images[i].shape) == 2:
                images[i] = cv2.cvtColor(images[i], cv2.COLOR_GRAY2BGR)
        
        final_image = np.hstack(images)

    return final_image

def find_contours(input_image, output_image):
    contours, _ = cv2.findContours(input_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        min_area = cv2.getTrackbarPos("Minimum Area", "Control Panel")
        if area > min_area:
            cv2.drawContours(output_image, contour, -1, (255, 0, 255), 7)
            perimeter = cv2.arcLength(contour, True)
            approx_shape = cv2.approxPolyDP(contour, perimeter * 0.02, True)
            x, y, width, height = cv2.boundingRect(approx_shape)
            cv2.rectangle(output_image, (x, y), (x + width, y + height), (0, 255, 0), 5)
            cv2.putText(output_image, f"Points: {len(approx_shape)}", (x + width + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(output_image, f"Area: {int(area)}", (x + width + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)

# Main loop for processing video frames
while True:
    success, frame = video_capture.read()
    contour_frame = frame.copy()
    blurred_frame = cv2.GaussianBlur(frame, (7, 7), 1)
    gray_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2GRAY)
    
    # Get threshold values from trackbars
    threshold1 = cv2.getTrackbarPos("Threshold1", "Control Panel")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Control Panel")
    
    # Edge detection using Canny
    edge_frame = cv2.Canny(gray_frame, threshold1, threshold2)
    
    # Dilate the edges to strengthen them
    kernel = np.ones((5, 5))
    dilated_frame = cv2.dilate(edge_frame, kernel, iterations=1)
    
    # Find and draw contours
    find_contours(dilated_frame, contour_frame)
    
    # Stack images for display
    stacked_images = combine_images(0.8, ([frame, edge_frame], [dilated_frame, contour_frame]))
    
    # Show the result in a window
    cv2.imshow("Output", stacked_images)
    
    # Exit the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_capture.release()
cv2.destroyAllWindows()
