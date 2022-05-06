import gooeypie as gp

app = gp.GooeyPieApp (Grade )
app =


def calculation (event):
    selection = course_types.selected
    grade = int(user_inp.text)
    if selection == "Graded":
        if grade >= 85:
            result.text = "High Distinction"
        elif grade >= 75:
            result.text = "Distinction"
        elif grade >= 65:
            result.text = "Credit"
        elif grade >= 55: 
            result.text = "Pass"
        else: 
            result.text = "Fail"
    else:
        if grade >= 50:
            result.text = "pass"
        else:
            result.text = "fail"







mark.lbl = gp.Label(home, 'Mark:')

