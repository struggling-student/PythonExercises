
def es2(ls,ftesto):
   with open(ftesto, 'r') as f:
      strTesto = f.read()
   strTesto = strTesto.replace(',', " ")
   lstStr = strTesto.split()
   count = 0
   for i in range(len(lstStr)-1):
      if((lstStr[i]+lstStr[i+1]) in ls):
         ls.remove(lstStr[i]+lstStr[i+1])
         count += 1
   return count
