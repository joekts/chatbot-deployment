#Import modules
import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

#Check for GPU support
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#Open our intents file
with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

#Load our saved training data
FILE = "data.pth"
data = torch.load(FILE)

#Define variables from our data
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

#Implement the neural network
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#Assign name to the chatbot
bot_name = "IT Services"

#Create a response
def get_response(msg):

    #Apply NLP techniques to user message
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    #Find a response using the neural network
    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    #If probability of response meets threshold output it, else chatbot does not understand
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    
    return "I do not understand..."

#Initial chatbot for testing in console, not used in prototypes implementation
if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)

