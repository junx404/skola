import requests       # requests kräver "pip3 install requests"

stad = [('Trollhättan', 12.28, 58.28), ('Helsingborg', 12.69, 56.04), ('Jukkasjärvi', 20.60, 67,85)]

def prognos():
    for i in range(24):
        tid0data = data['timeSeries'][i]
        print(tid0data['validTime'][11:16],"      ", end=' ')
        for mätvärde in tid0data['parameters']:
            if mätvärde['name'] == 't':      
                print(mätvärde['values'][0])

while True:
    print('-'*20, 'VÄDERPROGNOS', '-'*20)
    print(' 1. Trollhättan', "\n", '2. Helsingborg', "\n", '3. Jukkasjärvi', "\n", 'Q. Avsluta')
    val = input('Välj stad: ')
    if val == "q":
        print("Ha det gott, Glenn")
        break
    try:
        print("\n24-timmars prognos för " + str(stad[int(val)-1][0]) + ":")
    except:
        print("Välj ett giltigt alternativ")
        continue

    lat = stad[int(val)-1][2]
    lon = stad[int(val)-1][1]
    url='https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/'+str(lon)+'/lat/'+str(lat)+'/data.json'
    response = requests.get(url)  # anropar SMHIs webbserver och hämtar JSON
    data = response.json()        # data nu färdig dict med alla data
    print('TIDPUNKT     TEMPERATUR')
    prognos()