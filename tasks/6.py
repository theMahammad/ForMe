# Verilən cümlənin icərisində olan saitlərin sayını tapan proqram yazın
sait=['a','i','o','u','e',"ə",]
cumle='Salam necesen ,yaxsisan?'
cumle2=cumle.lower()
say=0
for i in cumle2:
    for j in sait:
        if i==j:
            say+=1
            print(i,end=" ")
            print(say)