from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, SubmitField,FileField
from wtforms import validators
from wtforms.validators import DataRequired, Length


class email_form(FlaskForm):
    sender_email = StringField("Sender's Email", validators=[DataRequired(), Length(3, 50)])
    receiver_email = StringField("Receiver's Email", validators=[DataRequired(), Length(3, 50)])
    subject = StringField("Subject")
    message = StringField("Message")
    html = StringField("HTML Body Text")
    file = FileField("File")
    submit = SubmitField("submit")
