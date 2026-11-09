''' This module contains the emotion_detector function
    for analyzing emotions in a given input text.
'''

# Import the json library to format the response
import json
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

    # If the response status code is 400, send back None values
    if response.status_code == 400:
        result = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }
        return result

    # Parse the response from the API
    formatted_response = json.loads(response.text)
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    dominant_emotion = max(formatted_response['emotionPredictions'][0]['emotion'], key=formatted_response['emotionPredictions'][0]['emotion'].get)

    # Returning a dictionary containing emotion analysis results
    result = {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion
    }
    return result