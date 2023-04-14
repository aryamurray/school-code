from Aviation import *

avi = Aviation()

flightsFileName = "flights.txt"

def equals (expected, student):
    expected = expected.replace(" ", "")
    expected = expected.replace("\t", "")
    expected = expected.lower()
    student = student.replace(" ", "")
    student = student.replace("\t", "")
    student = student.lower()
    return expected == student

#----- keep the code above this line uncommented ----------


# # --------------- Test 1 - Airport methods ---------------

a1 = Airport("YXU", "London", "Canada","North America")
a2 = Airport("ABC", "Madrid", "Spain","Europe")
a2.setCity("Athens")
a2.setCountry("Greece")
t1 = a1.getCode() == "YXU" and a1.getCity() == "London" and a1.getCountry() == "Canada"
t2 = a2.getCode() == "ABC" and a2.getCity() == "Athens" and a2.getCountry() == "Greece"
t3 = equals("YXU (London, Canada)", a1.__repr__()) and equals("ABC (Athens, Greece)", a2.__repr__())

if t1 and t2 and t3:
    print("Test 1 Passed. (Airport methods)")
else:
    print("Test 1 Failed. (Airport methods)")


# # --------------- Test 2 - Flight methods ---------------
a1 = Airport("YXU", "London", "Canada","North America")
a2 = Airport("ABC", "Athens", "Greece","Europe")
f1 = Flight("ABC123", a1, a2)
f2 = Flight("BCS101", Airport("ABQ", "Albuquerque", "United States","North America"), Airport("OMA", "Omaha", "United States","North America"))
f3 = Flight("XYZ321", a1, a2)
t1 = f1.getFlightNumber() == "ABC123" and f1.getOrigin() == a1 and f1.getDestination() == a2
t2 = f1 != f2 and f1 == f3
t3 = equals("Flight(ABC123): London -> Athens [international]", f1.__repr__()) and equals("Flight(BCS101): Albuquerque -> Omaha [domestic]", f2.__repr__())
t4 = not(f1.isDomesticFlight()) and f2.isDomesticFlight()

if t1 and t2 and t3 and t4:
    print("Test 2 Passed. (Flight methods)")
else:
    print("Test 2 Failed. (Flight methods)")



# # --------------- Test 3 - Exceptions ---------------
a1 = Airport("YXU", "London", "Canada","North America")
a2 = Airport("ABC", "Athens", "Greece","Europe")
t1 = not(avi.loadData("junk.txt", "stuff.txt","random name . nothing"))
t2 = len(avi._allAirports) == 0
t3 = t4 = False
try:
    Flight("PNT175", "Toronto", "New York")
except TypeError as e:
    if e.__str__().strip().lower() == "the origin and destination must be airport objects":
        t3 = True
try:
    t4 = Flight("12#$cv", a1, a2)
except TypeError as e:
    if e.__str__().strip().lower() == "the flight number format is incorrect":
        t4 = True
if t1 and t2 and t3 and t4:
    print("Test 3 Passed. (Exceptions)")
else:
    print("Test 3 Failed. (Exceptions)")


# # --------------- Test 4 - loadData() ---------------

t1 = avi.loadData("airports.txt", flightsFileName, "countries.txt")
total = 0
for i in avi._allFlights:
    total += len(avi._allFlights[i])

if t1 and len(avi._allAirports) == 37 and total == 60:
    print("Test 4 Passed. (loadData())")
else:
    print("Test 4 Failed. (loadData())")


# # --------------- Test 5 - getAirportByCode() ---------------

avi.loadData("airports.txt", flightsFileName, "countries.txt")
t1 = avi.getAirportByCode("ORD")

if isinstance(t1, Airport) and t1.getCity() == "Chicago":
    print("Test 5 Passed. (getAirportByCode())")
else:
    print("Test 5 Failed. (getAirportByCode())")



# # --------------- Test 6 - findAllCityFlights() ---------------

avi.loadData("airports.txt", flightsFileName, "countries.txt")
cf = avi.findAllCityFlights("Toronto")
cfs = ""
for f in cf:
    cfs += f.getFlightNumber() + " "
