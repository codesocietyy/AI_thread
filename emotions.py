import requests

subscription_key = "c695019b3cca4918b540fc688b7ec516"
face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
image_url = 'https://how-old.net/Images/faces2/main007.jpg'
headers = { 'Ocp-Apim-Subscription-Key': 'c695019b3cca4918b540fc688b7ec516' }

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion',
}

response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})
faces = response.json()
print(faces)
