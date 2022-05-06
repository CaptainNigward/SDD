from re import S
from textwrap import fill
import gooeypie as gp 


app = gp.GooeyPieApp('Voting System')
app.width = 480 
app.height = 320 

Govlogo = gp.Image(app, 'GooeyPie\AUGOV.png')
Text1 = gp.Label(app, 'House of representitives voting system ')

def CastStart(event):   
    StartVoting = gp.Window(app, 'Cast Your Vote')
    submit_button = gp.Button(StartVoting, 'Submit', thxpage)
    #window config
    StartVoting.width = 1080
    StartVoting.height = 320 
    StartVoting.show_on_top()
    StartVoting.set_grid(2,7)
    

    #labels 
    
    instructionlabel = gp.Image(StartVoting, 'GooeyPie\AUGOV.png')
    instructionlabel.width = 100
    
    candidate1label = gp.Label(StartVoting, 'Candidate 1')
    candidate2label = gp.Label(StartVoting, 'Candidate 2')
    candidate3label = gp.Label(StartVoting, 'Candidate 3')
    candidate4label = gp.Label(StartVoting, 'Candidate 4')
    candidate5label = gp.Label(StartVoting, 'Candidate 5')
    candidate6label = gp.Label(StartVoting, 'Candidate 6')
    
    #dropdown lists
    preference_list = [1,2,3,4,5,6]


    candidatechoice1 = gp.Dropdown(StartVoting, preference_list)
    candidatechoice2 = gp.Dropdown(StartVoting, preference_list)
    candidatechoice3 = gp.Dropdown(StartVoting, preference_list)
    candidatechoice4 = gp.Dropdown(StartVoting, preference_list)
    candidatechoice5 = gp.Dropdown(StartVoting, preference_list)
    candidatechoice6 = gp.Dropdown(StartVoting, preference_list)

    

    StartVoting.add(instructionlabel, 1,1)
    StartVoting.add(candidate1label, 1,2)
    StartVoting.add(candidate2label, 1,3)
    StartVoting.add(candidate3label, 1,4)
    StartVoting.add(candidate4label, 1,5)
    StartVoting.add(candidate5label, 1,6)
    StartVoting.add(candidate6label, 1,7)

    StartVoting.add(candidatechoice1, 2,2)
    StartVoting.add(candidatechoice2, 2,3)
    StartVoting.add(candidatechoice3, 2,4)
    StartVoting.add(candidatechoice4, 2,5)
    StartVoting.add(candidatechoice5, 2,6)
    StartVoting.add(candidatechoice6, 2,7)

    StartVoting.add(submit_button, 2, 1)
    

def thxpage(event):
    thxpage = gp.Window(app, 'Thank you for voting')
    thxpage.width = 480
    thxpage.height = 320
    thxpage.show_on_top()
    thxpage.set_grid(2,1)

    thankslabel = gp.Label(thxpage, 'Thank you for voting')

    thxpage.add(thankslabel,1,1 )
 


BeginButton = gp.Button(app, 'Begin', CastStart)
    


app.set_grid(4,1)
app.add(Govlogo, 1, 1, align = 'center')
app.add(Text1, 2, 1, align = 'center' )
app.add(BeginButton,3,1, align = 'center')



    



app.run()