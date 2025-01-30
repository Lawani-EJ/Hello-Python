from randomuser import RandomUser
import pandas as pd
import requests
import json

r = RandomUser()
some_list = r.generate_users(10)

name = r.get_full_name()
print(name)
print(some_list)

# 10 users with their full name and email adress
for user in some_list:
    print(user.get_full_name(), user.get_email())

data = requests.get('https://fruityvice.com/api/fruit/all')
results = json.loads(data.text)
print(data)
print(results)
print(pd.DataFrame(results))

df = pd.json_normalize(results)
print(df)

# Extracting the fruit name and its family
cherry = df.loc[df['name'] == 'Cherry']
cherry2 = (cherry.iloc[0]['family']),(cherry.iloc[0]['genus'])
print(cherry)
print(cherry2)
#Extracting the fruit and its calories
banana = df.loc[df['name'] == 'Banana']
banana2 = (banana.iloc[0]['name']),(banana.iloc[0]['nutritions.calories'])
print(banana)
print(banana2)
