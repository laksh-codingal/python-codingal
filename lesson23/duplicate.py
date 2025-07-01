
student_data = {
    "id1":{
        "name":["affan"],
        "class":["V"],
        "subject":["english,math,science"]

    },
    "id2":{
        "name":["bhuvan bp"],
        "class":["V"],
        "subject":["english,math,science"]

    },
    "id3":{
        "name":["arjun"],
        "class":["V"],
        "subject":["english,math,science"]

    },
    "id4":{
        "name":["bhuvan bp"],
        "class":["V"],
        "subject":["english,math,science"]

    },
    "id5":{
        "name":["laksh"],
        "class":["V"],
        "subject":["english,math,science"]

    },

}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key]=value

print(result)

