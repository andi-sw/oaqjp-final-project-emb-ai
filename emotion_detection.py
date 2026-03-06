import requests
import json

def emotion_detector(text_to_analyze):
    """Function that detects emotions from input text
    """
    url     = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header  = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj   = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = myobj, headers = header)

    formatted_response = json.loads(response.text)

    anger_score     = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score   = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score      = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score       = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score   = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    max_score = -10
    dominant_emotion = None
    for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness']:
        if formatted_response['emotionPredictions'][0]['emotion'][emotion] > max_score:
            max_score = formatted_response['emotionPredictions'][0]['emotion'][emotion]
            dominant_emotion = emotion

    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }