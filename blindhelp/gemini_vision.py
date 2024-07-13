import cv2
import time
import google.generativeai as genai
import os
from textToSpeech import text_to_speech
class IAnalysis:
    def __init__(self):
        GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
        genai.configure(api_key=GOOGLE_API_KEY)
    def g_vision(self, image,query):
        temp_path = "temp_image.jpg"
        cv2.imwrite(temp_path, image)
        # Upload the temporary file
        sample_file = genai.upload_file(path=temp_path, display_name="image")
        print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")
        file = genai.get_file(name=sample_file.name)
        print(f"Retrieved file '{file.display_name}' as: {sample_file.uri}")
        # Analyze the image using the Gemini model
        model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
        response = model.generate_content([sample_file, "Your task is to guide blind person. What can be seen in the image? Describe what ever can be seen in the image in such a way that you are providing information about the surrounding to help in independent mobility of the blind person. "])
        res_guide = self.gemini_guide(response,query) 
        return res_guide
    def gemini_guide(self,description,query):
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"You are an assistive guide for a blind person. Based on the following description of their surroundings: '{description}', provide clear, concise, and actionable guidance to help the person navigate safely. Also answer to the query {query} of the person(If query is empty string ignore query). Highlight any potential dangers or obstacles, and offer general directions or advice. Use simple and easy-to-understand language. Keep your responses short and mention only important aspects that has to be considered in real time by person. This response text will be converted to speech for each video frame so keep responses short, that should help in independent mobility of the blind person."
        res = model.generate_content(prompt).text
        return res
    # def g_query(self,query):
    
    
def get_description_from_gemini(image,query):
    # Get description from Gemini model
    analyzer = IAnalysis()
    description = analyzer.g_vision(image,query)
    return description

def main():
    # Open a connection to the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video stream.")
        text_to_speech('Error: Could not open video stream.')
        return

    frame_count = 0

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1

        # Process every alternate frame (or you can change the condition as needed)
        if frame_count % 2 == 0:
            query=""
            # Get description from Gemini model
            description = get_description_from_gemini(frame, query)

            # Print the description to the terminal
            print(f"Frame {frame_count}: {description}")

            # Put the description text on the frame
            font = cv2.FONT_HERSHEY_SIMPLEX
            text = description
            org = (10, 30)  # Top left corner with some padding
            font_scale = 1
            color = (255, 0, 0)  # Blue color in BGR
            thickness = 2

            frame = cv2.putText(frame, text, org, font, font_scale, color, thickness, cv2.LINE_AA)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Add a delay to reduce the number of API calls (optional)
        time.sleep(0.5)  # Adjust the delay as needed

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

main()
