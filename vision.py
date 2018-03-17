import requests

def getContext(URL):
    subscription_key = "9c48293c67a548a1b1458fd4d85f6f91"
    vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
    vision_analyze_url = vision_base_url + "analyze"
    image_url = URL
    headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    params = {'visualFeatures': 'Categories,Description,Color'}
    data = {'url': image_url}
    response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
    response.raise_for_status()
    analysis = response.json()
    image_caption = analysis["description"]["captions"][0]["text"].capitalize()
    print(image_caption)
    return analysis

def tagList(jsonDict):
    return jsonDict['description']['tags']

def threatLevel(tags):
    occurences = 0
    myThreatDict = ['weapon', 'gun', 'fire', 'holding', 'running', 'bomb', 'kill', 'threat', 'martyrdom' 'martyr']
    for i in myThreatDict:
        if i in tags:
            occurences = occurences + 1
    return occurences

print(getContext("https://s3.amazonaws.com/extremekarate/wp-content/uploads/2015/09/24161936/street-fight3.jpg"))
print(tagList(getContext("https://s3.amazonaws.com/extremekarate/wp-content/uploads/2015/09/24161936/street-fight3.jpg")))