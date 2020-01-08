a=20         #assigning the value of 20 to a
b=3

print(a+b)   # a add b
print(a-b)   # a minus b
print(a*b)   # a muptipy b
print(a/b)   # a divided by b
print(a**b)  # raise a to the power of b
print(a//b)  # floor division , only the integer part remains
print(a%b)   # modulus
a+=b         # assign the value of a+b to a,also a-=b,a*=b,a/=b,a**/b,a//=b,a%%=b
a=10
b=20
a,b=100,200
a,b=b,a      # They happens at the same time , a is still 100 when the next assigning took place
