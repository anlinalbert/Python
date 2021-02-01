# Display tuple value

inpstr = input ("Enter colors seperated by comma : ")
colors = tuple(inpstr.split (","))
print("First color :", colors[0], "\nLast color:", colors[-1])