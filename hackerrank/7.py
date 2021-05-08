link[https://www.hackerrank.com/challenges/py-if-else/problem]
n = input('Bir eded daxil edin :')
n=int(n)
if n%2==0 and n>0:
    if n in range(2,5):
        print('Not Weird')
    if n in range(6,20):
        print ('Weird') 
    else:
        print('Not Weird') 
else:
    print('Weird')              