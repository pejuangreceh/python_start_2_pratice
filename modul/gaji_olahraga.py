def dapat_penuh_waktu(pengalaman):
   gaji = 20000
   if pengalaman >= 3 and pengalaman < 5:
       k = 1.5
   elif pengalaman >= 5 and pengalaman < 7:
       k = 2
   elif pengalaman >= 7:
       k = 3
   else:
       k = 1
   gaji *= k
   return gaji
 
def dapat_paruh_waktu(jam):
   per_jam = 800
   gaji = jam*per_jam
   return gaji
