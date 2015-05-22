# Enumerate similar function
# Marco Botros

def enumerate2(list):
	for i in range(len(list)):
		yield (i,list[i])

StuList = ["stu","rebecca","jess"]
for i,v in enumerate2(StuList):
	print(i,v)
