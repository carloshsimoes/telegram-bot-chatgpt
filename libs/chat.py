import openai

from config import openaiApiKey

openai.api_key = openaiApiKey


def askToGPT(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response



def createImageGPT(image):
    response = openai.Image.create(
        prompt=image,
        n=1,
        size='1024x1024'
    )
    imageUrl = response['data'][0]['url']
    return imageUrl

