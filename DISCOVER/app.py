import requests, datetime
from flask import Flask, render_template, redirect, json, request, session, Markup, flash

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def main():
	return render_template('home.html')

@app.route('/submit',methods=['POST'])
def get_recommendations():
	topic = request.form['topic']
	title = request.form['title']
	keywords = request.form['keywords']
	abstract = request.form['abstract']




if __name__ == "__main__":
    app.run(debug=True,port=10002,use_evalex=False)
    # app.run(debug=True,host='192.168.43.53',port=5007,use_evalex=False)


##############
# 			Co authorship, graph model, topic clustering, random walk, citation recommendation.
#############