import math

def help():
    print("Dear Guest!")
    print("Welcome to the physics module _Phys_ !")
    print("My name is Seva Naumov. Program is made by me.")
    print(" You can find a lot of physical \
constans or calculate some physical values.")
    print("So you can find some astronomical data about our planet, \
solar system, and our galaxy.")
    print()
    print("You could enter : phys.[q_data]() ")
    print("[q] is physical quantity or unit (in other case).")
    print("[q] could be m, ma, f, P, p, G, F, g, a, M, R, r, c, ")
    print("R_black_hole (R_bh), astro_unit (au), light_year (ly), parsec (pc) and")
    print("relativity (l_relat).") 
    print("In Astronomical part:")
    print("[M] is mass of astronomical object")
    print("[R] is radius of astronomical object")
    print("[r] is radius of the orbit of astronomical object")
    print("[data] is some object and can be constant value:")
    print()
    print("density of some bodies")
    print("moon")
    print("sun")
    print("mercury")
    print("venus")
    print("earth")
    print("mars")
    print("jupiter")
    print("saturn")
    print("uranus")
    print("neptune")
    print("pluto")
    print("charon")
    print("galaxy_milky_way (gMW)")
    print("supermassive_black_hole (sbh)")
    print()
    print("If you want to calculate some values, you can use without [data].")
    print("But _ should to be certainly in that case.")
    print("It should be that : phys.[q_]")
    print("Function without _  give you only constants M, R and r,")
    print("which determines the parameters of the Earth  ")
    print("(it's mass, radiuses of it and orbit)")
    print()
    print("Good luck!")



# Mechanics:~


    
# Newton's mechanics:


def ma(m, a):
    ma = m * a
    return ma

def f(m, a):
    f = m * a
    return f

def a_f(f, m): #~
    a_f = f / m
    return a_f


# easy physics:


def m(p, V):
    m = p * V
    return m

def P(F, S):
    p = F / S
    return p


def P_fluid(p, h): #~
    g = 9.80665
    p_fluid = p * g * h
    return p_fluid

def P_f(p, h): #~
    g = 9.80665
    p_f = p * g * h
    return p_f


def P_fluid_(p, h, g): #~
    P_fluid_ = p * g * h
    return P_fluid_

def P_f_(p, h, g): #~
    P_f_ = p * g * h
    return P_f_


def P_atmosphere(): #~ for 273 K
    P_atmosphere = 101325
    return P_atmosphere


def F_a(p, V): #~
    g = 9.80665
    F_a = p * g * V
    return F_a

def F_a_(p, V, g): #~
    F_a_ = p * g * V
    return F_a_


# Object Density (p ; kg/m³): ~


def p_air():
    p_air = 1.225
    return p_air

def p_aqua(): #~
    p_aqua = 999.841
    return p_aqua

def p_water():
    p_water = 1030
    return p_water

def p_ice():
    p_ice = 917
    return p_ice

def p_oak():
    p_oak = 700
    return p_oak

def p_milk():
    p_milk = 1030
    return p_milk

def p_honey():
    p_honey = 1350
    return p_honey

def p_oil_sunflower():
    p_oil_sunflower = 930
    return p_oil_sunflower

def p_oil_engine():
    p_oil_engine = 900
    return p_oil_engine

def p_sulfuric_acid():
    p_sulfuric_acid = 1800
    return p_sulfuric_acid

def p_quicksilver():
    p_quicksilver = 13600
    return p_quicksilver

def p_kerosene():
    p_kerosene = 2700
    return p_kerosene

def p_alcohol():
    p_alcohol = 2500
    return p_alcohol

def p_oil():
    p_oil = 2300
    return p_oil

def p_acetone():
    p_acetone = 2300
    return p_acetone

def p_ester():
    p_ester = 1800
    return p_ester

def p_gasoline():
    p_gasoline = 1600
    return p_gasoline

def p_aluminum():
    p_aluminium = 2700
    return p_aluminium

def p_cast_iron():
    p_cast_iron = 7000
    return cast_iron

def p_zinc():
    p_zinc = 7100
    return p_zinc

def p_tin():
    p_tin = 7300
    return p_tin

def p_steel():
    p_steel = 7800
    return p_steel

def p_iron():
    p_iron = 7800
    return p_iron

def p_copper():
    p_copper = 8900
    return p_copper

def p_silver():
    p_silver = 10500
    return p_silver

def p_lead():
    p_lead = 11300
    return p_lead

def p_gold():
    p_gold = 19300
    return p_gold

