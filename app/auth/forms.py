from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField, IntegerField
from wtforms.validators import DataRequired, EqualTo


class UserCreationForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired()], render_kw={'autofocus': True})
    email = StringField("Email", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField()


class LoginForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired()], render_kw={'autofocus': True})
    password = PasswordField("Password", validators = [DataRequired()])
    submit = SubmitField()
    
class AddMugsForm(FlaskForm):
    title = StringField("title", validators = [DataRequired()], render_kw={'autofocus': True})
    img_url = StringField("img_url", validators = [DataRequired()])
    caption = StringField("caption", validators = [DataRequired()])
    price = DecimalField("price", validators=[DataRequired()])
    quantity = IntegerField("quantity", validators=[DataRequired()])
    submit = SubmitField()
    
class MakeAdminForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired()], render_kw={'autofocus': True})
    submitadmin = SubmitField()