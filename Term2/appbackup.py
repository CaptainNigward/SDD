import gooeypie as gp
from pcpartpicker import API 

app = gp.GooeyPieApp("PC Part Picker")
app.width = 700
app.height = 200 

app.set_grid(2,1)
first_page_logo = gp.Image(app, 'Term2\PCPartPicker_Logo.png')
begin_button = gp.Button(app,'Start Building', None)

app.add(first_page_logo,1, 1 )
app.add(begin_button, 2, 1)
app.run()

def cpupage(event):
    cpupage = gp.Window(app, 'cpupage')
    
api = API()

#The following code is provided by Mr. Fong 
#First go and pull the json format

def retrieve_data_from_pc_part_picker(component):
    initial_pull = api.retrieve(component)
    remove_dictionary_wrapper = initial_pull[component]
    formatted_list = [component for component in remove_dictionary_wrapper]
    return formatted_list


#make the data python friendly :) - adjust the i.[field] to add more

def access_fields(data_set):
    small_list = []
    for i in data_set:
        small_list.append([i.brand, i.model, i.price])
    return small_list

cpu_data = retrieve_data_from_pc_part_picker("cpu")
cpu_smaller_list = access_fields(cpu_data)
x = cpu_smaller_list 
scpu = ("Intel") #variable for user input 

for i in x: #linear search for brands and filtering out unavailable items
    if i[2] == "<Money: 0.00USD>" : #can't access integer in field 2 #Goal : if money = 0, item is not available 
        print("Item not available")
    elif i[0] == scpu: 
        print (i)
    else:
        pass
