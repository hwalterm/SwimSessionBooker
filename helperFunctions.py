import requests
import json
import datetime
from dateutil import parser

def getReservationData(Start_Date = '2020-10-28', End_Date = '2020-10-30'):
  headers = {
      'authority': 'arlingtonaquatics.ezfacility.com',
      'accept': '*/*',
      'x-requested-with': 'XMLHttpRequest',
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
      'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'origin': 'https://arlingtonaquatics.ezfacility.com',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://arlingtonaquatics.ezfacility.com/Sessions',
      'accept-language': 'en-US,en;q=0.9',
      'cookie': '__cfduid=d61419443394e4bd12df85e7ed30591491602765908; EZSSID=aja5abtmbtq3mhmg1y0zklaw; __RequestVerificationToken=ZKNYwxO3tMZaPPc1CCF-jUe24DGG1ZtKYo_QwNpi67a-9gETRYcb4rkf2WtqS024r4ezN8puenQwxvEnkONTWD9EOMk1',
  }

  data = {
    'LocationId': '2451',
    'Sunday': 'true',
    'Monday': 'true',
    'Tuesday': 'true',
    'Wednesday': 'true',
    'Thursday': 'true',
    'Friday': 'true',
    'Saturday': 'true',
    'StartTime': '12:00 AM',
    'EndTime': '12:00 AM',
    'ReservationTypes[0].Selected': 'true',
    'ReservationTypes[0].Id': '-1',
    'ReservationTypes[1].Id': '220004',
    'ReservationTypes[2].Id': '220670',
    'ReservationTypes[3].Id': '218723',
    'ReservationTypes[4].Id': '180273',
    'ReservationTypes[5].Id': '221056',
    'ReservationTypes[6].Id': '220559',
    'ReservationTypes[7].Id': '221500',
    'ReservationTypes[8].Id': '221328',
    'ReservationTypes[9].Id': '220665',
    'ReservationTypes[10].Id': '221050',
    'ReservationTypes[11].Id': '218205',
    'ReservationTypes[12].Id': '223886',
    'ReservationTypes[13].Id': '216191',
    'ReservationTypes[14].Id': '218201',
    'ReservationTypes[15].Id': '222784',
    'ReservationTypes[16].Id': '221061',
    'ReservationTypes[17].Id': '221057',
    'ReservationTypes[18].Id': '223340',
    'ReservationTypes[19].Id': '220667',
    'ReservationTypes[20].Id': '224418',
    'ReservationTypes[21].Id': '218202',
    'ReservationTypes[22].Id': '218206',
    'ReservationTypes[23].Id': '216193',
    'ReservationTypes[24].Id': '218223',
    'ReservationTypes[25].Id': '218232',
    'ReservationTypes[26].Id': '218234',
    'ReservationTypes[27].Id': '218104',
    'ReservationTypes[28].Id': '218228',
    'ReservationTypes[29].Id': '218233',
    'ReservationTypes[30].Id': '220030',
    'ReservationTypes[31].Id': '220031',
    'ReservationTypes[32].Id': '221621',
    'ReservationTypes[33].Id': '218231',
    'ReservationTypes[34].Id': '218105',
    'ReservationTypes[35].Id': '218229',
    'ReservationTypes[36].Id': '218226',
    'ReservationTypes[37].Id': '218222',
    'ReservationTypes[38].Id': '218227',
    'ReservationTypes[39].Id': '224005',
    'ReservationTypes[40].Id': '224004',
    'ReservationTypes[41].Id': '220014',
    'ReservationTypes[42].Id': '220013',
    'ReservationTypes[43].Id': '222608',
    'ReservationTypes[44].Id': '220015',
    'ReservationTypes[45].Id': '219876',
    'ReservationTypes[46].Id': '219880',
    'ReservationTypes[47].Id': '219779',
    'ReservationTypes[48].Id': '219945',
    'ReservationTypes[49].Id': '219780',
    'ReservationTypes[50].Id': '220668',
    'Resources[0].Selected': 'true',
    'Resources[0].Id': '-1',
    'Resources[1].Id': '152649',
    'Resources[2].Id': '152650',
    'Resources[3].Id': '152646',
    'Resources[4].Id': '152653',
    'Resources[5].Id': '151088',
    'Resources[6].Id': '152647',
    'Resources[7].Id': '152648',
    'Resources[8].Id': '152891',
    'Resources[9].Id': '156291',
    'Resources[10].Id': '153003',
    'Resources[11].Id': '227558',
    'Resources[12].Id': '227567',
    'Resources[13].Id': '227564',
    'Resources[14].Id': '227561',
    'Resources[15].Id': '227565',
    'Resources[16].Id': '227568',
    'Resources[17].Id': '227563',
    'Resources[18].Id': '227566',
    'Resources[19].Id': '227569',
    'Resources[20].Id': '227562',
    'Resources[21].Id': '146679',
    'Resources[22].Id': '163712',
    'Resources[23].Id': '151084',
    'Resources[24].Id': '147996',
    'Resources[25].Id': '151083',
    'Resources[26].Id': '147995',
    'Resources[27].Id': '151094',
    'Resources[28].Id': '151095',
    'Resources[29].Id': '229839',
    'Resources[30].Id': '227571',
    'Resources[31].Id': '227572',
    'Resources[32].Id': '151085',
    'Resources[33].Id': '151087',
    'Resources[34].Id': '150243',
    'Resources[35].Id': '152651',
    'Resources[36].Id': '152652',
    'Resources[37].Id': '152654',
    'Resources[38].Id': '152656',
    'Resources[39].Id': '153005',
    'Resources[40].Id': '227560',
    'Resources[41].Id': '154256',
    'Resources[42].Id': '154260',
    'Resources[43].Id': '154255',
    'Resources[44].Id': '150244',
    'Resources[45].Id': '154466',
    'Resources[46].Id': '156288',
    'Resources[47].Id': '158449',
    'StartDate': Start_Date,
    'EndDate': End_Date
  }

  response = requests.post('https://arlingtonaquatics.ezfacility.com/Sessions/FilterResults', headers=headers, data=data)
  return response.json()


# for i in getReservationData():
#   starttime = parser.parse(i['start'])
#   print(i)


#Get the table index of 7AM Wash-Lib Lap swimming
def getResponseindex(responseData, reservationType = 'Lap Swimming  Wash-Lib',
                     start = datetime.datetime.strptime('07:00', '%H:%M').time()):
  for i in responseData:
    startTime = parser.parse(i['start']).time()
    #print(i['reservationType'], startTime)
    if (reservationType == i['reservationType']
        and startTime ==start
        #and i[]
        ):
      return responseData.index(i)
  return -1

