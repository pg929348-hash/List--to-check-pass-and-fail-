count=0  
total=0
passes=0          
marks = [45, 22, 67, 33, 90, 12, 78]
for i in marks:
         count+=1
         total+=i
         if i>=33:
             passes+=1
             print(f"pass{i}")
         else:
             print(f"fail{i}")

     
          
average=round(total/count,2)
print(f"pass:-{passes}")   
print(f"your average:-{average}")
