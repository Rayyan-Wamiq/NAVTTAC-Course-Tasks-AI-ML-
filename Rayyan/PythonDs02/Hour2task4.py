Contacts = {
    "Person1": {"Name":"Rayyan", "Phone":"12345", "City":"Karachi"},
    "Person2": {"Name":"Qasim", "Phone":"17895", "City":"Lahore"}
}
print(Contacts["Person1"]["City"])
print(Contacts["Person1"]["City"][0])

for key, values in Contacts.items():
    print(key, values)

Contacts["Person1"]["Email"] = "rayyanwamiq1@gmail.com"
print(Contacts)