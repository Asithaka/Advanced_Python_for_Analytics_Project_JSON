import json

infile_sc = open('schools.geojson','r')

infile_ut = open('univ.json','r')

sc_data=json.load(infile_sc)

ut_data=json.load(infile_ut)


outfile_ut = open('readble_school_data.json', 'w')

json.dump(sc_data, outfile_ut, indent= 2 )

big_12_schools = []
enrollment = []
male1 = []
male = []
female = []


for line in ut_data:

    if line['NCAA']['NAIA conference number football (IC2020)'] == 108:

        big_12_schools.append(line['instnm'])
        enrollment.append(line['Total  enrollment (DRVEF2020)'])
        male1.append(line['Percent of total enrollment that are women (DRVEF2020)'])
        female.append(round(int(line['Total  enrollment (DRVEF2020)'])*(int(line['Percent of total enrollment that are women (DRVEF2020)'])/100)))
        male.append(round(int(line['Total  enrollment (DRVEF2020)'])*(100 - (int(line['Percent of total enrollment that are women (DRVEF2020)'])))/100))

print(big_12_schools)
print(enrollment)
print(male1)
print(male)
print(female)


list_of_school = sc_data['features']

for line in list_of_school:

    print(line['properties']['NAME'])
    print(line['properties']['STREET'] +' '+ line['properties']['CITY']+' '+ line['properties']['STATE'] + ' ' + line['properties']['ZIP'])


name  = []
address = [] 
lat = []
lon = []
enrollment = []
male =[]
female =[]

for line in sc_data:

    if line['properties']['NAME'] in big_12_schools:
         
        name.append(line['properties']['NAME'] )
        address.append(line['properties']['STREET'] +line['properties']['CITY'] +line['properties']['STATE'] +line['properties']['ZIP'])
        

    print(name)

