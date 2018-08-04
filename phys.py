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
    print("[q] could be m, ma, f, G, F, g, a, M, R, r, c, ")
    print("R_black_hole (R_bh), astro_unit (au), light_year (ly), parsec (pc) and")
    print("relativity (l_relat).") 
    print("In Astronomical part:")
    print("[M] is mass of astronomical object")
    print("[R] is radius of astronomical object")
    print("[r] is radius of the orbit of astronomical object")
    print("[data] is some object and can be constant value:")
    print()
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

    
# easy physics:


def m(p, V):
    m = p * V
    return m

def p(F, S):
    p = F / S
    return p


# Newton's physics:


def ma(m, a):
    ma = m * a
    return ma

def f(m, a):
    f = m * a
    return f


# gravity force



def G():
    G = 6.6740831 * 10 ** -11
    return G

def F(m, M, R):
    G = 6.6740831 * 10 ** -11
    F = G * m * M / R ** 2
    return F

def F_(m, M, R, h):
    G = 6.6740831 * 10 ** -11
    F = G * m * M / (R + h) ** 2
    return F_

def g():
    g = 9,80665
    return g

def a(M, R):
    G = 6.6740831 * 10 ** -11
    a = G * M / R ** 2
    return a

def a_(M, R, h):
    G = 6.6740831 * 10 ** -11
    a = G * M / (R + h) ** 2
    return a


# masses of the astronomic objects ( M ; кг ):


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


# radiuses of the astronomic objects ( R ; м ):


# our planet (Earth):

def R():
    R = 6356863
    return R

# search:

def R_(M, a):
    G = 6.6740831 * 10 ** -11
    R_ = (G * M / a) ** (1/2)
    
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


# speed of light (c ; м/с):


def c():
    c = 299792458
    return c


# astronomical unit:


# (a.e. = м)

def astro_unit(n):
    astro_unit = n * 149597870700
    return astro_unit

def au(n):
    au = n * 149597870700
    return au

# (м = a.e.)

def astro_unit_(n):
    astro_unit_ = n / 149597870700
    return astro_unit_

def au_(n):
    au_ = n / 149597870700
    return au_


# light year:


#(l.y. = м):

def light_year(n):
    light_year = n * 299792458 * 60 * 60 * 24 * 365
    return light_year

def ly(n):
    light_year = n * 299792458 * 60 * 60 * 24 * 365
    return ly

# (м = l.y.):

def light_year_(n):
    light_year_ = n / 299792458 / 365 / 24 / 60 / 60
    return light_year_

def ly_(n):
    ly_ = n / 299792458 / 365 / 24 / 60 / 60
    return ly_


# parsec:


# (pc = м):

def parsec(n):
    parsec = n * 149597870700 * 360 * 60 * 60 / (2 * math.pi) 
    return parsec

def pc(n):
    pc = n * 149597870700 * 360 * 60 * 60 / (2 * math.pi)
    return pc

# (м = pc):

def parsec_(n):
    parsec_ = 2 * n * math.pi / (360 * 60 * 60 * 149597870700)
    return parsec_

def pc_(n):
    pc_ = 2 * n * math.pi / (360 * 60 * 60 * 149597870700)
    return pc_

# relativity

def relativity(n, v):
    c = 299792458
    relativity = n / (1 - (v/c) ** 2) ** (1/2)
    return relativity

def l_relat(n, v):
    c = 299792458
    l_relat = n / (1 - (v/c) ** 2) ** (1/2)
    return l_relat
