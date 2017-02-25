numbers=raw_input()
numbers=list(numbers)
print "arxiko noumero tou xrhsth : ", numbers
for i in range(0,len(numbers)):
     if(i<len(numbers)):
       if(numbers[i]=='0'):
         numbers.remove('0')
         numbers.append('0')
print "tropopoihmeno noumero : ",numbers
