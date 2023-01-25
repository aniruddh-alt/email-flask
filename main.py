from flask import Flask, render_template, request, flash
from forms import *
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"


@app.route("/", methods=['GET', 'POST'])
def home():
    form = email_form()
    if form.validate_on_submit():
        flash("Email sent")
        from_emails = form.sender_email.data
        to_emails = form.receiver_email.data
        subject = form.subject.data
        body = form.message.data
        requestt(to_emails=to_emails, from_email=from_emails, subject=subject, body=body)

    return render_template("Home.html", form=form)


@app.route("/email", methods=['GET', 'POST'])
def requestt(to_emails, subject, body, from_email="aniruddhusa04@gmail.com", test_mode=False, api_key=123):
    url = 'https://chi-tools.uc.edu/email_service/api/send_mail'
    data = {'api_key': api_key, 'to_emails': to_emails, 'subject': subject, 'body': body,
            'from_email': from_email, 'test_mode': test_mode}
    r = requests.post(url=url, json=data)
    return r


if __name__ == "__main__":
    app.run(debug=True)
