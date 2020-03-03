
# # # import os

# # # # os.remove('./files.txt')
 
 
# # # if os.path.exists('./execise2.py'):          
# # #     os.remove('./execise2.py')
# # #     print("File deleted successfully")
# # # else:
# # #     os.remove('The file does not exist')
    

# # # dictionary
# # # person_dct = {
# # #     "name": "Asabeneh",
# # #     "country": "Finland",
# # #     "city": "Helsinki",
# # #     "skills": ["JavaScrip", "React", "Python"]
# # # }
# # # print(person_dct)
# # # # JSON: A string form a dictionary
# # # person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"
# # # print(person_json)

# # # # we use three quotes and make it multiple line to make it more readable
# # # person_json = '''{
# # #     "name":"Asabeneh",
# # #     "country":"Finland",
# # #     "city":"Helsinki",
# # #     "skills":["JavaScrip", "React","Python"]
# # # }'''

# # # print(person_json)
    
# # import json
# # # JSON
# # person_json = '''{
# #     "name": "Asabeneh",
# #     "country": "Finland",
# #     "city": "Helsinki",
# #     "skills": ["JavaScrip", "React", "Python"]
# # }'''
# # print(type(person_json))
# # # let's change JSON to dictionary
# # person_dct = json.loads(person_json)
# # print(type(person_dct))
# # print(person_dct)
# # print(person_dct['country'])

# # import json
# # # python dictionary
# # person = {
# #     "name": "Asabeneh",
# #     "country": "Finland",
# #     "city": "Helsinki",
# #     "skills": ["JavaScrip", "React", "Python"]
# # }
# # print(type(person))
# # # let's convert it to  json
# # # indent could be 2, 4, 8. It beautify the json
# # person_json = json.dumps(person, indent=4)
# # print(type(person_json))
# # print(person_json)

# import json
# # python dictionary
# person = {
#     "name": "Asabeneh",
#     "Age": 30,
#     "state": "Lagos",
#     "country": "Finland",
#     "favFoof": "Yam",
#     "city": "Helsinki",
#     "skills": ["JavaScrip", "React", "Python"]
# }
# with open('./files/json_example.json', 'a', encoding='utf-8') as f:
#     json.dump(person, f,  indent=4)


import csv
with open('./files/csv_example.csv') as f:
    # w use, reader method to read csv
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count >= 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')
