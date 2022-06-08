import gooeypie as gp
from pcpartpicker import API 


    
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
even_smaller_cpu_list = []
scpu = ("Intel")
# def cpumodelfilter(event):
#     for i in even_smaller_cpu_list:
#         for letters in i[2]:
#             if letters = filtertextbox:


for i in cpu_smaller_list:
    stringify = str(i[2]) # convert <Money: X.XX USD> into a string, e.g. "US$X.00"
    remove_us_prefix = stringify[3:] # cut off the US$ part
    remove_us_prefix = ''.join(str(remove_us_prefix).split(',')) #inspired by stackoverflow

    floatify = float(remove_us_prefix) # convert back into a float
        

    if floatify == 0.00:
        i[2] = "item not available"
        
        even_smaller_cpu_list.append(i)
    else:
        even_smaller_cpu_list.append(i)  
# print (even_smaller_cpu_list)



 
def cpupage(event):
    
    def cpufilter (event): #filter function 
        print ("cpufilter worked ! ")
        filtered_cpu_list = []

        if intelcpucheckbox.checked == True: #Intel filter 
            for i in even_smaller_cpu_list: 
                if i[0] == "Intel":
                    filtered_cpu_list.append (i)

        if amdcpucheckbox.checked == True: #AMD filter 
            for i in even_smaller_cpu_list:
                if i[0] == "AMD":
                    filtered_cpu_list.append (i)

        if modelcheckbox.checked == True: #filter model using first letter 
        
            for item in even_smaller_cpu_list:
                if filtertextbox.text == item[1][0]:
                    filtered_cpu_list.append (item) 
                else:
                    pass
        
        print(filtered_cpu_list)
        #return (filtered_cpu_list) # i want to return this to the outer funtion into the table 
    
            
        
        
        
        
    cpupage = gp.Window(app, 'cpupage')
    cpupage.width = 1280
    cpupage.height = 720
    cpupage.show_on_top()
    
    cputable = gp.Table(cpupage, ['Brand', 'Model', 'Price'])
    intelcpucheckbox = gp.Checkbox(cpupage, 'Intel')
    amdcpucheckbox = gp.Checkbox(cpupage, "AMD")
    modelcheckbox = gp.Checkbox(cpupage, 'Model')
    filtertextbox = gp.Input(cpupage)
    cputable.set_column_widths(150, 350, 300)
    for i in even_smaller_cpu_list:
        cputable.add_row([i[0], i[1], i[2]])
    cpupage.set_grid(3,2)
    cpupage.add(cputable, 1, 1, fill=True, column_span=2)   
    cpupage.add(intelcpucheckbox, 2,1)
    cpupage.add(amdcpucheckbox, 2, 2)
    cpupage.add(modelcheckbox, 3, 1)
    cpupage.add(filtertextbox, 3, 2)      

    modelcheckbox.add_event_listener('change', cpufilter) #User input detection 
    intelcpucheckbox.add_event_listener('change', cpufilter)
    amdcpucheckbox.add_event_listener('change', cpufilter)
    filtertextbox.add_event_listener('change', cpufilter)



        
      
    

app = gp.GooeyPieApp("PC Part Picker")
app.width = 700
app.height = 200 
app.set_resizable(True) #dom helped me with this 

app.set_grid(2,2)
first_page_logo = gp.Image(app, 'Term2\PCPartPicker_Logo.png')
begin_button = gp.Button(app,'Start Building', cpupage)

app.add(first_page_logo,1, 1, fill=True, column_span = 2 )
app.add(begin_button, 2, 1, fill=True, column_span= 2)
app.run()
