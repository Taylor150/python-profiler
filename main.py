# Profiler guesses your age, gender and nationality
import requests
import json
# App

# User's input
my_nam = input("Please input your first name here: ")

# Nationality
response = requests.get('https://api.nationalize.io/?name=' + my_nam)
nam_data = response.json()
# Selecting the correct key
nam_data = (nam_data['country'][0])
my_nat = (nam_data['country_id'])
print("Nationality: "), print(my_nat)

# Age
response = requests.get('https://api.agify.io/?name=' + my_nam + '&country_id=' + my_nat)
age_data = response.json()
# Selecting the correct key
age_data = (age_data['age'])
print("Age: "), print(age_data)

# Gender
response = requests.get('https://api.genderize.io/?name=' + my_nam + '&country_id=' + my_nat)
gen_data = response.json()
# Selecting the correct key
gen_data = (gen_data['gender'])
print("Gender: "), print(gen_data)
