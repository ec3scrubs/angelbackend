#!flask/bin/python
from flask import Flask, jsonify

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