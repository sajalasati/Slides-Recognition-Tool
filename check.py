fo = open('results.txt','r')
line = fo.readline()
c1,c2 = 0,0
print("Wrong ones:")
while len(line) > 0:
	line = line.split(' ')
	aa,bb = line[0], line[1]
	a = aa.split('.')[0]
	a = a.split('_')

	b = bb.split('.')[0]
	b = b.split('_')[0:2]
	if a[0] == b[0] and a[1]==b[1]:
		c1 += 1
	else:
		c2 += 1
		print(aa,bb)
	line = fo.readline()
print("correct images:",c1)
print("wrong images:",c2)
print("total images:",c2+c1)
print("accuracy=",(c1/(c1+c2))*100)