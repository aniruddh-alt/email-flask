from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired, Length


class email_form(FlaskForm):
    sender_email = EmailField("Sender's Email", validators=[DataRequired(), Length(3, 50)])
    receiver_email = EmailField("Reciever's Email", validators=[DataRequired(), Length(3, 50)])
    subject = StringField("Subject")
    message = StringField("Message", validators=[DataRequired()])
    submit = SubmitField("submit")
