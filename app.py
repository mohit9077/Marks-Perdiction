from flask import Flask, render_template, redirect, request
from sklearn.externals import joblib

app=Flask(__name__)

model=joblib.load("model.pkl")

@app.route('/')  ## routes are used for handling the different urls
def hello():
	return render_template("index.html")
	# we will write all the html code in this file
	#flask already know that html file will be present in templates folder

@app.route('/',methods=['POST'])
def submit():
	if request.method=='POST':
		hours=float(request.form['hours'])

		marks=str(model.predict([[hours]])[0][0])

	return render_template("index.html", f_marks=marks)

if __name__=='__main__':
	#app.debug= True ## if you don not set this to true then to see every small changes ,you need to restart the server
	app.run(debug=True)