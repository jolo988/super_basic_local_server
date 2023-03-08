from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
import csv

# basic website route
@app.route("/")
def my_home():
    return render_template('index.html')

# make pages dynamic, so we won't have to copy/paste fixed decorators
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name )

# store email/msg to database.txt (write to FILE)
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')

# 'a' append to database.txt
#  store database.txt to csv file
def write_to_csv(data):
    with open('database.csv', newline="", mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


# backend contact/email form; send info to database.txt
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong, try again!'
