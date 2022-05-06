from copy import copy
import string 
import random 
import gooeypie as gp 

app = gp.GooeyPieApp('Password Generator')



app.width = 480
app.height = 320


instructions = gp.Label(app, 'Set your password length')
length_slider = gp.Slider(app, 4, 30)
password_inp = gp.Input(app)
password_inp.justify = 'center'
check1 = gp.Checkbox(app, 'Characters')
check2 = gp.Checkbox(app,'Numbers')
check3 = gp.Checkbox(app, 'punctuations')

# passchars = [] 

# def passwordchars1(event):
#     passchars += string.ascii_letters

# def passwordchars2(event):
#     passchars += string.digits

# def passwordchars3(event):
#     passchars += string.punctuation

def make_password(event):

    passchars = "" 

    if check1.checked == True :
        passchars += string.ascii_letters
    if check2.checked == True :
        passchars += string.digits
    if check3.checked == True :
        passchars += string.punctuation

    new_password = ''
    for i in range(length_slider.value):
        new_password += random.choice(passchars)

    password_inp.text = new_password
    app.copy_to_clipboard(new_password)

# Event listeners
length_slider.add_event_listener('change', make_password)
check1.add_event_listener('change', make_password)
check2.add_event_listener('change', make_password)
check3.add_event_listener('change', make_password)



reset = gp.Button(app, 'reset', make_password)
app.set_grid(7,1)
app.add(instructions, 1,1, fill=True)
app.add(length_slider, 2, 1, fill=True)
app.add(password_inp, 3, 1, fill=True )
app.add(check1, 4, 1)
app.add(check2, 5, 1)
app.add(check3, 6, 1)
app.add(reset, 7,1)
app.run(    )