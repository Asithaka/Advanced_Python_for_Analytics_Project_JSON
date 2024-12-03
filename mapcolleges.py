import json

infile_sc = open('schools.geojson','r')

infile_ut = open('univ.json','r')

sc_data=json.load(infile_sc)

ut_data=json.load(infile_ut)


outfile_ut = open('readble_school_data.json', 'w')

json.dump(sc_data, outfile_ut, indent= 2 )

# Creating empty lists for total, make, female and Big 12 schools

big_12_schools = []
enrollment = []
male1 = []
male = []
female = []

# Filtering the Big 12 schools from unic.json and appending them to alist

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


names  = []
addresses = [] 
lats = []
lons = []

list_of_school = sc_data['features']

for line in list_of_school:

     if line['properties']['NAME'] in big_12_schools:

        name = line['properties']['NAME']
        address = line['properties']['STREET'] +' '+ line['properties']['CITY']+' '+ line['properties']['STATE'] + ' ' + line['properties']['ZIP']
        lon = line['geometry']['coordinates'][0]
        lat = line['geometry']['coordinates'][1]

        names.append(name)
        addresses.append(address)
        lons.append(lon)
        lats.append(lat)



print(names)
print(addresses)
print(lats)
print(lons)

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# "hoverinfo" is get from following documentation
# https://plotly.github.io/plotly.py-docs/generated/plotly.graph_objects.Scattergeo.html

data = [{
    'type':'scattergeo',
    'lon': lons,
    'lat':lats,
    'text': [f" {name}\n,{add}\n,Total Enrollment: {enr}\n,Male: {m}\n,Female: {f} " for name,add, enr,m,f in zip(names, addresses,enrollment,male,female)],
    'hoverinfo' : 'text',
     'marker' :{
        'size':[enrollment/1000 for enrollment in enrollment],
        'color':enrollment,
        'colorscale': 'ylgnbu',
        'reversescale': False,
        'colorbar' : { 'title':'Enrollment'}
    }
}]

mylayout = Layout(title = 'Enrollment of Big 12 schools')

fig ={'data':data, 'layout':mylayout}

offline.plot(fig, filename='EnrollmentofBIG12school.html')
