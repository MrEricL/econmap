import csv

def data_exist(data):
	l = []
	year = 1960
	for i in range(4,58):
		if not data[i]== "":
			l.append(year+i-4)
			l.append(round(float(data[i]),2))
	return l


def parse_data(t):
	ret = []

	if t == "unemp":
		f = open('unemp.csv', 'rb')
	elif t == "gdp":
		f = open('gdp.csv', 'rb')
	elif t == "gdppc":
		f = open('gdppc.csv', 'rb')
	else:
		print "Can't parse"
		return

	reader = csv.reader(f)
	for row in reader:
		tempd = {}
		tempd['name'] = row[0]
		tempd['code'] = row[1]
		tempd['data'] = data_exist(row)
		ret.append(tempd)
	f.close()

unemp = parse_data('unemp')
gdp = parse_data('gdp')
gdppc = parse_data('gdppc')