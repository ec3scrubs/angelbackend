#!flask/bin/python
from flask import Flask, jsonify
import requests

###############################
## HPE Sentiment requests
###############################

# Init
f = open('hpe_api_key', 'r')
api_key = f.read()

# Go through the corpus
def parse(text):
  pass


# Send request to HPE
def sentiment_request(text):
  r = requests.get('https://api.havenondemand.com/1/api/sync/analyzesentiment/v1?text=hey+there&apikey=' + api_key)
  print r.text
  

###############################
## Flask app
###############################
app = Flask(__name__)

sentiments = [
  {
    'id': 1,
    'date': u'19-05-2015',
    'description': u'ate food',
    'sentiment': u'positive',
    'score': u'0.5' 
  },
  {
    'id': 2,
    'date': u'20-05-2015',
    'description': u'failed all the exams rofl',
    'sentiment': u'negative',
    'score': u'-0.9' 
  },

]

@app.route('/sentiment/api/', methods=['GET'])
def get_sentiments():
  return jsonify({'sentiments': sentiments})


if __name__ == '__main__':
    app.run(debug=True)