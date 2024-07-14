# blindHelp
## Empowering the Blind: Navigate Your World with Confidence

### What it does?
This project is designed to assist visually impaired individuals by providing real-time audio descriptions of their surroundings and guiding them to specific indoor destinations.
The two features of this project are:
- Blind Assist : Empowering Vision through Voice. Blind Assist helps visually impaired individuals understand their surroundings by providing audio descriptions of the environment, enhancing their awareness and independence.
  About this feature:
  - Video Processing: Uses a camera to capture real-time video of the surroundings.
  - Object Detection and Description: Utilizes the Gemini Vision model to identify and describe objects in the environment.
  - Speech Feedback: Converts the description of the surroundings into speech, helping visually impaired users understand their environment.
  - Voice Queries: Allows users to ask questions about their surroundings, such as "Is there a table in the room?" or "Read the text on the box," and provides spoken answers.
 - Map Assist: Guiding You Indoors with Confidence. Map Assist aids visually impaired individuals in navigating indoor spaces by providing real-time audio guidance, ensuring they reach their destinations safely and efficiently.
   About this feature:
   - Indoor Navigation: Helps users navigate from one point to another within a building using a map of the room.
   - Pathfinding: The Gemini Vision model finds the best path to the destination.
   - Real-time Guidance: Combines map data and real-time video analysis to guide users, providing spoken instructions to reach their destination.

### Technologies used
- Gemini Vision Models: For object detection and environment description.
- OpenCV: For video frame processing.
- Google Text-to-Speech (TTS): To convert text descriptions into spoken words.
- Google Speech-to-Text (STT): To convert spoken queries from users into text for processing.
- Django and React: For building the web application interface.
- Gemini Flash: For generating text responses.
  
### Quick start
To start the project:
 Make you of camo app
 or give the videostream index as 0 in videoCapture of opencv
 After installing all the required libraries, run the command <br>
 run `cd blindhelp/` <br>
  `python main.py`
