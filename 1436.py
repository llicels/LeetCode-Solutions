def destination(paths):
	for i in range (len(paths)):
		current = paths[i][1]
		destination = current
		for j in range (len(paths)):
			if (current == paths[j][0]):
				destination = ""
		if (destination != ""):
			return (destination)

city = destination([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])
print(city)