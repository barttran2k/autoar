import json

a = {
   "3":{
      "3":{
         "arg":"--scope-exclude-pattern",
         "value":"3"
      },
      "1":{
         "arg":"--scope-include-pattern",
         "value":"123"
      },
      "2":{
         "arg":"--scope-include-subdomains",
         "value":"123"
      }
   },
   '4':{
        "3":{
            "arg":"--scope-exclude-pattern",
            "value":"3"
        },
        "1":{
            "arg":"--scope-include-pattern",
            "value":"123"
        },
        "2":{
            "arg":"--scope-include-subdomains",
            "value":"123"
        }
   }
}
a = dict(a)
print("_______________VALUES___________________")
for key, suboptions in a.items():
    print("" + key + ":")
    for suboption, subvalue in suboptions.items():
        print( "  " + subvalue['arg'] + ": "  + subvalue['value'])