import requests
import json

def emotion_detector(text_to_analyze):
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(URL, json=input_json, headers = header)

    if response.status_code == 200:
        detect_dict = json.loads(response.text)

        detect_emotions = detect_dict["emotionPredictions"][0]["emotion"]

        high_emotion = max(detect_emotions, key = detect_emotions.get)

        anger = detect_emotions["anger"]

        disgust = detect_emotions["disgust"]

        fear = detect_emotions["fear"]

        joy = detect_emotions["joy"]

        sadness = detect_emotions["sadness"]

        formatted_dict_emotions = {
            'anger': anger,

            'disgust': disgust,

            'fear': fear,

            'joy': joy,

            'sadness': sadness,

            'dominant emotion': high_emotion
            }

        return formatted_dict_emotions
    
    else:
        print("There was an error. The error code:", response.status_code)
        print("Response body:", response.text)
        