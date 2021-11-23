# Define a funtion "simple_interest" to calculate simple interest given principal amount(p), rate of interest(r) and time(t)
# SI = (P*T*R)/100
def simple_interest(p,t,r):
  si = (p*t*r)/100
  return si

# Call the function "simple_interest()" and print the result
si = simple_interest(3000,5,2)
print(si)