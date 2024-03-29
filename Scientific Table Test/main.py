from random import choice
global elements
elements = {"Ac":"Actinium","Ag":"Silver","Al":"Aluminum","Am":"Americium",
"Ar":"Argon","As":"Arsenic","At":"Astatine","Au":"Gold","B":"Boron","Ba":"Barium",
"Be":"Beryllium","Bh":"Bohrium","Bi":"Bismuth","Bk":"Berkelium","Br":"Bromine",
"C":"Carbon","Ca":"Calcium","Cd":"Cadmium","Ce":"Cerium","Cf":"Californium",
"Cl":"Chlorine","Cm":"Curium","Cn":"Copernicium","Co":"Cobalt","Cr":"Chromium",
"Cs":"Cesium","Cu":"Copper","Db":"Dubnium","Ds":"Darmstadtium","Dy":"Dysprosium",
"Er":"Erbium","Es":"Einsteinium","Eu":"Europium","F":"Fluorine","Fe":"Iron",
"Fl":"Flerovium","Fm":"Fermium","Fr":"Francium","Ga":"Gallium","Gd":"Gadolinium",
"Ge":"Germanium","H":"Hydrogen","He":"Helium","Hf":"Hafnium","Hg":"Mercury",
"Ho":"Holmium","Hs":"Hassium","I":"Iodine","In":"Indium","Ir":"Iridium",
"K":"Potassium","Kr":"Krypton","La":"Lanthanum","Li":"Lithium","Lr":"Lawrencium",
"Lu":"Lutetium","Lv":"Livermorium","Mc":"Moscovium","Md":"Mendelevium",
"Mg":"Magnesium","Mn":"Manganese","Mo":"Molybdenum","Mt":"Meitnerium",
"N":"Nitrogen","Na":"Sodium","Nb":"Niobium","Nd":"Neodymium","Ne":"Neon",
"Nh":"Nihonium","Ni":"Nickel","No":"Nobelium","Np":"Neptunium","O":"Oxygen",
"Og":"Oganesson","Os":"Osmium","P":"Phosphorus","Pa":"Protactinium","Pb":"Lead",
"Pd":"Palladium","Pm":"Promethium","Po":"Polonium","Pr":"Praseodymium",
"Pt":"Platinum","Pu":"Plutonium","Ra":"Radium","Rb":"Rubidium","Re":"Rhenium",
"Rf":"Rutherfordium","Rg":"Roentgenium","Rh":"Rhodium","Rn":"Radon",
"Ru":"Ruthenium","S":"Sulfur","Sb":"Antimony","Sc":"Scandium","Se":"Selenium",
"Sg":"Seaborgium","Si":"Silicon","Sm":"Samarium","Sn":"Tin","Sr":"Strontium",
"Ta":"Tantalum","Tb":"Terbium","Tc":"Technetium","Te":"Tellurium","Th":"Thorium",
"Ti":"Titanium","Tl":"Thallium","Tm":"Thulium","Ts":"Tennessine","U":"Uranium",
"V":"Vanadium","W":"Tungsten","Xe":"Xenon","Y":"Yttrium","Yb":"Ytterbium",
"Zn":"Zinc","Zr":"Zirconium"}


def getKey(val):
   for key, value in elements.items():
      if val == value:
         return key

def askQuestion(element, answer):
    response = input('What is the symbol for the element: '+ element + '? ')
    if response == answer:
        print('Correct!')
        return True
    else:
        print('Sorry! You got it incorrect :(')
        print('The correct answer was:', answer)

def main():
    global score
    score = 0
    for i in range(10):
        element = choice(list(elements.values()))
        print('Score:', score)
        answer = getKey(element)
        print(answer)
        q = askQuestion(element, answer)
        if q:
            score += 2
        
    print('Final Score: ' + str(score)+ '/20')
main()