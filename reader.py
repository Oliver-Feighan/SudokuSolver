def reader(bash_input):
	
	lines = []

	for line in open(bash_input):

		line = line.replace(".", " ").replace("/", " ").split()
		line = list(line[0])

		if line:
			lines.append(line)

	return(lines)