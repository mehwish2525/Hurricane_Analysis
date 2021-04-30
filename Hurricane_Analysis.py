# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def update_damage(list1):
  new_damage = []
  for i in list1:
    if i == "Damages not recorded":
      new_damage.append("Damages not recorded")
    elif i.find("M")>0:
      tmp = i.split("M")
      tmp2 = float(tmp[0])*conversion["M"]
      new_damage.append(tmp2)
    elif i.find("B")>0:
      tmp = i.split("B")
      tmp2 = float(tmp[0])*conversion["B"]
      new_damage.append(tmp2)
  return new_damage

# test function by updating damages
update_damages = update_damage(damages) 

# 2 
# Create a Table
def name_hurricanes(Name,Month,Year,Max_sustained_wind,Areas_affected,Damage,Death):
  hurricanes = {}
  hurricane = {}
  for i in range(0,len(Name)):
    hurricanes = {"Name":Name[i],"Month":Month[i],"Year":Year[i],"Max Sustanined Wind": Max_sustained_wind[i],"Areas Affected":Areas_affected[i],"Damage":Damage[i],"Death":Death[i]}
    hurricane[Name[i]] = hurricanes
  return(hurricane)

# Create and view the hurricanes dictionary
hurricane = name_hurricanes(names,months,years,max_sustained_winds,areas_affected,update_damages,deaths)
#print(hurricane)

# 3
# Organizing by Year
def year_hurricanes(dict1_dict1):
  current_year= {}
  current_cane = {}
  current_cane2 = {}
  for keys,values in dict1_dict1.items():
    current_year = values["Year"]
    current_cane = values
    current_cane2[current_year] = current_cane
  return current_cane2
# create a new dictionary of hurricanes with year and key
hurricanes_year = year_hurricanes(hurricane)
#print(hurricanes_year)

# 4
# Counting Damaged Areas
def damaged_areas(dict1_dict1):
  hurricanes_affected_areas = {}
  count = 0
  for key in dict1_dict1:
    area_list = dict1_dict1[key]["Areas Affected"]
    for area in area_list:
      if area in hurricanes_affected_areas:
        hurricanes_affected_areas[area] = hurricanes_affected_areas[area]+1
      else:
        hurricanes_affected_areas[area] = 1
  return(hurricanes_affected_areas)

# create dictionary of areas to store the number of hurricanes involved in
affected_area_count = damaged_areas(hurricane)
#print(affected_area_count)

# 5 
# Calculating Maximum Hurricane Count
def most_effected(dict1_dict1):
  max_area_count = 0
  max_area = 'Central America'
  for keys,values in dict1_dict1.items():
    if values>=max_area_count:
      max_area_count=values+1
      max_area = keys
  return max_area, max_area_count-1

# find most frequently affected area and the number of hurricanes involved in
most_effected_areas = most_effected(affected_area_count)

print("The most effected by "+str(int(most_effected_areas[1])) +"x was casused in " + str(most_effected_areas[0])+ " area." )

# 6
# Calculating the Deadliest Hurricane
def most_deaths_fuct(dict1_dict1):
  max_mortality_cane = "Cuba I" 
  max_mortality = 0
  for keys,values in dict1_dict1.items():
    if values["Death"]>=max_mortality:
      max_mortality = values["Death"]
      max_mortality_cane = keys
  return max_mortality_cane,max_mortality
  
# find highest mortality hurricane and the number of deaths
most_deaths = most_deaths_fuct(hurricane)
print("The most deaths of "+str(int(most_deaths[1])) +" was casused by hurricane " + str(most_deaths[0])) 


# 7
# Rating Hurricanes by Mortality
def mortality_rates(dict1_dict1):
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for keys,values in dict1_dict1.items():
    if values["Death"] == 0:
      hurricanes_by_mortality[0].append(keys)
    if values["Death"]>=0 and values["Death"]<100:
      hurricanes_by_mortality[1].append(keys)
    if values["Death"]>=100 and values["Death"]<500:
      hurricanes_by_mortality[2].append(keys)
    if values["Death"]>=500 and values["Death"]<1000:
      hurricanes_by_mortality[3].append(keys)
    if values["Death"]>=1000 and values["Death"]<10000:
      hurricanes_by_mortality[4].append(keys)
    if values["Death"]>=100000:
      hurricanes_by_mortality[5].append(keys)
  return hurricanes_by_mortality

# categorize hurricanes in new dictionary with mortality severity as key
mortality_rating = mortality_rates(hurricane)
print(mortality_rating)

# 8 Calculating Hurricane Maximum Damage
def greatest_damage(dict1_dict1):
  max_damage_hurrican = "Cuba I"
  max_damage_cost = 0
  for keys,values in dict1_dict1.items():
    if values["Damage"]=="Damages not recorded":
      tmp = "C"
    else:
      if values["Damage"]>max_damage_cost:
        max_damage_cost = values["Damage"]
        max_damage_hurrican = keys
  return max_damage_hurrican,max_damage_cost

# find highest damage inducing hurricane and its total cost
greatest_damage = greatest_damage(hurricane)
print("The greatest damage of "+str(int(greatest_damage[1])) +" was casused by hurricane " + str(greatest_damage[0])) 

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def damage_rates(dict1_dict1):
  hurricanes_by_damages = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for keys,values in dict1_dict1.items():
    if values["Damage"]=="Damages not recorded":
      tmp = "C"
    else:   
      if values["Damage"] == damage_scale[0]:
        hurricanes_by_damages[0].append(keys)
      elif values["Damage"]>=damage_scale[0] and values["Damage"]<damage_scale[1]:
        hurricanes_by_damages[1].append(keys)
      elif values["Damage"]>=damage_scale[1] and values["Damage"]<damage_scale[2]:
        hurricanes_by_damages[2].append(keys)
      elif values["Damage"]>=damage_scale[2] and values["Damage"]<damage_scale[3]:
        hurricanes_by_damages[3].append(keys)
      elif values["Damage"]>=damage_scale[3] and values["Damage"]<damage_scale[4]:
        hurricanes_by_damages[4].append(keys)
      elif values["Damage"]>=damage_scale[4]:
        hurricanes_by_damages[5].append(keys)
  return hurricanes_by_damages

# categorize hurricanes in new dictionary with damage severity as key
damages_from_hurricanes = damage_rates(hurricane)
print(damages_from_hurricanes)
