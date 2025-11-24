from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, \
    BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email



class EditProfileForm(FlaskForm):
    """Edit Profile Form"""
    username = StringField('Username', validators=[DataRequired(), Length(1,64)])
    about_me = TextAreaField('About Me', validators=[Length(max=140)])
    submit = SubmitField('Save Changes')

class RegisterForm(FlaskForm):
    """Register Form"""
    username = StringField('Username', validators=[DataRequired(), Length(1,64)])
    email = StringField('Email', validators=[DataRequired(), Length(1,64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField('Username', validators=[DataRequired(), Length(1,64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class PostForm(FlaskForm):
    """Comment Form"""
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Post')