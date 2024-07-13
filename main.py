# run the main.py file

from speech import run
from blindhelp.conversion.textToSpeech import text_to_speech


text_to_speech('Welcome to your AI assistant. Starting the application')

run()


# import anyio
# from speech import run
# from blindhelp.conversion.textToSpeech import text_to_speech

# async def text_to_speech_async(text):
#     # Run the synchronous function in a thread
#     await anyio.to_thread.run_sync(text_to_speech, text)

# async def main():
#     # Wait for text_to_speech to complete
#     await text_to_speech_async('Welcome to your AI assistant. Starting the application')
#     # Call run() after text_to_speech is done
#     run()

# # Run the main function
# anyio.run(main)
