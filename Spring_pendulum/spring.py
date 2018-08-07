import math
import phys as p

print()

print("Movement of the body under the action of a spring: ")
k = int(input("Coefficient of elasticity: "))
m = int(input("Mass: "))
x = int(input("Initial coordinate: "))
v = int(input("Starting speed: "))
t = int(input("Time: "))
n = int(input("Processing threshold:  "))

X = x
V = v

f = t / n
l = x
S = 0
d = 0
r = x

while d < t :
	a = (-k / m) * x
	x = x + v * f
	v = v + a * f
	d = d + f

	S = S + math.fabs(v * f)

	if math.fabs(r) > math.fabs(x) :
		A = math.fabs(r)
	else:
		r = x

print()

q = math.fabs(x - l)
p = S / (4 * A)
T = t / p
q = str(int(q)) + "." + str (int(q * 1000 % 1000))
x = str(int(x)) + "." + str (int(x * 1000 % 1000))
v = str(int(v)) + "." + str (int(v * 1000 % 1000))
a = str(int(a)) + "." + str (int(a * 1000 % 1000))
A = str(int(A)) + "." + str (int(A * 1000 % 1000))
T = str(int(T)) + "." + str (int(T * 1000 % 1000))

print("The body will be on the coordinate", x, "m ;")
print("The body will pass the distance", q, "m ;")
print("The body will have a finite speed", v, "m/s ;")
print("The body will have finite acceleration", a, "m/s² ;")
print()
print("The body undergoes mechanical oscillations of a spring pendulum:")
print("The amplitude of the oscillations is", A, "м ;")
print("The period of oscillation is", T, "c .")
print()

z = input("Do you calculate the motion in steps? ")
print()

if z == "YES" or z == "Yes" or z == "yes" :

	i = int(input("Please set step in seconds: "))

	print()

	U = t + 1
	d = 0

	for t1 in range (0, U, i):
		
		a1 = (-k / m) * X
		f = t1 / n
		L = X

		while d < t1 :
			a1 = (-k / m) * X
			X = X + V * f
			V = V + a1 * f
			d = d + f

		q1 = math.fabs(X - L)
		q2 = str(int(q1)) + "." + str(int(q1 * 1000 % 1000))	
		X2 = str(int(X)) + "." + str (int(X * 1000 % 1000))	
		V2 = str(int(V)) + "." + str (int(V * 1000 % 1000))
		a2 = str(int(a1)) + "." + str (int(a1 * 1000 % 1000))

		print(t1, " second :", sep = "")
		print("The body will be on the coordinate", X2, "м ;")
		print("The body will pass the distance", q2, "м ;")
		print("The body will have a speed", V2, "м/с ;")
		print("The body will have acceleration", a2, "м/с² .")
		print()

elif z == "NO" or z == "No" or z == "no":
	print("Ok")
	print()