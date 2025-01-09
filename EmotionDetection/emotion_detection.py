import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyze} }

    response = requests.post(url, json = myobj, headers=header)

    formatted_response = response.json()

    emotions_data = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions_data, key=emotions_data.get)

    return {
    'anger_score'  : emotions_data['anger'],
    'disgust_score' : emotions_data['disgust'],
    'fear_score' : emotions_data['fear'],
    'joy_score' : emotions_data['joy'],
    'sadness_score' : emotions_data['sadness'],
    'dominant_emotion' : dominant_emotion
    }

