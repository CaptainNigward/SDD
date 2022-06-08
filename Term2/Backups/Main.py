from pcpartpicker import API 

api = API()

#The following codes are provided by Mr. Fong #open source 
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
        small_list.append([i.price])
    return small_list

cpu_data = retrieve_data_from_pc_part_picker("cpu")
cpu_smaller_list = access_fields(cpu_data)
print(cpu_smaller_list(1))

