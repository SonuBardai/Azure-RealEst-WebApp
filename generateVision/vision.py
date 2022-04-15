import os
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes, VisualFeatureTypes
import json

credentials = json.load(open('generateVision/credentials.json'))
API_KEY = credentials['API_KEY']
ENDPOINT = credentials['ENDPOINT']
cv_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))

def getTags(image_url):
    response = cv_client.describe_image_in_stream(image = open(image_url, 'rb'))
    return response.tags

def getTagsByImage(image):
    response = cv_client.describe_image_in_stream(image = image)
    return response.tags


# print(getTags('./testingImages/5.jpg'))