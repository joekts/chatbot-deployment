
## Initial Setup:

1. You need Python installed on your computer. https://www.w3schools.com/python/python_getstarted.asp

Clone repo and create a virtual environment
```
$ git clone https://github.com/joeskts/chatbot-deployment.git
$ cd chatbot-deployment
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
>>> quit()
```
Run
```
$ (venv) python train.py
```
$ (venv) python app.py
```
From there open the index.html file, and create a live server using the following VSCode exension: https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer

Created from Patrick Loeber's YouTube videos.
https://www.youtube.com/watch?v=a37BL0stIuM&t=235s
