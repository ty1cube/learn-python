#1. vegetables fruit& aninmals
# fruit_products = ("apple","carrot","grape","pineapple","watermelon","strawberry","balckberry")
# vegetable_products = ("broccoli","brussels","artichoke","aubergine","asparagus")
# animal_product = ("milk","meat","cheese","egg")
# food_stuff = fruit_products+vegetable_products+animal_product
# print (food_stuff)


#2. contry
# country = input("Enter a country: ")
# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# for countries in nordic_countries:
#     if country in countries:
#         print(country,"is a nordic country")
# else:
#     print("The country you enter is not a nordic country")


#3. siblings
# sibl =()
# sibling_sister = ("adepeju","kofoworola","olajumoke","adebimpe",)
# sibling_brother = ("ahmed","kayode","nuhu")
# siblings = sibling_brother+sibling_sister
# print ("The total number of siblings is:", len(siblings))
# parent = ("Mr abdul","Mrs abdul")
# sibling_brother,*family_member =siblings ,"Mr abdul","Mrs abdul"
# print(family_member)


#4.
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# front_end.extend(["Python", "SQL"])
# full_stack = back_end+front_end

# # front_end.append("SQL")
# print(full_stack)



#5 unpacking list
country1,country3,country2,*scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print("The following countries are scandic:",scandic)



#6 student age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
srt_age = sorted(ages)
age_max = max(srt_age)
age_min = min(srt_age)
age_sum = age_min +age_max
print("The sum of the ages is: ",age_sum)

def median(age):
    srt_age = sorted(ages)
    lstLen = len(ages)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return srt_age[index]
    else:
        return (srt_age[index] + srt_age[index + 1])/2
    
print("The median is:",median(ages))
def average(item):
    return sum(item)/len(item)
print("The average of the age is: ",average(ages))
print("The range of maximum and minimum age :",range(age_max,age_min))
print(abs(age_min-average(ages)))
print(age_max-average(ages))

#7dictionary

person = {
'first_name':'Azeez',
'last_name':'Akinsola',
'age':250,
'country':'Nigeria',
'is_marred':True,
'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address':{
    'street':'Space street',
    'zipcode':'02210'
}
}
# if "skills"!= " ":
#      print(person["skills"][2])
if "skills" in person.keys():
    if "Python" in person.values():
        print(person["skills"])
# for person_values in person.values():



#8. file loop
# country_handler = open("countries.py","r")
# country_list = country_handler.readlines()
# country_handler.close()
# for countries in country_list:
#     country_found = countries.find("land")
#     if country_found>=0:
#         print(countries)