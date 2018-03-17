import requests
import json

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
    jsonFaces = json.loads(response.text)
    return jsonFaces

def processJson(jsonInput):
    emotions = jsonInput[0]['faceAttributes']['emotion']

    anger = emotions['anger']
    fear = emotions['fear']
    contempt = emotions['contempt']
    happiness = emotions['happiness']
    surprise = emotions['surprise']
    disgust = emotions['disgust']
    sadness = emotions['sadness']
    neutral = emotions['neutral']



    return anger

urls = [
'https://irisscuprodstore.blob.core.windows.net/i-4d277707a9574e1b8854f4fb417f24fd/i-3b555c0aa6554169b226b2dc92ba9869?sv=2017-04-17&sr=b&sig=jWYkYU5y%2FhlRf4uL21JrYWZtLdIIxpLmR2q00jl8J1g%3D&se=2018-03-18T00%3A00%3A00Z&sp=r'
    , 'https://irisscuprodstore.blob.core.windows.net/i-4d277707a9574e1b8854f4fb417f24fd/i-8013991b0f7040e2ba2fd8e4edc91a35?sv=2017-04-17&sr=b&sig=ERTfqH7opZlCb%2BPXLe%2Be8pG%2BrlHhh7luxgz3FPOMajs%3D&se=2018-03-18T00%3A00%3A00Z&sp=r'
    , 'https://irisscuprodstore.blob.core.windows.net/i-4d277707a9574e1b8854f4fb417f24fd/i-fd731e5fa4cd4beab26e40e802b66deb?sv=2017-04-17&sr=b&sig=Iwnt1qEaxBswQioR7kP7OiPi61pao%2BIq6UCogTVP2qI%3D&se=2018-03-18T00%3A00%3A00Z&sp=r'
    , 'https://irisscuprodstore.blob.core.windows.net/i-4d277707a9574e1b8854f4fb417f24fd/i-09ad2a70ee1943ca9ab0d2710271d765?sv=2017-04-17&sr=b&sig=FHl1zJO9y2D7UHcMwdNj8lZCcrks%2BHfX35xrDzB%2FqM4%3D&se=2018-03-18T00%3A00%3A00Z&sp=r'
    , 'https://irisscuprodstore.blob.core.windows.net/i-4d277707a9574e1b8854f4fb417f24fd/i-8ea60bcd71d44c8abfdc14209607b971?sv=2017-04-17&sr=b&sig=i%2BVOQWPTvy8IcAJiux0R8thNtKDt2j3VQbmEpdgBLFI%3D&se=2018-03-18T00%3A00%3A00Z&sp=r'
    , 'https://irisscuprodstore.blob.core.windows.net/i-4d277707a9574e1b8854f4fb417f24fd/i-251b55b6db6c43568da909dfa4fafc10?sv=2017-04-17&sr=b&sig=lkB5S0QHFa13ms%2FwQ%2FisKP4FgWGygLthcUVnN%2FSqMLc%3D&se=2018-03-18T00%3A00%3A00Z&sp=r'
    , 'https://irisscuprodstore.blob.core.windows.net/i-4d277707a9574e1b8854f4fb417f24fd/i-89f53a8a91114658a35c90eeffa26ded?sv=2017-04-17&sr=b&sig=RGifaZ2WRlIy%2BwMAVWAh5lNDhqaWrPGNSIoLtUOdUdc%3D&se=2018-03-18T00%3A00%3A00Z&sp=r'
    , 'https://irisscuprodstore.blob.core.windows.net/i-4d277707a9574e1b8854f4fb417f24fd/i-2889da3996ef46c78dba6a88e134e085?sv=2017-04-17&sr=b&sig=ncsnjdHT7lvjahk4LCJnWGzguJZDFw%2B4PWUeOEZuzCQ%3D&se=2018-03-18T00%3A00%3A00Z&sp=r'
    , 'https://irisscuprodstore.blob.core.windows.net/i-4d277707a9574e1b8854f4fb417f24fd/i-e83cbe90d2474932ae0c82fff812e709?sv=2017-04-17&sr=b&sig=6LBV3tracSlKLUHBOF0gIpoxEouyOOnYEC60Z6bWOtA%3D&se=2018-03-18T00%3A00%3A00Z&sp=r'
    , 'https://irisscuprodstore.blob.core.windows.net/i-4d277707a9574e1b8854f4fb417f24fd/i-eb8c8e0fd88b4953affb8dad1626430b?sv=2017-04-17&sr=b&sig=Q1%2Fz2Uqx6rZOS%2FvzPp6Z19u%2B%2B30zNciuFNJSNYijubM%3D&se=2018-03-18T00%3A00%3A00Z&sp=r'
    , 'https://irisscuprodstore.blob.core.windows.net/i-4d277707a9574e1b8854f4fb417f24fd/i-eb89e08e1f8d41c191f3de1d8b40511d?sv=2017-04-17&sr=b&sig=dJFjsDJbf%2BI9413yinS7kJhGcg8Tvi88w4riEGjNNUA%3D&se=2018-03-18T00%3A00%3A00Z&sp=r'
    , 'https://irisscuprodstore.blob.core.windows.net/i-4d277707a9574e1b8854f4fb417f24fd/i-f1676dfe83b24b989e7754bed074af73?sv=2017-04-17&sr=b&sig=fvEIIKn%2FS%2FfElshXvM6%2BeNc0K0rGMTa%2BWWEGkIVaI6k%3D&se=2018-03-18T00%3A00%3A00Z&sp=r'
, 'https://irisscuprodstore.blob.core.windows.net/i-4d277707a9574e1b8854f4fb417f24fd/i-c34ca050529a4fabb1a4c80892c20d8e?sv=2017-04-17&sr=b&sig=xQ0n4mxuXJTCEAIjDNd4c0WLWjLY%2ByfP%2FptirMZx7MA%3D&se=2018-03-18T00%3A00%3A00Z&sp=r'
, 'https://irisscuprodstore.blob.core.windows.net/i-4d277707a9574e1b8854f4fb417f24fd/i-afeb3b68ab5b482d918025b840df27d7?sv=2017-04-17&sr=b&sig=ii4Yx3FVy5YQgBi114P3iUcgOO803VE%2B5ToDFCR9LpE%3D&se=2018-03-18T00%3A00%3A00Z&sp=r'
]

