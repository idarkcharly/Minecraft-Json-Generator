# @Author : Charly1307
# Version : 1.0
# Loop to be stopped manual
import json
import os

print("================welcome================\n")
print("Json file generator for Item Models\n")
# You can change the path HERE
print("EXAMPLE: C:\\Users\\carlos\\Desktop\\Guardar\\")
path = str(input("Insert the PATH directory: \n"))
file_path = os.path.join(path)

mod_id = str(input("Insert the modid: \n"))

while True:
    item_id = str(input("Insert the item id: \n"))
    # Python dictionary
    item_models = {
        "parent": "item/generated",
        "textures": {
            "layer0": ""
        }
    }

    item_models["textures"]['layer0'] = mod_id + ':item/' + item_id
    # Serializing json
    json_object = json.dumps(item_models, indent=4)
    # Generate json file
    with open(file_path + item_id+'.json', "w") as outfile:
        outfile.write(json_object)
        print("=======SUCCESS=======\n")