import cv2

def main():
    # Open a connection to the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    frame_count = 0

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            break

        # Increment the frame count
        frame_count += 1

        # Print the frame number to the terminal
        print(f"Frame number: {frame_count}")

        # Put the frame number text on the frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f"Frame: {frame_count}"
        org = (frame.shape[1] - 150, 30)  # Top right corner with some padding
        font_scale = 1
        color = (255, 0, 0)  # Blue color in BGR
        thickness = 2

        frame = cv2.putText(frame, text, org, font, font_scale, color, thickness, cv2.LINE_AA)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


