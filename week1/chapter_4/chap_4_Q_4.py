
test_str = 'Text For TeSt'

print("The original string is : " + str(test_str))

res = [idx for idx in range(len(test_str)) if test_str[idx].isupper()]

print("Uppercase elements indices : " + str(res)) 
