from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<string:page_location>")
def home_index(page_location):
    return render_template(page_location)

def server_data_txt(data): 
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {email}, {subject}, {message}')

def server_data_csv(data): 
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
        if request.method == 'POST': 
            try: 
                data = request.form.to_dict()
                server_data_txt(data)
                return redirect('thankyou.html')
            except: 
                return 'Did not save to database'
        else: 
            return 'uhuuummm, something is going'
