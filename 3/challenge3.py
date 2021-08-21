def getval(obj,key):
  """
  this function takes the object which is a nested dictionary(obj) and list of keys (key) as input
  and returns the value (obj1) as output.
  """
    
   obj1=obj
   keys=key.split('/')
   
   for item in keys:
      obj1=obj1[item]
   return obj1


obj={'a':{'b':{'c':'d'}}}
key ="a/b/c"

val=getval(obj,key)

print(val)