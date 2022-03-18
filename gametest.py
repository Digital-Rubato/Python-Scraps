class Base:
	
	print("This is the base tile")
	theinput = input("Where to go?")
	if theinput == Map.maps:

		return theinput
	else:
		None
	

class Map:
	maps = {
		'base': Base(),
		'forest': Forest(),
		'bossroom': Boss_Room(),
		'shop': Shop()
		}

instance = Base()
instance()