import math
import phys

print()
R = phys.R_k()
M = phys.M_v()
n = 1234567
P = phys.P_atmosphere()

print("Let's determine the pressure of atmosphere and density of air on the ground! ")
print("For example: ")

T = phys.T(0)
p_0 = P * M / (R * T)

print("Pressure of atmosphere:", P, "Pa for temperature: 0°C")
print("Density of air:", p_0, "kg/m³ for temperature: 0°C")
print()

t = float(input("Please set temperature in °C: "))

k = math.fabs(t)
f = t / n
d = 0

print()
while math.fabs(d) < k:
	p = P * M / (R * T)
	i = d + f
	T = phys.T(i)
	P = p * R * T / M
	d = d + f
	i = d + f
	T = phys.T(i)

print("Pressure of atmosphere: ", P, " Pa for temperature: ", t, "°C ;", sep = "")
print("Density of air: ", p, " kg/m³ for temperature: ", t, "°C .", sep = "")
print()
print("Let's determine the pressure of atmosphere and density of air at height above sea level!")
h = float(input("Please set height: "))
print()

n = 1234567
l = h / n 
T = phys.T(t)
P1 = P
p1 = p
d1 = 0

while d1 < h:
	if phys.t(T) > -270.5:
		T = phys.T_h(T, l)
	g = phys.a_(phys.M(), phys.R(), d1)
	d_P = -(p1 * g * l)
	P1 = P1 + d_P
	p1 = P1 * M / (R * T)
	d1 = d1 + l

t = phys.t(T)

print("Temperature: ", t, "°C", sep = "")
print("Pressure of air:", P1, "Pa")
print("Density of air:", p1, "kg/m³")
print("Gravity acceleration", g, "m/s²")
print()
