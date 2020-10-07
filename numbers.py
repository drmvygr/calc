print("...numbers...")
print("dream's first python project")
while True:
  x = input("Please enter a number:")
  try:
    val=float(x)
    break
  except ValueError:
    print("That's not a number!")
while True:
  y = input("Please enter another number:")
  try:
    val=float(y)
    break
  except ValueError:
    print("Are you dumb? I said a NUMBER!")
while True:
  op = input("Please choose an operator (+, -, /, *, **, //, %): ")
  if op in ["+","-","/","*","**","//","%"]:
    break
  else: print("That's not an operator!")
while True:
  try:
    w=eval(f"{x}{op}{y}")
    break
  except ZeroDivisionError:
    print("No.")
    exit()
z=round(w,2)
print(x,op,y,"is",z)
