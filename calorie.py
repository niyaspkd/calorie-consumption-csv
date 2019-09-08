import csv
from operator import itemgetter
from collections import Counter
# from collections import OrderedDict
calorie_count = {}
tot = {}
final = {}
person_list =[]
food_list = []
calorie_map_v = []
person_data = {}
food_freq = {}
fav_food = {}
# calorie_data = csv.reader(open('Calories.csv', newline=''), delimiter=' ', quotechar='|')
# calori_data1 = csv.reader(open('Calories1.csv', newline=''), delimiter=' ', quotechar='|')

# for data in calorie_data :
# 	print (calorie_data) 
# 	try:
# 		calorie_count[data[0]] = data[-1]
# 	except:
# 	    "Task finished"

# print (calorie_count)
def calorie_map():
	try:
		calorie_data1 = csv.DictReader(open("Calories.csv"))
		# for data in calorie_data:

		# 	# dict_value = sorted(data.items(), key=lambda x: x[1]['Calories'])
		# 	# print (dict_value)
		for value in calorie_data1:
			calorie_map_v.append(dict(value))
		return calorie_map_v
	except:
		"finished"

def total_cal():
	try:
		calorie_data = csv.DictReader(open("Calories.csv"))
		calorie_data1 = csv.DictReader(open("Calories1.csv"))
		# for data in calorie_data:

		# 	# dict_value = sorted(data.items(), key=lambda x: x[1]['Calories'])
		# 	# print (dict_value)
		# for value in calorie_data:
		# 	total_list.append(value)

		# return (total_list)

		for data in calorie_data1:

			# dict_value = sorted(data.items(), key=lambda x: x[1]['Calories'])
			# print (dict_value)
			person_list.append(dict(data))

		

		for food_value in person_list:

			
			person_data.setdefault(food_value['person'], []).append([food_value['food'],food_value['qty']])


			food_list.append(food_value['food'])
		return food_list
	except:
		"finished"
	 
	

def favourite_food():
	try:
		for food in food_list:
			if food not in food_freq:
				food_freq[food]=1
			else:
				food_freq[food]+=1
		
		total_freq = sorted(food_freq.items(), key=lambda item: item[1])
		fav = total_freq[-1]
		
		print ("favourite_food for all :" ,  str(fav[0]))
		print ("liked by:", str(fav[1]))
	except:
		"done"

def favourite_for_person():
	try:
		for per,fud in person_data.items():
			fav_me = sorted(fud, key=lambda x: int(x[1]))

			fav_food[per] = fav_me[-1]
		return fav_food
	except:
		"done"

def fav_calorie_max():

	try:
		for person, favo in fav_food.items():
			for cal_data in calorie_map_v:
				if cal_data['Food'] == favo[0]:
					total_cal = int(favo[1]) * int(cal_data['Calories'])

					print (str(person)+ '-' +str(favo[0]) + '-' + str(total_cal))
	except:
			"index issue"

def total_calorie_all():
	
	for key, val in person_data.items():
		
		for i in val:

			for dat in calorie_map_v:
				
				if dat['Food'] == i[0]:

			   		total =  int(i[1]) * int(dat['Calories'])
			   		tot.setdefault(key, []).append(total)
			   		
	return tot
			   		
def final_list_cal():
	for food, cal in tot.items():

		final[food] = sum(cal)
	return final


 

total_cal()	
print("************************************")
print("************************************")	
favourite_food()
favourite_for_person()
print("************************************")
calorie_map()
print("Favourite food Calories")
print("************************************")
fav_calorie_max()
print("************************************")
print("Individual Consumption total")
total_calorie_all()
print (final_list_cal())