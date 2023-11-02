# initializing list
test_list = ["all", "love", "and", "get", "educated", "by", "gfg"]


print("The original list is : " + str(test_list))

res = []
vow = "aeiou"
for sub in test_list:
	flag = False
	

	for ele in vow:
		if sub.startswith(ele):
			flag = True
			break
	if flag:
		res.append(sub)

print("The extracted words : " + str(res))
