import math
import phys

print()
print("Fall to the Earth 2")
print("The body flies to the Earth and fall in.")
print("Please enter the values of its starting state to calculate its further movement:")
print()
h = int(input("Height, m: "))
v = int(input("Starting speed, m/s: "))
t = int(input("Time, s: "))
n = 10000
w = input("Consider air resistance? ")

if w == "YES" or w == "Yes" or w == "yes":
	C = phys.C_sphere()
	print()
	V_s = float(input("Please set the body volume: "))

	R_s = (V_s / math.pi * 3 / 4) ** (1 / 3)
	s = math.pi * R_s ** 2

	m = float(input("Please set the mass of body, kg: "))
	t_q = float(input("Please set the temperature on the ground, °C : "))
	t_q1 = t_q

print()

H = h
v1 = v

M_v = phys.M_v()
R_k = phys.R_k()

M = phys.M()
R = phys.R()
r = R
f1 = t / n

d = 0
q = 0
S = 0
T = 0

if w == "YES" or w == "Yes" or w == "yes":
	mt_q = math.fabs(t_q)
	dt_q = t_q / n

	P = phys.P_atmosphere()
	T_q = phys.T(0)
	d_q = 0

	while math.fabs(d_q) < mt_q:
		p_q = P * M_v / (R_k * T_q)
		i = d_q + dt_q
		T_q = phys.T(i)
		P = p_q * R_k * T_q / M_v
		d_q = d_q + dt_q
		i = d_q + dt_q
		T_q = phys.T(i)

	P1 = P
	p_q1 = p_q

V = 4 / 3 * math.pi * R ** 3
p = M / V

while d < t:
	R = r + h

	f = phys.l_relat(f1, v)

	if w == "YES" or w == "Yes" or w == "yes":

		l = h / n
		T_q = phys.T(t_q1)
		P = P1
		p_q = p_q1
		d_q = 0

		while math.fabs(d_q) < math.fabs(h):
			if phys.t(T_q) > -270.5:
				T_q = phys.T_h(T_q, l)

			g = phys.a_(M, r, d_q)
			d_P = -(p_q * g * l)

			if h >= 0:
				P = P + d_P

			p_q = P * M_v / (R_k * T_q)
			d_q = d_q + l

		t_q = phys.t(T_q)
		P_ = P
		k = phys.k_r(p_q, C, s)
		da = phys.F_r2(k, v) / m

		g = phys.a(M, R)
		F = phys.F_a_(p_q, V_s, g) / m

	else:
		da = 0
		F = 0

	a = phys.a(M, R) - F - da

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
			h = R - r
			v = -v

	d = d + f1
	q = q + f

print("The body will be on the height:", h, "m")
if h < 0:
	print("The body will be on distance to the center:", R, "m")

print("The body will have speed:", v, "m/s")
print("The body will have acceleration:", a, "m/s²")

if h < 0:
	print("Time of fall of body to the center of the Earth:", T, "s")

if w == "YES" or w == "Yes" or w == "yes":
	print()
	print("Temperature around: ", t_q, "°C", sep = "")
	print("Pressure of atmosphere: ", P, "Pa")
	print("Density of air:", p_q, "kg/m³")

print("")
print("The past time around:", q, "s")
print()

z = input("Do you calculate the motion in steps? ")
print()

if z == "Yes" or z == "yes" or z == "YES":

	I = int(input("Please set step in seconds: "))

	print()

	M1 = phys.M()
	R1 = phys.R()
	r = R1

	U = t + 1
	d = 0

	if w == "YES" or w == "Yes" or w == "yes":
		p_q_ = p_q1
		T_q_ = phys.T(t_q1)

		l = H / n
		
		P_ = P1
		p_q_ = p_q1
		t_q_ = t_q1
		T_q_ = phys.T(t_q1)
		d_q = 0

		while math.fabs(d_q) < math.fabs(H):
				
			if phys.t(T_q_) > -270.5:
				T_q_ = phys.T_h(T_q_, l)

			g = phys.a_(M, r, d_q)
			d_P = -(p_q_ * g * l)

			if H >= 0:
				P_ = P_ + d_P

			p_q_ = P_ * M_v / (R_k * T_q_)
			d_q = d_q + l

		t_q_ = phys.t(T_q_)

		k = phys.k_r(p_q_, C, s)
		da = phys.F_r2(k, v1) / m

		g = phys.a(M1, R1)
		F = phys.F_a_(p_q_, V_s, g) / m

	else:
		F = 0
		da = 0

	a1 = phys.a(M1, R1) - F - da

	for t1 in range (0, U, I):
		a1 = phys.a(M1, r + H)
		V1 = 4 / 3 * math.pi * R1 ** 3
		p1 = M1 / V1
		f1 = t1 / n

		while d < t1:

			R1 = r + H

			f = phys.l_relat(f1, v1)

			if w == "YES" or w == "Yes" or w == "yes":

				l = H / n
				d_q = 0
				P_ = P1
				p_q_ = p_q1
				t_q_ = t_q1
				T_q_ = phys.T(t_q1)

				while math.fabs(d_q) < math.fabs(H):
				
					if phys.t(T_q_) > -270.5:
						T_q_ = phys.T_h(T_q_, l)

					g = phys.a_(M, r, d_q)
					d_P = -(p_q_ * g * l)

					if H >= 0:
						P_ = P_ + d_P

					p_q_ = P_ * M_v / (R_k * T_q_)
					d_q = d_q + l

				t_q_ = phys.t(T_q_)

				k = phys.k_r(p_q_, C, s)
				da = phys.F_r2(k, v1) / m

				g = phys.a(M1, R1)
				F = phys.F_a_(p_q_, V_s, g) / m

			else:
				F = 0
				da = 0

			a1 = phys.a(M1, R1) - F - da

			H = H + v1 * f - a1 * f ** 2 / 2
			v1 = v1 - a1 * f

			if H <= 0:
				V1 = 4 / 3 * math.pi * R1 ** 3
				M1 = p1 * V1

				if R1 < 0:
					R1 = -R1
					H = R1 - r
					v1 = -v1
					
			d = d + f1

		print(t1,"second:")
		print("Height:", H, "m")
		if H < 0:
			print("Distance to the center:", R1, "m")
		print("Speed:", v1, "m/s")
		print("Acceleration:", a1, "m/s²")

		if w == "YES" or w == "Yes" or w == "yes":
			print()
			print("Temperature around: ", t_q_, "°C", sep = "")
			print("Pressure of atmosphere: ", P_, "Pa")
			print("Density of air:", p_q_, "kg/m³")
		print()

elif z == "No" or z == "no" or z == "NO":
	print("Ok")

	print()
