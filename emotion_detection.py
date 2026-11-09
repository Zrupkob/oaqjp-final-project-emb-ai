''' This module contains the emotion_detector function
    for analyzing emotions in a given input text.
'''

# Import the requests library to handle HTTP requests
import requests

# Define a function named emotion_detector that takes a string input (text_to_analyze)
def emotion_detector(text_to_analyze):
    ''' This code sends a myobj dictionary with an input text
        to the emotion detector model defined in url and header,
        then handles the response.
    '''
    # URL of the emotion detector service
    url = ('https://sn-watson-emotion.labs.skills.network/'
    'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header, timeout=5000)

    # Return the response text
    return response.text