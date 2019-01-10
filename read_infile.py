#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 16:10:25 2017

@author: max
"""
from math import ceil
import os
import re
import sys
import numpy as np
from math import pi
import matplotlib.pyplot as plt
from numpy.core.multiarray import ndarray
from scipy.interpolate import griddata
from shapely.geometry import LineString, Polygon
from scipy.interpolate import UnivariateSpline, interp1d


class ReadInfile:
    """Reads main GT3 input file.
    
    Methods:
        read_vars
        read_exp
        wall_prep
        showparams
    
    Attributes:    
        exp_inp          (bool)      
        a                (float)    tokamak minor radius (m)
        BT0              (float)    toroidal field strength at mag. axis (T)
        R0_a             (float)    tokamak major radius (m)
        Z0               (float)    vertical height of the magnetic axis (m)
        kappa_up         (float)    upper elongation at the seperatrix
        kappa_lo         (float)    lower elongation at the seperatrix
        tri_up           (float)
        tri_lo           (float)
        xmil             (int)
        xpt_R            (float)
        xpt_Z            (float)
        xpt
        thetapts_approx  (int)
        thetapts
        rmeshnum_p       (int)
        rpts             (int)
        ni0              (float)
        ni9              (float)
        ni_sep           (float)
        nu_ni            (float)
        ne0              (float)
        ne9              (float)
        ne_sep           (float)
        nu_ne            (float)  
        Ti0              (float)
        Ti9              (float)
        Ti_sep           (float)
        nu_Ti            (float)
        Te0              (float)
        Te9              (float)
        Te_sep           (float)
        nu_Te            (float)
        j0               (float)
        j_sep            (float)
        nu_j             (float)
        s_k_up           (float)
        s_k_lo           (float)
        xtheta1          (float)
        xtheta2          (float)
        xtheta3          (float)
        xtheta4          (float)
        wallfile         (str)         
    """

    def __init__(self, infile):
        sys.dont_write_bytecode = True

        self.shotlabel = None  # type: str

        self.invars = {}  # Populated in read_vars
        self.in_prof = {}  # Populated in read_vrs
        self.in_map2d = {}
        self.in_line2d = {}

        self.neutfile_loc = None
        self.ntrl_switch = None

        self.xpt = None
        self.xpt_R = None
        self.xpt_Z = None

        self.wall_line = None  # type: object
        self.wall_exp = None

        self.wall_vertex = None  # type: ndarray
        self.wall_vertex_closed = None  # type: ndarray

        self.neut_outfile = None  # type: str

        self.read_vars(infile)
        self.read_exp()
        self.set_ntrl_switch()

        # if hasattr(self, 'wall_file'):
        #    self.wall_prep()

    def read_vars(self, infile):
        """
        """
        
        # some regex commands we'll use when reading stuff in from the input file
        r0di = "r'%s *= *([ , \d]*) *'%(v)"
        r0df = "r'%s *= *([+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?) *'%(v)"
        # r0ds = "r'%s *= *((?:/?\.?\w+\.?)+/?) *'%(v)"
        r0ds = "r'%s *= *((?:\/?\w+)+(?:\.\w+)?) *'%(v)"
        # r1di = "r'%s\( *(\d*) *\) *= *(\d*) *'%(v)"
        # r1df = "r'%s\( *(\d*)\) *= *([+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?) *'%(v)"
        # r2df = "r'%s\( *(\d*)\) *= *((?:[+\-]?\d*\.?\d*(?:[eE]?[+\-]?\d+)?, ?)*) *'%(v)"

        # GENERAL PARAMETERS

        # GRID CONSTRUCTION PARAMETERS

        self.invars = dict(
            rhopts=['int', r0di],
            edge_rho=['float', r0df],
            rhopts_edge=['int', r0di],
            rhopts_core=['int', r0di],
            thetapts_approx=['int', r0di],
            BT0=['float', r0df],
            Er_scale=['float', r0df],
            psi_scale=['float', r0df],

            # SOL PARAMETERS
            sollines_psi_max=['float', r0df],
            num_sollines=['int', r0di],
            xi_sep_pts=['int', r0di],
            ib_trim_off=['float', r0df],
            ob_trim_off=['float', r0df],
            xi_ib_pts=['int', r0di],
            xi_ob_pts=['int', r0di],

            # NEUTRALS PARAMETERS
            core_thetapts_ntrl=['int', r0di],
            ib_thetapts_ntrl=['int', r0di],
            ob_thetapts_ntrl=['int', r0di],
            rhopts_ntrl=['int', r0di],
            edge_rho_ntrl=['float', r0df],
            rhopts_edge_ntrl=['float', r0df],
            rhopts_core_ntrl=['float', r0df],
            wall_ni_min=['float', r0df],
            wall_ne_min=['float', r0df],
            wall_Ti_min=['float', r0df],
            wall_Te_min=['float', r0df],
            tri_min_angle=['float', r0df],
            tri_min_area=['float', r0df],

            # PFR PARAMETERS
            pfr_ni_val=['float', r0df],
            pfr_ne_val=['float', r0df],
            pfr_Ti_val=['float', r0df],
            pfr_Te_val=['float', r0df],

            # IOL PARAMETERS
            numcos=['int', r0di],
            R_loss=['float', r0df],

            # RAD TRANS RELATED QUANTITIES - NEEDS WORK
            eq1=['float', r0df],
            eq2=['float', r0df],
            xmas1=['float', r0df],
            xmas2=['float', r0df],
            ephia=['float', r0df],
            xk=['float', r0df],
            delma=['float', r0df],
            xnuati=['float', r0df],
            xnuioni=['float', r0df],
            q95=['float', r0df],

            # NEUTRALS CALCULATION
            neut_outfile=['str', r0ds],
            ntrl_rho_start=['float', r0df],
            ntrl_rpts=['int', r0di],
            ntrl_thetapts=['int', r0di],

            # NEUTRAL BEAM CALCULATION
            ebeam=['float', r0df],
            abeam=['float', r0df],
            alphain=['float', r0df],
            pbeam=['float', r0df],
            rtang=['float', r0df],

            # EXECUTABLE LOCATIONS
            nbeams_loc=['str', r0ds],
            adpak_loc=['str', r0ds],
            triangle_loc=['str', r0ds]
        )

        self.in_prof = dict(
            er_file=['str', r0ds, 'er_data'],
            jr_file=['str', r0ds, 'jr_data'],
            ne_file=['str', r0ds, 'ne_data'],
            nD_file=['str', r0ds, 'nD_data'],
            nT_file=['str', r0ds, 'nT_data'],
            nW_file=['str', r0ds, 'nW_data'],
            nBe_fil=['str', r0ds, 'nBe_data'],
            na_file=['str', r0ds, 'na_data'],
            nC_file=['str', r0ds, 'nC_data'],
            Te_file=['str', r0ds, 'Te_data'],
            Ti_file=['str', r0ds, 'Ti_data'],
            TC_file=['str', r0ds, 'TC_data'],
            frac_C_file=['str', r0ds, 'frac_C_data'],
            vpolC_file=['str', r0ds, 'vpolC_data'],
            vtorC_file=['str', r0ds, 'vtorC_data'],
            vpolD_file=['str', r0ds, 'vpolD_data'],
            vtorD_file=['str', r0ds, 'vtorD_data'],
            nbi_dep_file=['str', r0ds, 'dPdr_norm1_data']
        )

        self.in_map2d = dict(psirz_file=['str', r0ds, 'psirz_exp'])
        
        self.in_line2d = dict(wall_file=['str', r0ds, 'wall_exp'])
        
        # Read input variables
        with open(os.getcwd() + '/inputs/' + infile, 'r') as f:
            for count, line in enumerate(f):
                if not line.startswith('#'):
                    # read in 0d variables
                    for v in self.invars:
                        exec("result = re.match(%s, line)" % self.invars[v][1])
                        if result:
                            exec("self.%s = %s(result.group(1))" % (v, self.invars[v][0]))
                            
                    # read in the names of radial profile input files
                    for v in self.in_prof:
                        exec("result = re.match(%s, line)" % self.in_prof[v][1])
                        if result:
                            exec("self.%s = %s(result.group(1))" % (v, self.in_prof[v][0]))

                    # read in the names of input files that map a quantity on the R-Z plane
                    for v in self.in_map2d:
                        exec("result = re.match(%s, line)" % self.in_map2d[v][1])
                        if result:
                            exec("self.%s = %s(result.group(1))" % (v, self.in_map2d[v][0]))

                    # read in the names of input files that define a line in the R-Z plane
                    for v in self.in_line2d:
                        exec("result = re.match(%s, line)" % self.in_line2d[v][1])
                        if result:
                            exec("self.%s = %s(result.group(1))" % (v, self.in_line2d[v][0]))

        # adjust thetapts so there are lines at theta = 0, pi/2, pi, and 3pi/2
        # this is critical for x-miller mode, but could be nice for the experimental input mode as well
        
        # self.thetapts =  int(4 * ceil(float(self.thetapts_approx)/4))+1
        try:
            self.xpt = np.array([self.xpt_R, self.xpt_Z])
        except:
            pass

    def read_exp(self, filename=None):
        
        # read in additional input files
        for infile in self.in_prof:
            try:
                exec("filename = self.%s" % infile)
                filepath = os.getcwd()+'/inputs' + filename
                try:
                    exec("self.%s = np.genfromtxt('%s',comments='#')" % (self.in_prof[infile][2], filepath))
                except Exception as e:
                    print 'Something may have gone wrong: ', e
            except:
                pass
            
        for infile in self.in_map2d:
            try:

                exec("filename = self.%s" % infile)
                filepath = os.getcwd()+'/inputs/' + filename
                try:
                    exec("self.%s = np.genfromtxt('%s',comments='#')" % (self.in_map2d[infile][2], filepath))
                except Exception as e:
                    print 'Something may have gone wrong: ', e
            except:
                pass
            
        for infile in self.in_line2d:
            try:
                exec("filename = self.%s" % infile)
                filepath = os.getcwd()+'/inputs/' + filename
                try:
                    exec("self.%s = np.genfromtxt('%s',comments='#')" % (self.in_line2d[infile][2], filepath))
                except Exception as e:
                    print 'Something may have gone wrong: ', e
            except:
                pass

        self.wall_line = LineString(self.wall_exp)
        
    def set_ntrl_switch(self):
        # set neutral switch for modes that need neutrals
        # 0: don't run neutrals because not necessary for calculations being done
        # 1: neutrals needed, but the neut_outfile specified in input file exists.
        #    Use that data rather than running neutpy
        # 2: run neutpy
        
        # check if specified neutpy_outfile exists. If so, read in and skip everything else.
        outfile_found = 0
        try:
            for root, subdirs, files in os.walk(os.getcwd()):
                for filename in files:
                    if filename == self.neut_outfile:
                        outfile_found = 1
                        os.path.join(root, filename)
                        self.neutfile_loc = os.path.join(root, filename)
                        self.ntrl_switch = 1
                        
            if outfile_found == 0:
                self.neutfile_loc = os.getcwd() + '/' + self.neut_outfile
                self.ntrl_switch = 2
        except AttributeError:
            # neut_outfile wasn't specified in input file. Assign default value of neut_outfile.dat
            self.neutfile_loc = os.getcwd() + '/neut_outfile.dat'
            self.ntrl_switch = 2

    def wall_prep(self):
        """
        """   
    
        adotb = (self.wall_exp[:, 0] - np.roll(self.wall_exp[:, 0], 1)) \
            * (self.wall_exp[:, 0] - np.roll(self.wall_exp[:, 0], -1)) \
            + (self.wall_exp[:, 1] - np.roll(self.wall_exp[:, 1], 1)) \
            * (self.wall_exp[:, 1] - np.roll(self.wall_exp[:, 1], -1))
        mag_a = np.sqrt((self.wall_exp[:, 0]-np.roll(self.wall_exp[:, 0], 1))**2
                        + (self.wall_exp[:, 1]-np.roll(self.wall_exp[:, 1], 1))**2)
        mag_b = np.sqrt((self.wall_exp[:, 0]-np.roll(self.wall_exp[:, 0], -1))**2
                        + (self.wall_exp[:, 1]-np.roll(self.wall_exp[:, 1], -1))**2)
        
        wall_angles = np.arccos(adotb/(mag_a*mag_b))/pi
        self.wall_vertex = np.zeros((self.wall_exp.shape[0], 2))
        
        for i in range(0, self.wall_exp.shape[0]):
            if wall_angles[i] <= 0.99:
                self.wall_vertex[i, :] = self.wall_exp[i, :]
            else:
                self.wall_vertex[i, :] = 0
        self.wall_vertex = self.wall_vertex[np.all(self.wall_vertex != 0, axis=1)]  # removing zeros from array
        # need to add in an additional criteria to also remove points that are extremely close to other points,
        # even if they create a sufficiently large angle
        self.wall_vertex_closed = np.vstack((self.wall_vertex, self.wall_vertex[0]))
        self.wall_line = LineString(self.wall_vertex_closed)
        # self.wall_ring = LinearRing(wall_pts)
        # self.wall_line = LineString(self.wall_vertex)

    def showparams(self):
        """
        """
        print '**PARAMETERS FOR SHOT \'{}\'.'.format(self.shotlabel)
        for key in vars(self).iteritems():
            if (key[0][0] != '_' and key[0] != 'line' and key[0] != 'infile' and key[0] != 'variable'
                    and key[0] != 'value'):
                print ('{} = {}'.format(key[0], key[1]))
        print '**END OF PARAMETERS**'
