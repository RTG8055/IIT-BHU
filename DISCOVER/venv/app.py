import requests, datetime
from flask import Flask, render_template, redirect, json, request, session, Markup, flash

app = Flask(__name__)
app.secret_key = '8bf9547569cd5a638931a8639cf9f86237931e92' 
@app.route('/')
@app.route('/home')
def main():
	return render_template('home.html')

def get_sample_number(title_new):
	path = "output/input.txt"

	with open(path,'r') as f:
		for line in f:
			line = line.strip("\t|\n")
			title,sample_num = line.split('<--')
			if(title == title_new):
				return sample_num
	return 0;

def get_results(sample_number):
	# path = "../output/sample"+str(sample_number)+"/LN"+str(sample_number)
	path = "output/LN"+str(sample_number)+".txt"
	html_text=''

	with open(path,'r') as f:
		i=0
		for line in f:
			i+=1
			line = line.strip("\t|\n")
			print line
			rowid,rowvalue = line.split('.')
			html_text += '<tr class="row100">'
			html_text += '<td class="column100 column1" data-column="column1">' + rowid + '</td>' 
			html_text += '<td class="column100 column2" data-column="column2">' + rowvalue + '</td>' 
			html_text += '</tr>'
			if(i==15):
				break

	return html_text

@app.errorhandler(404)
@app.errorhandler(405)
def page_not_found(e):
	print e
	msg =' There was an error. go to <a href="/home">home</a> page'
	return render_template('error.html', error=msg)

@app.route('/load')
def loading():
	return render_template('loading.html')

@app.route('/home',methods=['GET','POST'])
def get_recommendations():
	topic = request.form['topic']
	title = request.form['title'].strip()
	keywords = request.form['keywords']
	abstract = request.form['abstract']

	sample_number = get_sample_number(title)
	# sample_number=2
	if(sample_number == 0):
		msg = 'Please check the title entered! No such paper found. Go to <a href="/home">home</a> page'
		# print("sample not found")
		return render_template('error.html', error=msg)
	print "afv"
	session['n']=sample_number
	
	return redirect('/load')


@app.route('/results')
def results():
	html_table = get_results(session['n'])
	# html_table = 'text to be returnredsgdcghdhrsgf'
	params={}
	params['rows'] = html_table
	return render_template('results.html',params = params)

if __name__ == "__main__":
    app.run(debug=True,port=10002,use_evalex=False)
    # app.run(debug=True,host='192.168.43.53',port=5007,use_evalex=False)


##############
# 		Co authorship, graph model, topic clustering, random walk, citation recommendation.
#############