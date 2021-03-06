# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 19:48:34 2017

@author: max
"""
from __future__ import division
import numpy as np
from math import pi, sqrt
# import matplotlib.pyplot as plt
# import matplotlib.gridspec as gridspec
from scipy.constants import e
# import matplotlib as mpl
# import matplotlib.ticker as mtick
# from scipy.stats import maxwell
from scipy.special import gammaincc
from scipy.interpolate import interp1d
from collections import namedtuple
import sys

import time


def timefunc(f):
    def f_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print f.__name__, 'took', end - start, 'time'
        return result
    return f_timer


m_d = 3.343583719e-27
m_t = 5.006e-27
m_c = 1.9926467e-26
m_a = 6.643e-27


class IOL:
    """
    """
    def __init__(self, inp, core):
        sys.dont_write_bytecode = True
        np.warnings.filterwarnings('ignore')

        numcos = inp.numcos  # TODO: Clean this up
        # The additional point (numcos +1) is to account for the trimming in the
        # The line with [:-1]. This trimming accounts for the zero at the end of the coslist
        angles = np.linspace(-1, 1, inp.numcos + 1)

        # By rolling and adding, one gets angles between -1 and 1 but not including -1 and 1
        self.coslist = ((angles + np.roll(angles, -1)) / 2)[:-1]

        polpts = len(core.rho[-1])
        radpts = len(core.rho.T[-1])

        # THE FOLLOWING ARRAYS ARE 4-DIMENSIONAL ARRAYS
        # [ LAUNCH THETA POSITION , LAUNCH ANGLE COSINE, LAUNCH r  , EXIT THETA POSITION  ]

        # NOTE TO FUTURE DEVELOPERS: IF YOU TRY TO LOOP OVER THE PLASMA POINTS, LAUNCH ANGLES, AND
        # EXIT LOCATIONS IN PYTHON THE WAY YOU WOULD IN C OR FORTRAN, IT'S GOING TO TAKE FOREVER.
        # ALTHOUGH THESE ARRAYS TAKE MORE MEMORY THAN I'D LIKE, IT'S CURRENTLY NECESSARY TO DO IT THIS WAY.
        # MAYBE SOMETHING TO IMPROVE ON IN THE FUTURE.

        # CREATE ARRAYS FOR LAUNCH POINTS IN THE PLASMA
        r0 = np.broadcast_arrays(np.ones(polpts)[:, None, None, None],
                                 np.ones(inp.numcos)[:, None, None],
                                 core.rho)[-1]

        B0 = np.broadcast_arrays(np.ones(polpts)[:, None, None, None],
                                 np.ones(inp.numcos)[:, None, None],
                                 core.B_tot)[-1]

        f0 = np.broadcast_arrays(np.ones(polpts)[:, None, None, None],
                                 np.ones(inp.numcos)[:, None, None],
                                 core.f_phi)[-1]

        psi0 = np.broadcast_arrays(np.ones(polpts)[:, None, None, None],
                                   np.ones(inp.numcos)[:, None, None],
                                   core.psi)[-1]

        phi0 = np.broadcast_arrays(np.ones(polpts)[:, None, None, None],
                                   np.ones(inp.numcos)[:, None, None],
                                   core.E_pot)[-1] * 1E3  # now in volts

        zeta0 = np.broadcast_arrays(np.ones(polpts)[:, None, None, None],
                                    self.coslist[:, None, None],
                                    np.ones(core.R.shape))[1]

        # CREATE ARRAYS FOR DESTINATION POINTS ALONG THE SEPERATRIX
        R1 = np.broadcast_arrays(np.ones(polpts)[:, None, None, None],
                                 np.ones(inp.numcos)[:, None, None],
                                 np.ones(radpts)[:, None],
                                 np.ones(polpts)[:],
                                 core.R[-1][:, None, None, None])[-1]

        f1 = np.broadcast_arrays(np.ones(polpts)[:, None, None, None],
                                 np.ones(inp.numcos)[:, None, None],
                                 np.ones(radpts)[:, None], np.ones(polpts)[:],
                                 core.f_phi[-1][:, None, None, None])[-1]

        B1 = np.broadcast_arrays(np.ones(polpts)[:, None, None, None],
                                 np.ones(inp.numcos)[:, None, None],
                                 np.ones(radpts)[:, None],
                                 np.ones(polpts)[:],
                                 core.B_tot[-1][:, None, None, None])[-1]

        psi1 = np.broadcast_arrays(np.ones(polpts)[:, None, None, None],
                                   np.ones(inp.numcos)[:, None, None],
                                   np.ones(radpts)[:, None],
                                   np.ones(polpts)[:],
                                   core.psi[-1][:, None, None, None])[-1]

        phi1 = np.broadcast_arrays(np.ones(polpts)[:, None, None, None],
                                   np.ones(inp.numcos)[:, None, None],
                                   np.ones(radpts)[:, None],
                                   np.ones(polpts)[:],
                                   core.E_pot[-1][:, None, None, None])[-1] * 1E3  # now in volts

        Tprofile = namedtuple('Tprofile', 'i C')(
            core.T.i.kev.T[0],
            core.T.C.kev.T[0]
        )

        # iol_params = {}
        # iol_params['r0'] = r0
        # iol_params['B0'] = B0
        # iol_params['f0'] = f0
        # iol_params['psi0'] = psi0
        # iol_params['phi0'] = phi0
        # iol_params['zeta0'] = zeta0
        # iol_params['R1'] = R1
        # iol_params['f1'] = f1
        # iol_params['B1'] = B1
        # iol_params['psi1'] = psi1
        # iol_params['phi1'] = phi1
        # iol_params['Tprofile'] = Tprofile

        # convert iol_params to namedtuple so individual parameters can be accessed as normal attributes
        iol_p = namedtuple('iol_p', 'r0 B0 f0 psi0 phi0 zeta0 R1 f1 B1 psi1 phi1')(
            r0,
            B0,
            f0,
            psi0,
            phi0,
            zeta0,
            R1,
            f1,
            B1,
            psi1,
            phi1
        )
        
        # Calculate IOL for thermal deuterium
        forb_d_therm, morb_d_therm, eorb_d_therm = calc_iol_maxwellian(1,
                                                                       m_d,
                                                                       iol_p,
                                                                       core.thetapts,
                                                                       Tprofile.i,
                                                                       self.coslist,
                                                                       numcos)
        self.forb_d_therm = inp.R_loss * forb_d_therm
        self.morb_d_therm = inp.R_loss * morb_d_therm
        self.eorb_d_therm = inp.R_loss * eorb_d_therm
        self.forb_d_therm_1D = self.forb_d_therm[:, 0]
        self.morb_d_therm_1D = self.morb_d_therm[:, 0]
        self.eorb_d_therm_1D = self.eorb_d_therm[:, 0]

        # Calculate IOL for thermal tritium
        forb_t_therm, morb_t_therm, eorb_t_therm = calc_iol_maxwellian(1,
                                                                       m_t,
                                                                       iol_p,
                                                                       core.thetapts,
                                                                       Tprofile.i,
                                                                       self.coslist,
                                                                       numcos)
        self.forb_t_therm = inp.R_loss * forb_t_therm
        self.morb_t_therm = inp.R_loss * morb_t_therm
        self.eorb_t_therm = inp.R_loss * eorb_t_therm
        self.forb_t_therm_1D = self.forb_t_therm[:, 0]
        self.morb_t_therm_1D = self.morb_t_therm[:, 0]
        self.eorb_t_therm_1D = self.eorb_t_therm[:, 0]

        # Calculate IOL for thermal carbon
        forb_c_therm, morb_c_therm, eorb_c_therm = calc_iol_maxwellian(6,
                                                                       m_c,
                                                                       iol_p,
                                                                       core.thetapts,
                                                                       Tprofile.C,
                                                                       self.coslist,
                                                                       numcos)
        self.forb_c_therm = inp.R_loss * forb_c_therm
        self.morb_c_therm = inp.R_loss * morb_c_therm
        self.eorb_c_therm = inp.R_loss * eorb_c_therm
        self.forb_c_therm_1D = self.forb_c_therm[:, 0]
        self.morb_c_therm_1D = self.morb_c_therm[:, 0]
        self.eorb_c_therm_1D = self.eorb_c_therm[:, 0]

        # Calculate IOL for thermal alphas
        forb_a_therm, morb_a_therm, eorb_a_therm = calc_iol_maxwellian(2,
                                                                       m_a,
                                                                       iol_p,
                                                                       core.thetapts,
                                                                       Tprofile.i,
                                                                       self.coslist,
                                                                       numcos)
        self.forb_a_therm = inp.R_loss * forb_a_therm
        self.morb_a_therm = inp.R_loss * morb_a_therm
        self.eorb_a_therm = inp.R_loss * eorb_a_therm
        self.forb_a_therm_1D = self.forb_a_therm[:, 0]
        self.morb_a_therm_1D = self.morb_a_therm[:, 0]
        self.eorb_a_therm_1D = self.eorb_a_therm[:, 0]

        # Calculate IOL for fast, monoenergetic alphas
        v_alpha = sqrt(2*3.5E6*1.6021E-19/m_a)
        forb_a_fast, morb_a_fast, eorb_a_fast = calc_iol_mono_en(2,
                                                                 m_a,
                                                                 iol_p,
                                                                 core.thetapts,
                                                                 v_alpha,
                                                                 self.coslist,
                                                                 numcos)

        # currently applying R_loss to fast alphas as well as thermal, although I'm skeptical of this. -MH
        self.forb_a_fast = inp.R_loss * forb_a_fast
        self.morb_a_fast = inp.R_loss * morb_a_fast
        self.eorb_a_fast = inp.R_loss * eorb_a_fast
        self.forb_a_fast_1D = self.forb_a_fast[:, 0]
        self.morb_a_fast_1D = self.morb_a_fast[:, 0]
        self.eorb_a_fast_1D = self.eorb_a_fast[:, 0]

        # Calculate IOL for neutral deuterium beams
        v_beam = sqrt(2*80.0E3*1.6021E-19/m_d)
        zeta_beam = -0.96
        forb_d_nbi, morb_d_nbi, eorb_d_nbi = calc_iol_beams(1,
                                                            m_d,
                                                            iol_p,
                                                            core.thetapts,
                                                            v_beam,
                                                            zeta_beam,
                                                            self.coslist)
        # currently applying R_loss to fast alphas as well as thermal, although I'm skeptical of this. -MH
        self.forb_d_nbi = inp.R_loss * forb_d_nbi
        self.morb_d_nbi = inp.R_loss * morb_d_nbi
        self.eorb_d_nbi = inp.R_loss * eorb_d_nbi
        self.forb_d_nbi_1D = self.forb_d_nbi[:, 0]
        self.morb_d_nbi_1D = self.morb_d_nbi[:, 0]
        self.eorb_d_nbi_1D = self.eorb_d_nbi[:, 0]


def calc_vsep(z, m, p):
    """Calculates V_sep"""

    # a = (np.abs(p.B1 / p.B0) * p.f0 / p.f1 * p.zeta0) ** 2 - 1 + (1 - p.zeta0 ** 2) * np.abs(p.B1 / p.B0)
    # b = 2 * z * e * (p.psi0 - p.psi1) / (p.R1 * m * p.f1) * np.abs(p.B1 / p.B0) * p.f0 / p.f1 * p.zeta0
    # c = (z * e * (p.psi0 - p.psi1) / (p.R1 * m * p.f1)) ** 2 - 2 * z * e * (p.phi0 - p.phi1) / m

    temp0 = z * e * (p.psi0 - p.psi1) / (p.R1 * m * p.f1)
    temp1 = np.abs(p.B1 / p.B0)
    temp2 = temp1 * p.f0 / p.f1 * p.zeta0

    a = temp2 * temp2 - 1 + (1 - p.zeta0 * p.zeta0) * temp1
    b = 2 * temp0 * temp2
    c = temp0 * temp0 - 2 * (z * e / m) * (p.phi0 - p.phi1)

    # Quadratic Formula in the form (b/2a) - sqrt( (b/2a)**2 - c/a)
    b_over_2a = b / (2 * a)
    discriminant = np.sqrt(b_over_2a ** 2 - c/a)

    v_sep = np.full(p.r0.shape, fill_value=np.nan)

    # all cases where b/2a < discriminant:
    #   -b/2a - discriminant is negative
    #   -b/2a + discriminant is positive
    upper_cases = b_over_2a < discriminant
    v_sep[upper_cases] = -b_over_2a[upper_cases] + discriminant[upper_cases]

    # all cases where b/2a > 0 and b/2a > D:
    # (-b/2a - discriminant) < (-b/2a + discriminant)
    lower_cases = np.logical_and(b_over_2a < 0, b_over_2a > discriminant)
    v_sep[lower_cases] = -b_over_2a[lower_cases] - discriminant[lower_cases]

    # all cases where b/2a > 0 and b/2a > discriminant
    #   (-b/2a - discriminant) < (-b/2a + discriminant) < 0
    #   v_sep for these conditions is already nan

    v_sep_min = np.nanmin(np.nanmin(v_sep, axis=0), axis=2).T
    v_sep_min[-1] = 0
    return v_sep, v_sep_min


def expensive_function(z, m, p):
    a = (np.abs(p.B1 / p.B0) * p.f0 / p.f1 * p.zeta0) ** 2 - 1 + (1 - p.zeta0 ** 2) * np.abs(p.B1 / p.B0)
    b = 2 * z * e * (p.psi0 - p.psi1) / (p.R1 * m * p.f1) * np.abs(p.B1 / p.B0) * p.f0 / p.f1 * p.zeta0
    c = (z * e * (p.psi0 - p.psi1) / (p.R1 * m * p.f1)) ** 2 - 2 * z * e * (p.phi0 - p.phi1) / m

    v_sep_1 = (-b + np.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    v_sep_2 = (-b - np.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return v_sep_1, v_sep_2


def calc_iol_maxwellian(z, m, param, thetapts, Tprofile, coslist, numcos):
    """Calculates eps_min for IOL of species treated with a truncated maxwellian."""

    v_sep, v_sep_min = calc_vsep(z, m, param)

    # Define the Maxwellian for every point in the plasma based on its temperature

    T_matrix = np.zeros(v_sep_min.shape)
    for indx, row in enumerate(T_matrix):
        T_matrix[indx, :] = Tprofile[indx]

    # Create the launch angle matrix (used in the calculation of M_orb)
    zeta_matrix = np.zeros(v_sep_min.shape)
    for indx, column in enumerate(zeta_matrix.T):
        zeta_matrix[:, indx] = coslist[indx]

    eps_min = m * v_sep_min**2 / (2*T_matrix*1E3*e)

    # F_orb calculation
    # note: the use of gammaincc renders the denominator in Dr. Stacey's equations obsolete.
    integrand_f = gammaincc(3/2, eps_min)
    F_orb_1D = np.sum(integrand_f, axis=1)*(2/numcos)/2
    F_orb_1D = np.nan_to_num(F_orb_1D)
    F_orb = np.repeat(F_orb_1D.reshape(-1, 1), thetapts, axis=1)

    # M_orb calculation
    integrand_m = zeta_matrix*gammaincc(2, eps_min)
    M_orb_1D = np.sum(integrand_m, axis=1)*(2/numcos)/2
    M_orb_1D = np.nan_to_num(M_orb_1D)
    M_orb = np.repeat(M_orb_1D.reshape(-1, 1), thetapts, axis=1)

    # E_orb calculation
    integrand_e = gammaincc(5/2, eps_min)
    E_orb_1D = np.sum(integrand_e, axis=1)*(2/numcos)/2
    E_orb_1D = np.nan_to_num(E_orb_1D)
    E_orb = np.repeat(E_orb_1D.reshape(-1, 1), thetapts, axis=1)

    return F_orb, M_orb, E_orb


def calc_iol_mono_en(z, m, param, thetapts, v_mono, coslist, numcos):
    """calculates IOL for a monoenergetic species with isotropic launch angle (i.e. fast alphas)"""

    v_sep, v_sep_min = calc_vsep(z, m, param)

    # Create the launch angle matrix (used in the calculation of M_orb)
    zeta_matrix = np.zeros(v_sep_min.shape)
    for indx, column in enumerate(zeta_matrix.T):
        zeta_matrix[:, indx] = coslist[indx]

    # F_orb calculation
    # integrand_f = np.where(v_sep_min <= v_mono, 1.0, 0)
    integrand_f = np.heaviside(v_mono - v_sep_min, 1)
    F_orb_1D = np.sum(integrand_f, axis=1) * (2 / numcos) / 2
    F_orb_1D = np.nan_to_num(F_orb_1D)
    F_orb = np.repeat(F_orb_1D.reshape(-1, 1), thetapts, axis=1)

    # M_orb calculation
    # integrand_m = zeta_matrix * np.where(v_sep_min <= v_mono, 1, 0)
    integrand_m = zeta_matrix * np.heaviside(v_mono - v_sep_min, 1)
    M_orb_1D = np.sum(integrand_m, axis=1) * (2 / numcos) / 2
    M_orb_1D = np.nan_to_num(M_orb_1D)
    M_orb = np.repeat(M_orb_1D.reshape(-1, 1), thetapts, axis=1)

    # E_orb calculation
    # E_orb is mathematically identical to F_orb for monoenergetic, isotropic launch angle species
    E_orb = F_orb

    return F_orb, M_orb, E_orb


def calc_iol_beams(z, m, param, thetapts, v_mono, zeta_beam, coslist):
    """calculates IOL for a monoenergetic species with a single known launch angle (i.e. beam ions)"""

    v_sep, v_sep_min = calc_vsep(z, m, param)

    # Obtain v_sep_min(zeta_beam) for each rho value
    v_sep_min_zeta = np.zeros(len(v_sep_min))

    for i, v in enumerate(v_sep_min):
        # create interpolation function of v_sep_min(rho) vs zeta
        v_sep_min_zeta_interp = interp1d(coslist, v, fill_value='extrapolate')
        # get v_sep_min(zeta_beam)
        v_sep_min_zeta[i] = v_sep_min_zeta_interp(zeta_beam)

    # F_orb calculation
    F_orb_1D = np.heaviside(v_mono - v_sep_min_zeta, 1)
    F_orb_1D = np.nan_to_num(F_orb_1D)
    F_orb = np.repeat(F_orb_1D.reshape(-1, 1), thetapts, axis=1)

    # M_orb calculation
    M_orb_1D = zeta_beam * np.heaviside(v_mono - v_sep_min_zeta, 1)
    M_orb_1D = np.nan_to_num(M_orb_1D)
    M_orb = np.repeat(M_orb_1D.reshape(-1, 1), thetapts, axis=1)

    # E_orb calculation
    # E_orb is mathematically identical to F_orb for monoenergetic, monodirectional species
    E_orb = F_orb

    return F_orb, M_orb, E_orb

# iolplot=1
# if iolplot==1:
#    fig = plt.figure(figsize=(5, 5))
#    fig.suptitle('IOL a, b, c in DIII-D with cos:{}'.format(coslist[-2]), fontsize=15)
#    ax1 = fig.add_subplot(221)
#    ax1.set_title(r'$v_{sep-1}$', fontsize=12)
#    ax1.set_ylabel(r'R', fontsize=12)
#    ax1.set_xlabel(r'Z', fontsize=12)
#    ax1.axis('equal')
#    ax1.grid(b=True, which='both', axis='both')
#    CS = ax1.contourf(brnd.R, brnd.Z, v_sep_1[:, -2, :, 0].T, 500)
#    plt.colorbar(CS)
#
#    ax2 = fig.add_subplot(222)
#    ax2.set_title(r'$v_{sep-2}$', fontsize=12)
#    ax2.set_ylabel(r'R', fontsize=12)
#    ax2.set_xlabel(r'Z', fontsize=12)
#    ax2.axis('equal')
#    ax2.grid(b=True, which='both', axis='both')
#    CS = ax2.contourf(brnd.R, brnd.Z, v_sep_2[:, -2, :, 0].T, 500)
#    plt.colorbar(CS)
#
#    ax3 = fig.add_subplot(223)
#    ax3.set_title(r'$v_{sep}$', fontsize=12)
#    ax3.set_ylabel(r'R', fontsize=12)
#    ax3.set_xlabel(r'Z', fontsize=12)
#    ax3.axis('equal')
#    ax3.grid(b=True, which='both', axis='both')
#    #CS = ax3.pcolor(brnd.R, brnd.Z, v_sep[:, 10, :, 0].T, vmin=0, vmax=1E8)
#    CS = ax3.contourf(brnd.R, brnd.Z, v_sep[:, -2, :, 0].T, 500)
#    plt.colorbar(CS)

#    plt.tight_layout()
#    fig.subplots_adjust(top=0.84)
# if iolplot==1:
#     fig = plt.figure(figsize=(6, 8))
#     fig.suptitle(r'IOL v_{} with cos:{}'.format('esc', coslist[0]), fontsize=15)
#     ax1 = fig.add_subplot(111)
#     #ax1.set_title(r'$v_{sep}$', fontsize=12)
#     ax1.set_ylabel(r'Z', fontsize=12)
#     ax1.set_xlabel(r'R', fontsize=12)
#     ax1.axis('equal')
#     ax1.grid(b=True, which='both', axis='both')
#
#     test = np.nanmin(v_sep, axis=3).T
#
#     CS = ax1.contourf(brnd.R, brnd.Z, np.log10((0.5*m*test[:, 0, :]**2)/(1.6021E-19 * 1.0E3)), 500)
#     plt.colorbar(CS)
#     #plt.tight_layout()
#     fig.subplots_adjust(top=0.95)
#     #fig.subplots_adjust(top=0.95)
# return