t1 = isinstance(cf,list) and len(cf) == 6
acodes = ['MCK533','QGC143','KPP582','CUN974','CFE916','AOK874 ']
total = 0
for a in acodes:
    if a in cfs:
        total += 1
t2 = total == 6

if t1 and t2:
    print("Test 6 Passed. (findAllCityFlights())")
else:
    print("Test 6 Failed. (findAllCityFlights())")


# # --------------- Test 7 - findAllCountryFlights() ---------------

avi.loadData("airports.txt", flightsFileName, "countries.txt")
cf = avi.findAllCountryFlights("Brazil")
cfs = ""
for f in cf:
    cfs += f.getFlightNumber() + " "
t1 = isinstance(cf,list) and len(cf) == 4
acodes = ['YZF667','XGY802','MOO674','FFC468 ']
total = 0
for a in acodes:
    if a in cfs:
        total += 1
t2 = total == 4

if t1 and t2:
    print("Test 7 Passed. (findAllCountryFlights())")
else:
    print("Test 7 Failed. (findAllCountryFlights())")


# # --------------- Test 8 - findFlightBetween() ---------------

avi.loadData("airports.txt", flightsFileName, "countries.txt")
f1 = avi.findFlightBetween(avi.getAirportByCode("PVG"), avi.getAirportByCode("YOW"))
f2 = avi.findFlightBetween(avi.getAirportByCode("LAX"), avi.getAirportByCode("DTW"))
t1 = equals(f1, "Direct Flight(MTN376): PVG to YOW")
t2 = f2 == -1

if t1 and t2:
    print("Test 8 Passed. (findFlightBetween())")
else:
    print("Test 8 Failed. (findFlightBetween())")


# # --------------- Test 9 - findFlightBetween() ---------------

avi.loadData("airports.txt", flightsFileName, "countries.txt")
f1 = avi.findFlightBetween(avi.getAirportByCode("LAX"), avi.getAirportByCode("MIA"))
t1 = isinstance(f1, set) and "CPT" in f1

if t1:
    print("Test 9 Passed. (findFlightBetween())")
else:
    print("Test 9 Failed. (findFlightBetween())")



# # --------------- Test 10 - findReturnFlight() ---------------

# LOD619,MEX,LAX
# LOX618,LAX,MEX

# USO770,MEX,CPT
# USO771,CPT,MEX

#EKR896,SFO,YHZ

avi.loadData("airports.txt", flightsFileName, "countries.txt")
f1 = avi.findFlightByNo('LOD619')
f2 = avi.findFlightByNo('USO770')
f3 = avi.findFlightByNo('EKR896')
t1 = avi.findReturnFlight(f1)
t1 = avi.findReturnFlight(t1)
t2 = avi.findReturnFlight(f2)
t2 = avi.findReturnFlight(t2)
t3 = avi.findReturnFlight(f3)

if f1 == t1 and f2 == t2 and t3 == -1:
    print("Test 10 Passed. (findReturnFlight())")
else:
    print("Test 10 Failed. (findReturnFlight())")



# # --------------- Test 11 - findFlightsAcross() ---------------
avi.loadData("airports.txt", flightsFileName, "countries.txt")
res=avi.findFlightsAcross('Atlantic')
if res == {'XJX595', 'LJC201', 'DAJ762', 'MDW532', 'YZF667', 'JAG578', 'JKQ130', 'JHW048', 'YFZ738', 'CUN974', 'NIA196', 'VKG041', 'VIP930', 'YOF338', 'USO770', 'USO771'}:
    print("Test 11 Passed. (findFlightsAcross('Atlantic'))")
else:
    print("Test 11 Failed. (findFlightsAcross('Atlantic'))")

# # --------------- Test 12 - findFlightsAcross() ---------------
# avi.loadData("airports.txt", flightsFileName, "countries.txt")
# res=avi.findFlightsAcross('Pacific')
# if res == {'MTN376', 'QMG091', 'VDT680', 'CSY487', 'YOI104', 'TYV528', 'KPP582', 'CSX772', 'ERO171', 'PGY075', 'YVF322', 'EYS649'}:
#     print("Test 12 Passed. (findFlightsAcross('Pacific'))")
# else:
#     print("Test 12 Failed. (findFlightsAcross('Pacific'))")