def p_platinum():
    p_platinum = 21500
    return p_platinum

def p_sun():
    p_sun = 3300
    return p_sun

def p_earth():
    p_earth = 5520
    return p_earth

def p_blood():
    p_blood = 1050
    return p_blood

def p_human():
    p_human = 1036
    return p_human


# Elastic force: ~


def F_e(k, x):
    F_e = -k * x
    return F_e


# Friction force (max): ~


def F_f(n, N):
    F_f = n * N
    return F_f

def N(m):
    g = 9.80665
    N = m * g
    return N

def N_(m, b):
    g = 9.80665
    N_ = m * g * math.cos(math.radians(b))
    return N_


def _N(m, g):
    _N = m * g
    return _N

def _N_(m, g, b):
    _N_ = m * g * math.cos(math.radians(b))
    return _N_


def a_f(F, m, n):
    g = 9.80665
    a_f = F / m - n * g
    return a_f

def a_f_(n, b):
    g = 9.80665
    if math.tan(math.radians(b)) > n:
        a_f_ = g * (math.sin(math.radians(b)) - n * math.cos(math.radians(b)))
    else:
        a_f_ = 0
    return a_f_

def a_f_F(F, m, n, b):
    g = 9.8066
    if F / m + g * math.sin(math.radians(b)) > g * n * math.cos(math.radians(b)):
        a_f_F = F / m + g * (math.sin(math.radians(b)) - n * math.cos(math.radians(b)))
    else:
        a_f_F = 0
    return a_f_F


def _a_f(F, m, n, g):
    _a_f = F / m - n * g
    return _a_f

def _a_f_(n, b, g):
    if math.tan(math.radians(b)) > n:
        _a_f_ = g * (math.sin(math.radians(b)) - n * math.cos(math.radians(b)))
    else:
        _a_f_ = 0
    return _a_f_

def _a_f_F(F, m, n, b, g):
    if F / m + g * math.sin(math.radians(b)) > g * n * math.cos(math.radians(b)):
        _a_f_F = F / m + g * (math.sin(math.radians(b)) - n * math.cos(math.radians(b)))
    else:
        a_f_F = 0
    return a_f_F


# Resistance force ~


# for low speed: ~

def F_r1(k, v):
    F_r1 = -k * v
    return F_r1

# for high speed: ~

def F_r2(k, v):
    F_r2 = -k * v * math.fabs(v)

# coefficient of resistance: ~

def k_r(p, C, S):
    k_r = p * C * S / 2
    return k_r

# C of resistance: ~

def C_parachute():
    C_parachute = 1.17
    return C_parachute

def C_cube():
    C_cube = 1.05
    return C_cube

def C_cylinder():
    C_cylinder = 0.82
    return C_cylinder

def C_sphere():
    C_sphere = 0.47
    return C_sphere

def C_hemisphere():
    C_hemisphere = 0.4
    return C_hemisphere

def C_teardrop():
    C_teardrop = 0.04
    return C_teardrop



# Astronimical Mechanics:~



# Gravity force: ~


def G():
    G = 6.6740831 * 10 ** -11
    return G

def F(m, M, R):
    G = 6.6740831 * 10 ** -11
    F = G * m * M / R ** 2
    return F

def F_(m, M, R, h): #~
    G = 6.6740831 * 10 ** -11
    F_ = G * m * M / (R + h) ** 2
    return F_

def g(): #~
    g = 9.80665
    return g

def a(M, R):
    G = 6.6740831 * 10 ** -11
    a = G * M / R ** 2
    return a

def a_(M, R, h): #~
    G = 6.6740831 * 10 ** -11
    a_ = G * M / (R + h) ** 2
    return a_


# masses of the astronomic objects ( M ; kg ):


# our planet (Earth):

def M():
    M = 5.97 * 10 ** 24
    return M

# search:

def M_(a, R):
    G = 6.6740831 * 10 ** -11
    M_= a * R ** 2 / G
    return M_

# Moon:

def M_moon():
    M_moon = 7.35 * 10 ** 22
    return M_moon

# Sun:

def M_sun():
    M_sun = 1.9885 * 10 ** 30
    return M_sun

# planets in our solar system:

def M_mercury():
    M_mercury = 3.33 * 10 ** 23
    return M_mercury

def M_venus():
    M_venus = 4.87 * 10 ** 24
    return M_venus

def M_earth():
    M_earth = 5.97 * 10 ** 24
    return M_earth

