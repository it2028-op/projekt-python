import  physics

def a(m):
    '''
    Tato funkce vypočítá jakou silou vás přitahuje Země a jakou by vás přitahoval Měsíc.
    '''
    return m * physics.EARTH_GRAVITY

def b(m):
    return m * physics.MOON_GRAVITY

def c():
    '''
    Tato funkce vypočítá rozdíl rychlosti zvuku a světla a jakou energii by jste potřebovali k dosažení rychlosti zvuku.
    '''
    return physics.SPEED_OF_LIGHT / physics.SPEED_OF_SOUND

print(a.__doc__)
vaha = int(input("Zadejte prosím vaši hmotnost v celých kg: "))
print('Na Zemi jste přitahováni silou', round(a(vaha),2), 'N')
print('Na Měsíci by jste byli přitahováni silou', round(b(vaha),2), 'N, neboli asi', round(a(vaha)/b(vaha), 0), 'krát méně.')
print('Rychlost světla je', round(physics.SPEED_OF_LIGHT / physics.SPEED_OF_SOUND,1), 'krát větší než rychlost zvuku, takže se rovná', round(physics.SPEED_OF_LIGHT / physics.SPEED_OF_SOUND,0), 'Mach')
