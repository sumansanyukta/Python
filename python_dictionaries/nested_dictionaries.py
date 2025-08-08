#a dictionary can contain other dictioneries
myfamily = {
    "member1":{
        "name" : "Ratish",
        "role" : "Father"
    },
    "member2":{
        "name" : "Gauri",
        "role" : "Mother"
    },
    "member3":{
        "name" : "Prabhat",
        "role" : "Brother"
    },
    "member4":{
        "name" : "Sneha",
        "role" : "Sister"
    },
    "member5":{
        "name" : "Sumnima",
        "role" : "Sister"
    }
}

print(myfamily)
print(myfamily["member1"]["name"], [myfamily["member1"]["role"]])