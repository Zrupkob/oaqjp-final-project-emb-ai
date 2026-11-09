''' Executing this function initiates the application of emotion detection
    to be executed over the Flask channel and deployed on localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using the emotion_detector()
        function. The output returned shows the emotions and their confidence 
        score for the provided text, along with the dominant emotion.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the values from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if the dominant_emotion is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with the scores and dominant emotion
    answer = f"For the given statement, the system response is " \
    f"'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, " \
    f"'joy': {joy_score} and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
    return answer

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    #This function executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)