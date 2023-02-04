import json
import os
from flask import Flask, render_template, flash
from forms import *
import requests
from fileinput import filename

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"


@app.route("/", methods=["GET", 'POST'])
def home():
    form = email_form()
    if form.validate_on_submit():
        flash("Email sent")
        from_emails = form.sender_email.data
        to_emails = form.receiver_email.data
        subject = form.subject.data
        body = form.message.data
        html = form.html.data
        file = form.file.data
        file.save(file.filename)

        requestt(to_emails=to_emails, from_email=from_emails, subject=subject, body=body, file=file, html_body=html)

    return render_template("Home.html", form=form)


@app.route("/email", methods=['GET', 'POST'])
def requestt(to_emails, subject, body, file, html_body, from_email="aniruddhusa04@gmail.com", test_mode=False,
             api_key='pYkqe7Y96A2PgbTlcgZ5', ):
    url = 'https://chi-tools.uc.edu/email_service/api/send_mail'
    data = {'api_key': api_key, 'to_emails': to_emails, 'subject': subject, 'body': body,
            'from_email': from_email, 'test_mode': test_mode, 'html_body': html_body}
    files = {'files': open(file.filename, "rb")}
    requests.post(url=url, data=data, files=files)
    return "Email Sent"


if __name__ == "__main__":
    app.run(debug=True)
