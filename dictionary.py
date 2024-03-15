dic = {
    "Naruto": "Shado clone",
    "Itachi": "Gain Jutsu",
    "Madara": "Sukuyami",
    "Kakasi": "Copy ninja",
    "Saskey": "Saring gun"
}

print(dic)
print(dic.items())

for key, value in dic.items():
    print(f"{key} expart in {value}")

for key in dic:
    print(dic[key])

# print(dic["Hasirama"])        # it give me error
print(dic.get("Hasirama"))      # it's not give me error, it return None


