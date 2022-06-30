from astropy.table import QTable
from astropy import units as u

import matplotlib.pyplot as plt
import numpy as np
from scipy import*
import aplpy
from matplotlib import*
from astropy.convolution import Kernel1D
from astropy.convolution import Box1DKernel
from astropy import units as u
from astropy.io import fits
from spectral_cube import SpectralCube
from spectral_cube import* # SpectralCube 
from spectral_cube import Projection 
import scipy.ndimage as nd
from pvextractor import extract_pv_slice
from pvextractor import Path
from scipy import optimize
from sympy import nsolve
from scipy.optimize import fsolve 
from scipy.constants import*
from astropy import constants as con
from astropy import units as u
#import matplotlib.mlab as mlab
from astropy.convolution import Kernel1D
import scipy.ndimage as nd
import aplpy
import matplotlib 
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import MaxNLocator
from scipy import stats
from astropy.table import Table
from matplotlib.ticker import FormatStrFormatter
from astropy.wcs import WCS
from astropy.wcs import utils 
from astropy.wcs.utils import pixel_to_skycoord
from astropy.wcs.utils import skycoord_to_pixel
from astropy.table import QTable
import warnings
from astropy.io import fits
import pandas as pd


##### FUNCTIONS ##########################################################################################
def f(pb,pr): # pb = blue lobe pixel. USE A LINEAR FUNCTION JOINING BLUE AND RED LOBE PIXELS
    x0 = (pb[0]+pr[0])/2
    y0 = (pb[1]+pr[1])/2
    dx = np.abs(pb[0]-x0)
    dy = np.abs(pb[1]-y0) # since y0 is midpoint, the distances from pb[1] and pr[1] are the same 
    if np.abs(pr[0]-pb[0]) <= 1e-2: # if blue and red pixels are vertical so slope=infty
        xb = x0 - 2*dx # dx = 0 anyway; all x-coordinates are the same 
        xr = x0 + 2*dx
        if pb[1] < y0:
            yb = pb[1] - 2*dy # dist between mid point and blue pixel
            yr = pr[1] + 2*dy
        elif pb[1] > y0:
            yb = pb[1] + 2*dy
            yr = pr[1] - 2*dy
    else:
        m = (pr[1]-pb[1])/(pr[0]-pb[0]) # finite slope
        if pb[0] < x0:
            xb = x0 - 2*dx
            xr = x0 + 2*dx
            yb = y0 + m*(xb-x0)
            yr= y0 + m*(xr-x0)
        elif pb[0] > x0:
            xb = x0 + 2*dx
            xr = x0 - 2*dx
            yb = y0 + m*(xb-x0)
            yr = y0 + m*(xr-x0)
    pb2 = (xb,yb)
    pr2 = (xr,yr)
    return pb2, pr2

 ### DEFINE FUNCTIONS 

def length(s):
    if s%2 == 0: #modulo zero => even
        l = s/2
    else:
        l = (s+1)/2
    return l

def Jnu(T, nu=330.5*u.GHz):
    jnu = ((con.h * nu / con.k_B)
            / (np.exp(con.h * nu / (con.k_B * T)) - 1))
    return( jnu )

def G(v, Amp, V0, Sig0, Offset):
    return( Amp * np.exp(-(v-V0)**2/(2*Sig0**2))+Offset )

def Quad(v, c0, v0, c2):
    return( c0 + c2 * (v - v0)**2 ) # a + b(x-x0)^2 form
