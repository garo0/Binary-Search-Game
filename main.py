import time
import sys

print("From which to which number do you want the list to be")

try:
	s, e = int(input("From: ")), int(input("To: "))
except ValueError:
	print("Number must be type: int")
	sys.exit()

if s > e:
	print("Cannot generate list: s > e")


l = list(range(s,e+1))

print(f"Which number would you like to serach from {s} to {e}")
try:
	n = int(input("Number: "))
except ValueError:
	print("Number must be type: int")

index = 0
t = time.time()
while len(l) != 1:
	length = len(l)
	half = len(l)//2
	if n in l[:half]:
		l = l[:half]
	else:
		index = index + half
		l = l[half:]

dt = time.time()-t

print(f"Your number is in the index: {index}")
print(f"Operation took: {dt}s")
