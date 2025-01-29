from randomuser import RandomUser
import pandas as pd

r = RandomUser()
some_list = r.generate_users(10)
print(some_list)