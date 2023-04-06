from flask import Flask, render_template, request, redirect, send_from_directory
import csv
import os

app = Flask(__name__)

@app.route("/")
def my_home1():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv (data):
        with open ('database.csv', mode='a') as database2:
            email = data["email"]
            subject = data["subject"]
            input = data["input"]
            csv_writer=csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email, subject, input])

@app.route("/submit_form", methods=['GET', 'POST'])
def submit_form():
    if request.method=='POST':
        data=request.form.to_dict()
        write_to_csv(data)
        return redirect('/thanks.html')
    else:
        return "something wrong"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')







