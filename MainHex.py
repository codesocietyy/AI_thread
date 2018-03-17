from emotions import check_if_pic_nervous
from vision import object_analysis

def main(url):
    nervousness, pictureID = check_if_pic_nervous(url)
    weaponThreat = object_analysis(url)
    Risk_factor = (nervousness + weaponThreat)/2.0
    if Risk_factor > 0.8:
        # return "This is a major threat. Please report to customs and add %s BLOCKCHAIN! Get them!" % pictureID
        return pictureID, Risk_factor
    elif Risk_factor > 0.7:
        # return "Add them to the blockchain. Stay cautious"
        return pictureID, Risk_factor

    else:
        # return "Have a nice day"
        return pictureID, Risk_factor



print main('https://how-old.net/Images/faces2/main007.jpg')