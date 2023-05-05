import json
values = {
    "U": {
        "name": "URL (Required)",
        "options": {
            "values":"abc"}
    }
}
options = json.loads(open("options.json").read()) 
flag = 0
for key, option in options.items():
    try:
        if option["options"]["required"] is True:
            if key not in values.keys():
                print(f"Error: {option['options']['name']} is required.")
                print(option["options"]["name"] + " = " + option["options"]["value"])
                flag +=1
                t=0
    except:
        for i in option["options"]:
            if len(i) > 1:
                if option["options"][i]['required'] is True:
                    print("false")