s=lambda x: ''if not x else str(x%10)+'\n'+s(x//10)
print(s(2456))