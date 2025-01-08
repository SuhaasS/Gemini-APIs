# Gemini API reading images
from PIL import Image
import google.generativeai as genai

from pathlib import Path

image_content = None
try:
    genai.configure(api_key="AIzaSyAIGf_2RGsLijy4HAn60AvPMSPqN9Bf_Ic")  # configures my api key so that any call uses my api key
    model = genai.GenerativeModel("gemini-1.5-flash")   # choses the model of Gemini

    print('Generating Content...')
    prompt = 'Describe the photo? How many cars? What is the license plate number(s)?'
    '''
    Cars:
    /Users/suhaassurapaneni/Downloads/istockphoto-1247667822-612x612.jpg
    '''
    '''
    Tirupati:
    /Users/suhaassurapaneni/Downloads/maxresdefault.jpg
    /Users/suhaassurapaneni/Downloads/ee0a3926-df7a-11ec-8fe2-ac5ac3115257_1653851450176.avif
    '''

    image_path = Path('/Users/suhaassurapaneni/Downloads/istockphoto-1247667822-612x612.jpg')
    image_content = Image.open(image_path)

    response = model.generate_content([prompt, image_content])   # gets a response from the chosen model from the given prompt
                                                                # type(response) == GenerateContentResponse
    print('Content Generated!!!')

    print(response.text)    # prints response test

finally:
    if image_content != None:
        image_content.close()
        print('Closed!!!')
        