airports = {"ATL":"Hartsfield–Jackson Atlanta International Airport",
      "PEK":"Beijing Capital International Airport",
			"DXB":"Dubai International Airport",
			"LAX":"Los Angeles International Airport",
			"HND":"Tokyo Haneda Airport",
			"ORD":"O'Hare International Airport (Chicago)",
			"LHR":"London Heathrow Airport",
			"SAR":"Hong Kong International Airport",
			"PVG":"Shanghai Pudong International Airport",
			"CDG":"Paris-Charles de Gaulle Airport",
			"AMS":"Amsterdam Airport Schiphol",
			"DEL":"Indira Gandhi International Airport (Delhi)",
			"CAN":"Guangzhou Baiyun International Airport",
			"FRA":"Frankfurt Airport",
			"DFW":"Dallas/Fort Worth International Airport",
			"ICN":"Seoul Incheon International Airport",
			"IST":"Istanbul Atatürk Airport",			
			"CGK":"Soekarno-Hatta International Airport",
			"SIN":"Singapore Changi Airport",
			"DEN":"Denver International Airport",
			}

def main():
    code = input('Enter a 3-digit airport code: ').upper()
    while len(code) != 3 or code not in airports.keys():
        code = input('Enter a 3-digit airport code: ').upper()
    print(airports[code])
main()
