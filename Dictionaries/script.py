D = {'a':0,'b':1,'c':2}
print(D.values()) 
print(D['b'])

Dict = {"key1":1,"Key2":"2","Key3":[3,3,3],"Key4":(4,4,4),'Key5':5, (0,1):6}
print(Dict)
print(Dict.keys)
print(Dict[0,1])

release_year_dict = {"Thriller":"1982","Back in Black" :"1980","The Dark Side Of The Moon":"1973","The BodyGuard":"1992","Bat Out Of Hell":"1977","Their Greatest Hits (1972-1975)":"1976","Saturday Night Fever":"1977","Rumors":"1977"}
print(release_year_dict)
print(release_year_dict["Thriller"])
print(release_year_dict["Back in Black"])

getting_release_year_keys = release_year_dict.keys()
print(getting_release_year_keys)
# print(release_year_dict.keys())

getting_release_year_values = release_year_dict.values()
print(getting_release_year_values)
# print(release_year_dict.values())

release_year_dict['Graduation'] = '2007'
updated_release_year_dict = release_year_dict
print (updated_release_year_dict)

del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
deleted_release_year_dict = release_year_dict
print(deleted_release_year_dict)

verify = 'Thriller' in release_year_dict
print(verify)
verify2 = 'Back in Black' in release_year_dict
print(verify2)