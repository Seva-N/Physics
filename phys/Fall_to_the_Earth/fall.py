import math
import phys
print()
print("The body flies to the Earth and fall in.")
print("Please enter the values of its starting state to calculate its further movement:")
print()
h = int(input("Height: "))
v = int(input("Starting speed: "))
t = int(input("Time: "))
n = int(input("Processing threshold: "))

H = h
v1 = v

M = phys.M()
R = phys.R()
r = R
f = t / n
d = 0
q = 0
S = 0
T = 0

V = 4 / 3 * math.pi * R ** 3
p = M / V

while d < t:
	R = r + h
	a = phys.a(M, R)
	h = h + v * f - a * f ** 2 / 2
	v = v - a * f

	if h <= 0:
		V = 4 / 3 * math.pi * R ** 3
		M = p * V
		S = S + math.fabs(v * f - a * f ** 2 / 2)

		if S < r:
			T = T + f
		if R < 0:
			R = -R
			h = -(r - R)
			v = -v

	d = d + f
	q = q + phys.l_relat(f, v)
	
print()
print("The body will be on the height:", int(h), "m")
if h < 0:
	print("The body will be on distance to the center:", R, "m")
print("The body will have speed:", v, "m/s")
print("The body will have acceleration:", a, "m/s²")
print("Time of fall of body to the center of the Earth:", T, "s")
print("The past time around:", q, "s")
print()

z = input("Do you calculate the motion in steps? ")
print()

if z == "Yes" or z == "yes" or z == "YES":

	i = int(input("Please set step in seconds: "))

	print()

	M1 = phys.M()
	R1 = phys.R()
	r = R1
	U = t + 1
	d = 0

	for t1 in range (0, U, i):
		a1 = phys.a(M1, R1)
		V1 = 4 / 3 * math.pi * R1 ** 3
		p1 = M1 / V1
		f = t1 / n
		while d < t1:
			R1 = r + H
			a1 = phys.a(M1, R1)
			H = H + v1 * f - a1 * f ** 2 / 2
			v1 = v1 - a1 * f

			if H < 0:
				V1 = 4 / 3 * math.pi * R1 ** 3
				M1 = p1 * V1

				if R1 < 0:
					R1 = -R1
					H = -(r - R1)
					v1 = -v1
					
			d = d + f

		print(t1, " second:")
		print("Height:", int(H), "m")
		if H < 0:
			print("Distance to the center:", R1, "m")
		print("Speed:", v1, "m/s")
		print("Acceleration:", a1, "m/s²")
		print()

elif z == "No" or z == "no" or z == "NO":
	print("Ok")

	print()