def M_mars():
    M_mars = 6.4185 * 10 ** 23
    return M_mars

def M_jupiter():
    M_jupiter = 1.9 * 10 ** 27
    return M_jupiter

def M_saturn():
    M_saturn = 5.68 * 10 ** 26
    return M_saturn

def M_uranus():
    M_uranus = 8.68 * 10 ** 25
    return M_uranus

def M_neptune():
    M_neptune = 1.02 * 10 ** 26
    return M_neptune

def M_pluto():
    M_pluto = 1.303 * 10 ** 22
    return M_pluto

# Pluto satellites:

def M_charon():
    M_charon = 1.52 * 10 ** 21
    return M_charon

# galaxy Milky Way:

def M_galaxy_milky_way():
    M_sun = 1.9885 * 10 ** 30
    R_galaxy_milky_way = 4.8 * 10 ** 11 * R_sun
    return R_galaxy_milky_way

def M_gMW():
    M_sun = 1.9885 * 10 ** 30
    M_gMW = 4.8 * 10 ** 11 * R_sun
    return M_gMW

# Supermassive black hole

def M_supermassive_black_hole():
    M_supermassive_black_hole = 1.7449856116 * 10 ** 41
    return M_supermassive_black_hole

def M_sbh():
    M_sbh = 1.7449856116 * 10 ** 41
    return M_sbh


# radiuses of the astronomic objects ( R ; m ):


# our planet (Earth):

def R():
    R = 6356863
    return R

# equator of the Earth: ~

def R_equator():
    R_eguator = 6378100
    return R_eguator

def R_e():
    R_e = 6378100
    return R_e

# pole of the Earth: ~

def R_pole():
    R_pole = 6356777
    return R_pole

def R_p():
    R_p = 6356777
    return R_p

# search:

def R_(M, a):
    G = 6.6740831 * 10 ** -11
    R_ = (G * M / a) ** (1/2)
    return R_

# Moon:

def R_moon():
    R_moon = 1737100
    return R_moon

# Sun:

def R_sun():
    R_sun = 6.96 * 10 ** 8
    return R_sun

# planets in our solar system:

def R_mercury():
    R_mercury = 2439700
    return R_mercury

def R_venus():
    R_venus = 6051800
    return R_venus

def R_earth():
    R_earth = 6356863
    return R_earth

def R_mars():
    R_mars = 3389500
    return R_mars

def R_jupiter():
    R_jupiter = 69911000
    return R_jupiter

def R_saturn():
    R_saturn = 58232000
    return R_saturn

def R_uranus():
    R_uranus = 25360000
    return R_uranus

def R_neptune():
    R_neptune = 24622000
    return R_neptune

def R_pluto():
    R_pluto = 5900000
    return R_pluto

# Pluto satellites:

def R_charon():
    R_charon = 606000
    return R_charon

# galaxy Milky Way:

def R_galaxy_milky_way():
    light_year = 299792458 * 60 * 60 * 24 * 365
    R_galaxy_milky_way = 50000 * light_year
    return R_galaxy_milky_way

def R_gMW():
    light_year = 299792458 * 60 * 60 * 24 * 365
    R_gMW = 50000 * light_year
    return R_gMW

# Supermassive black hole:

def R_supermassive_black_hole():
    R_supermassive_black_hole = 259162433900880.38
    return R_supermassive_black_hole

def R_sbh():
    R_sbh = 259162433900880.38
    return R_sbh

# black hole (calculate):

def R_black_hole(M, R):
    G = 6.6740831 * 10 ** -11
    c = 299792458
    R_black_hole = 2 * G / c ** 2
    return R_black_hole

def R_bh(M, R):
    G = 6.6740831 * 10 ** -11
    c = 299792458
    R_bh = 2 * G / c ** 2
    return R_bh


# radiuses of the orbits of the astronomic objects ( r ; м ):


# orbit of our planet (Earth):

def r():
    r = 149597870700
    return r

# search:

def r_(v, a):
    r_ = v ** 2 / a
    return r_

# orbit of the Moon aroud the Earth:

def r_moon():
    r_moon = 384.4 * 10 ** 6
    return r_moon

# orbit of the Sun in galaxy Milky Way:

def r_sun():
    light_year = 299792458 * 60 * 60 * 24 * 365
    r_sun = 26000 * light_year
    return r_sun

# orbits of the planets in our solar system:

def r_mercury():
    r_mercury = 57909227000
    return r_mercury

def r_venus():
    r_venus = 108.2 * 10 ** 9
    return r_venus

