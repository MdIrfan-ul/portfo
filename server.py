from flask import Flask,render_template,url_for,request,redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<string:homepage>")
def work(homepage):
    return render_template(homepage)

def data_to_txt(data):
	with open('Datastore.txt', mode='a') as database:
		email = data["email"]
		subject = data["Subject"]
		message = data["message"]
		file = database.write(f'\n{email},{subject},{message}')

def data_to_csv(data):
	with open('Datastore.csv',mode='a',newline='') as database2:
		email = data["email"]
		subject = data["Subject"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter=',',quotechar="|", quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])



@app.route("/submit_form",methods=['POST','GET'])
def submit_form():
    if request.method=='POST':
    	data = request.form.to_dict()
    	data_to_csv(data)	
    	return redirect('thankyou.html')
    else:
    	return 'Try Again' 

   	
