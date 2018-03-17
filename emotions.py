import requests

def make_call(URL):
    subscription_key = "c695019b3cca4918b540fc688b7ec516"
    face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
    image_url = URL
    headers = {'Ocp-Apim-Subscription-Key': 'c695019b3cca4918b540fc688b7ec516'}

    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'emotion',
    }

    response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})
    faces = response.json()
    return faces


print(make_call("https://how-old.net/Images/faces2/main007.jpg"))