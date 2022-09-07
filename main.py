num = int(input("write number "))
sum = 0
if 100<num<1000:
     pass
while(num != 0):

      sum = sum + num % 10
      num = num // 10
print('suma is ', sum)
