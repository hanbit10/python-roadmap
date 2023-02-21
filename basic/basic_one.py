name = "Beau"; print(name)
age = 39

# 1+1
# "Beau"

print(type(name) == str)
print(isinstance(name, int))
print(isinstance(age, int))

condition1 = True; condition2 = False
val = not condition1 
val2 = condition1 and condition2
val3 = condition1 or condition2
print("This is conditions:"); 
print(val)
print(val2)
print(val3)

def is_adult(age):
  if age >= 18:
    return True
  else:
    return False

def is_adult2(age):
  return True if age >= 18 else False