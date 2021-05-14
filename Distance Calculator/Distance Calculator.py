#www.101computing.net/stopping-distance-calculator/

mu = 0.7 # Friction Coefficient
tr = 1.5 # Response Time
g = 9.81 # Gravity
road = 'w'
if road == 'w':
    mu = 0.5
elif road == 'i':
    mu = 0.3

mph = float(input('Enter the speed of the vehicle in MPH: '))
mps = mph/2.237

RD = mps * tr
BD = (mps**2)/(2 * mu * g)

SD = RD + BD

print('Stopping distance:', SD, 'meters')