def r_earth():
    r_earth = 149597870700
    return r_earth

def r_mars():
    r_mars = 249.2 * 10 ** 9
    return r_mars

def r_jupiter():
    r_jupiter = 7.785 * 10 ** 11
    return r_jupiter

def r_saturn():
    r_saturn = 1429394069000
    return r_saturn

def r_uranus():
    r_uranus = 2876679082000
    return r_uranus

def r_neptune():
    r_neptune = 4503443661000
    return r_neptune

def r_pluto():
    r_pluto = 5906440606290.79
    return r_pluto

# orbits of the Pluto satellites aroud Pluto:

def r_charon():
    r_charon = 19.6 * 10 ** 6
    return r_charon


# speed of light (c ; m/s ):


def c():
    c = 299792458
    return c


# astronomical unit:


# (a.u. = m)

def astro_unit(n):
    astro_unit = n * 149597870700
    return astro_unit

def au(n):
    au = n * 149597870700
    return au

# (m = a.u.)

def astro_unit_(n):
    astro_unit_ = n / 149597870700
    return astro_unit_

def au_(n):
    au_ = n / 149597870700
    return au_


# light year:


#(l.y. = m):

def light_year(n):
    light_year = n * 299792458 * 60 * 60 * 24 * 365
    return light_year

def ly(n): #~
    ly = n * 299792458 * 60 * 60 * 24 * 365
    return ly

# (m = l.y.):

def light_year_(n):
    light_year_ = n / 299792458 / 365 / 24 / 60 / 60
    return light_year_

def ly_(n):
    ly_ = n / 299792458 / 365 / 24 / 60 / 60
    return ly_


# parsec:


# (pc = m):

def parsec(n):
    parsec = n * 149597870700 * 360 * 60 * 60 / (2 * math.pi) 
    return parsec

def pc(n):
    pc = n * 149597870700 * 360 * 60 * 60 / (2 * math.pi)
    return pc

# (m = pc):

def parsec_(n):
    parsec_ = 2 * n * math.pi / (360 * 60 * 60 * 149597870700)
    return parsec_

def pc_(n):
    pc_ = 2 * n * math.pi / (360 * 60 * 60 * 149597870700)
    return pc_



# Thermodynamics: ~



# values of an ideal gas:~


def R_k():
    R_k = 8.31447
    return R_k

# molar mass of air:~

def M_v():
    M_v = 0.0289644
    return M_v
    
# temperature:~

def T(t):
    T = 273 + t
    return T

def t(T):
    t = T - 273
    return t

def t_min():
    t_min = -273
    return t_min

# the Mendeleev-Clapeyron equation:~


def V_ideal_gas(P, v, T):
    R = 8.31447
    V_ideal_gas = v * R * T / P
    return V_ideal_gas

def V_ig(P, v, T):
    R = 8.31447
    V_ig = v * R * T / P
    return V_ig


def P_ideal_gas(V, v, T):
    R = 8.31447
    P_ideal_gas = v * R * T / V
    return P_ideal_gas

def P_ig(V, v, R, T):
    R = 8.31447
    P_ig = v * R * T / V
    return P_ig


def v_ideal_gas(P, V, T):
    R = 8.31447
    v_ideal_gas = P * V / (R * T)
    return v_ideal_gas

def v_ig(P, V, T):
    R = 8.31447
    v_ig = P * V / (R * T)
    return v_ig


def T_ideal_gas(P, V, v):
    R = 8.31447
    T_ideal_gas = P * V / (v * R)
    return T_ideal_gas

def T_ig(P, V, v):
    R = 8.31447
    T_ig = P * V / (v * R)
    return T_ig


# Dependence of temperature on height (T ; K):~


def t_h(t, h):
    t_h = t - 0.0065 * h
    return t_h

def T_h(T, h):
    T_h = T - 0.0065 * h
    return T_h



# Relativity of Einstein:~



# relativity

def relativity(n, v):
    c = 299792458
    relativity = n / (1 - (v / c) ** 2) ** (1/2)
    return relativity

def l_relat(n, v):
    c = 299792458
    l_relat = n / (1 - (v / c) ** 2) ** (1/2)
    return l_relat


def relativity_(n, v):
    c = 299792458
    relativity_ = n * (1 - (v / c) ** 2) ** (1/2)
    return relativity_

def l_relat_(n, v):
    c = 299792458
    l_relat_ = n * (1 - (v / c) ** 2) ** (1/2)
    return l_relat_
