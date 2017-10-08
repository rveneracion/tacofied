import random

def pickone(listing, num):
    return listing[num % len(listing)]

def taco_bellify(name=None):
    '''
    generates a series of words which sounds like a food item that taco bell would sell 
    (i.e. "Double Chicken Gordilada Presidente")
    '''

    #generate an integer by hashing the name. if no name is given, generate a random number
    if name == None:
        namenum = random.randint(-(2**31),(2**31))
    else:
        namenum = hash(name)

    sizes = ["", "XXL", "Super", "Fiery","Tasty","Double", "Macho"]
    size = pickone(sizes,namenum)

    cheefies = ["Cheesy","Beefy","Chicken","Bean","Cinnamon","Apple","Veggie", "Steak", "Pollo","Guacamole"]
    cheefy = pickone(cheefies, namenum)
    
    pres = ["Tac" ,"Burr" ,"Ques" ,"Gord" ,"Ench" ,"Chim" ,"Emp" ,"Chal" ,"Chil","Crunch","Nach", "Tort", "Tost", "Mex-","Much","Mas"]
    mids = ["it" ,"adill" ,"ilad" ,"ichang" ,"anad" ,"irit" ,"up" ,"adit", "arit", "ador", "amale" ]
    ends = ["a","o"]

    foodita = pickone(pres,namenum) + pickone(mids,namenum) + pickone(ends,namenum)
    foodita = foodita.replace("ci", "qui")
    foodita = foodita.replace ("ce", "que")
    foodita = foodita.replace ("leo", "le")
    foodita = foodita.replace ("lea", "le")

    supremitos = ["", "Supreme", "Crunchwrap", "Belgrande", "Loco", "Presidente", "con Carne", "con Queso"]
    supremito = pickone(supremitos,namenum)
    if supremito == 'Loco' and foodita[-1] == 'a':
            supremito = 'Loca'

    taco_supremo = [size, cheefy, foodita, supremito]
    taco_supremo = [taco for taco in taco_supremo if not taco == ""]

    el_foodo = ' '.join(taco_supremo)

    return el_foodo