emo_dic = {'anger' : 0,
           'fear':0,
           'contempt':0,
           'happiness':0,
           'surprise':0,
           'disgust':0,
           'sadness':0,
           'neutral':0}

# for url in urls:
#     api_call = make_call(url)
#     emo_dic['anger'] = api_call[0]['faceAttributes']['emotion']['anger'] + emo_dic['anger']
#     emo_dic['fear'] = api_call[0]['faceAttributes']['emotion']['fear'] + emo_dic['fear']
#     emo_dic['contempt'] = api_call[0]['faceAttributes']['emotion']['contempt'] + emo_dic['contempt']
#     emo_dic['happiness'] = api_call[0]['faceAttributes']['emotion']['happiness'] + emo_dic['happiness']
#     emo_dic['surprise'] = api_call[0]['faceAttributes']['emotion']['surprise'] + emo_dic['surprise']
#     emo_dic['disgust'] = api_call[0]['faceAttributes']['emotion']['disgust'] + emo_dic['disgust']
#     emo_dic['sadness'] = api_call[0]['faceAttributes']['emotion']['sadness'] + emo_dic['sadness']
#     emo_dic['neutral'] = api_call[0]['faceAttributes']['emotion']['neutral'] + emo_dic['neutral']

# print emo_dic

# nervousface = {k: v / len(urls) for k, v in emo_dic.iteritems()}
# print nervousface

# print(processJson(make_call("https://how-old.net/Images/faces2/main007.jpg")))


# def add_to_blockchain():
#     do something
#
# if

def check_if_pic_nervous(url):
    Nervous = {'neutral': 0.5833571428571428, 'sadness': 0.09264285714285714,  'anger': 0.030571428571428576, 'surprise': 0.08428571428571428, 'fear': 0.14049999999999999, 'happiness': 0.06392857142857143}

    face = make_call(url)[0]
    difference = 0
    for key in  Nervous:
        difference += abs(Nervous[key]-face['faceAttributes']['emotion'][key])
    return difference, face['faceId']

# check_if_pic_nervous("https://how-old.net/Images/faces2/main007.jpg")


