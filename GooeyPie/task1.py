
import string
import random
import gooeypie as gp

# All the possible characters in a password - letters, numbers and symbols
password_chars = string.ascii_letters + string.digits + string.punctuation

def make_password(event):
    # Create the password by choosing random characters
    new_password = ''
    for n in range(length_slider.value):
        new_password += random.choice(password_chars)

    # Display the new password in the password input field
    password_inp.text = new_password
    app.copy_to_clipboard(new_password)

app = gp.GooeyPieApp('Password generator') 

instructions = gp.Label(app, 'Set your desired password length using the slider')
length_slider = gp.Slider(app, 4, 30)
password_inp = gp.Input(app)
password_inp.justify = 'center'
entergrade = gp.Input(app)
entergradelabel = gp.Label(app, 'please enter grade')

length_slider.add_event_listener('change', make_password)

app.set_grid(5, 1)
app.add(instructions, 1, 1)
app.add(length_slider, 2, 1, fill=True)
app.add(password_inp, 3, 1, fill=True)
app.add(entergradelabel, 4, 1)
app.add(entergrade, 5, 1)

# Set the default password length. This will also trigger the make_password() function
length_slider.value = 12

app.run()