# -*- coding: utf-8 -*-
'''
@autor: ntrivisonno, lgarelli, mstorti
@date: APR2024
'''

import numpy


def fluid_prop(h, T):
    # Density [kg/m3] Tref=15 C
    rho0 = 1.225
    # Exponential aprox
    # Interp ISA Data
    href = [-500, 0, 500, 1e3, 1.5e3, 2e3, 2.5e3, 3e3, 3.5e3, 4e3, 4.5e3, 5e3, 5.5e3, 6e3, 6.5e3, 7e3, 7.5e3, 8e3, 8.5e3, 9e3, 9.5e3, 10e3, 10.5e3, 11e3, 11.5e3, 12e3, 12.5e3, 13e3, 13.5e3, 14e3, 14.5e3, 15e3, 15.5e3, 16e3, 16.5e3, 17e3, 17.5e3, 18e3, 18.5e3, 19e3, 19.5e3, 20e3, 22e3, 24e3, 26e3]
    r = [1.048878, 1.000000, 0.952836, 0.907385, 0.863566, 0.820645, 0.780906, 0.741901, 0.704447, 0.668380, 0.633864, 0.600653, 0.568747, 0.538229, 0.508935, 0.480865, 0.454019, 0.428397, 0.403835, 0.380335, 0.357976, 0.336597, 0.316197, 0.296777, 0.274255, 0.253448, 0.234190, 0.216401, 0.200000, 0.184823, 0.170869, 0.157895, 0.145900, 0.134802, 0.124602, 0.115137, 0.106406, 0.098327, 0.090902, 0.083966, 0.077601, 0.071726, 0.052632, 0.038270, 0.027989]
    rho = rho0*numpy.interp(h, href, r)

    # Dinamic Viscosity [kg/m s]
    mu = 1.802e-5
    # c Sound speed
    # c = 340.2
    hrefc = href
    cref = [342.20, 340.30, 338.40, 336.50, 334.50, 332.60, 330.60, 328.60, 326.60, 324.60, 322.60, 320.60, 318.60, 316.60, 314.40, 312.30, 310.20, 308.10, 306.00, 303.80, 301.70, 299.50, 297.30, 295.10, 295.10, 295.10, 295.10, 295.10, 295.10, 295.10, 295.10, 295.10, 295.10, 295.10, 295.10, 295.10, 295.10, 295.10, 295.10, 295.10, 295.10, 295.10, 296.40, 297.80, 299.10]
    c = numpy.interp(h, hrefc, cref)
    return [rho, mu, c]
