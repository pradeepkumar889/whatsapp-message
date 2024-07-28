import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
def apply_filter():
    def apply_filter(img, filter_type):
        if filter_type == 0:
            # No filter
            return img
        elif filter_type == 1:
            # Grayscale filter
            return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        elif filter_type == 2:
            # Sepia filter
            kernel = np.array([[0.272, 0.534, 0.131],
                            [0.349, 0.686, 0.168],
                            [0.393, 0.769, 0.189]])
            return cv2.transform(img, kernel)
        elif filter_type == 3:
            # Negative filter
            return cv2.bitwise_not(img)
        elif filter_type == 4:
            # Gaussian blur filter
            return cv2.GaussianBlur(img, (15, 15), 0)
        elif filter_type == 5:
            # Canny edge detection
            return cv2.Canny(img, 100, 200)
        else:
            # Default to no filter
            return img

    def main():
        # Initialize the webcam
        cap = cv2.VideoCapture(0)

        # Initialize the HandDetector
        detector = HandDetector(staticMode=False, maxHands=1, detectionCon=0.8, minTrackCon=0.5)

    # Variable to keep track of the previous number of fingers
        prev_fingers = -1

        while True:
        # Capture frame from the webcam
            success, img = cap.read()
        
            if not success:
                break
        
        # Detect hands in the frame
            hands, img = detector.findHands(img, draw=True)
        
            if hands:
                # Get the first hand detected
                hand = hands[0]
            
            # Get the number of fingers up
                fingers = detector.fingersUp(hand).count(1)
            
                # Apply filter if the number of fingers changes
                if fingers != prev_fingers:
                    prev_fingers = fingers
                    print(f'Number of fingers: {fingers}')
        
            # Apply the filter to the image
            filtered_img = apply_filter(img, prev_fingers)
        
        # Display the image
            cv2.imshow("Image", filtered_img)
        
        # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Release the webcam and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

    if __name__ == "__main__":
        main()
apply_filter()