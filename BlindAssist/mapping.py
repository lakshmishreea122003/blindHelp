import cv2
import time
import google.generativeai as genai
import os
from .textToSpeech import text_to_speech
from .speech import getQuery

class IAnalysis:
    def __init__(self):
        GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
        genai.configure(api_key=GOOGLE_API_KEY)
    def g_vision(self, image,map_description,query):
        temp_path = "temp_image.jpg"
        cv2.imwrite(temp_path, image)
        # Upload the temporary file
        sample_file = genai.upload_file(path=temp_path, display_name="image")
        print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")
        file = genai.get_file(name=sample_file.name)
        print(f"Retrieved file '{file.display_name}' as: {sample_file.uri}")
        # Analyze the image using the Gemini model
        model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
        response = model.generate_content([sample_file, "Your task is to guide blind person. What can be seen in the image? Describe what ever can be seen in the image in such a way that you are providing information about the surroundings to help in independent mobility of the blind person. "])
        res_guide = self.gemini_guide_map(response,map_description,query) 
        return res_guide
    
    def gemini_guide_map(self,description,map_description, query):
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"You are an assistive guide for a blind person. Here is the rough description of the room where the blind person is: {map_description}  Based on the following description of their surroundings: '{description}', provide clear, concise, and actionable guidance to help the person navigate safely. Also answer to the query {query} of the person(If query is empty string ignore query). Highlight any potential dangers or obstacles, and offer general directions or advice. Use simple and easy-to-understand language. Keep your responses short and mention only important aspects that has to be considered in real time by person. This response text will be converted to speech for each video frame so keep responses short, that should help in independent mobility of the blind person. In the responses it should be plain text with no markdown format. Keep the response short. Do not include special charaters like *,@,# or any such charactes it should be a plain text only. "
        res = model.generate_content(prompt).text
        
        return res

    def g_map(self,file_path):
        sample_file = genai.upload_file(path=file_path, display_name="image")
        print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")
        file = genai.get_file(name=sample_file.name)
        print(f"Retrieved file '{file.display_name}' as: {sample_file.uri}")
        model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
        response = model.generate_content([sample_file, "I have provided you a brief map of a room.What can be seen in the image? Describe the image. Give me a guide as to how person can reach the door if the he is at table2."])
        return response.text

     
    
    
def get_directions_map(image,query):
    # Get description from Gemini model
    analyzer = IAnalysis()
    map_description = 'The room is rectangular with a door located in the top right corner. As you enter from the door, you will find a whiteboard on the wall to your immediate right. Two tables are positioned horizontally in the room. Table 1 is closer to the whiteboard and the left side of the room, while Table 2 is slightly to the right of Table 1, closer to the center. Chairs are aligned along both sides of these tables, providing seating. The room features four windows: Window 1 is on the top left side near the whiteboard, Window 2 is on the left side near the middle, Window 3 is on the bottom left side, and Window 4 is on the right side near the middle.'
    description = analyzer.g_vision(image,map_description,query)
    return description

def map_main():
    # Open a connection to the webcam
    text_to_speech('Running the map application')
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    frame_count = 0

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1
        query = ""

        # Process every alternate frame (or you can change the condition as needed)
        if frame_count % 2 == 0:
            # Get description from Gemini model
            query = getQuery()
            description = get_directions_map(frame,query)
            

            # Print the description to the terminal
            print(f"Frame {frame_count}: {description}")
            text_to_speech(description)

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

