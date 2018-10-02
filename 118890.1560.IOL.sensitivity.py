#!/usr/bin/env python2
"""
Created on Thu Dec 28 02:13:04 2017

@author: Jonathan
"""
###############################################################################
#
#    Shot 118890.1560 sensitivity study of IOL and neutrals
#
###############################################################################

import GTEDGE3_cli
import lib.graphs.graphs as graphs
import matplotlib.pyplot as plt
import pickle
import numpy as np

SHOT=118890
TIMEID=1560

###############################################################################
#
#   Utilities
#
##############################################################################

def yRangeFind(inList):
    x=np.concatenate(inList)
    flat=x.flatten()
    flat.sort()
    return [flat[2],flat[-2]]

###############################################################################
#
#    Chi Comparison
#
###############################################################################

def chiComp1(shot, shotnoIOL):
    prettyID = [r'$Q^{diff}_{j,L}=Q^{total}_j$ w/ IOL',
                r'$Q^{diff}_{j,L}=Q^{total}_j$ w/out IOL']

    title = r"Comparison of Ion Heat Conductivity w/ and w/out IOL"

    adjustments = {}
    caption = ["Ion heat conductivity in the edge for DIII-D shot %s.%s w/ and w/out IOL correction" % (str(SHOT),str(TIMEID)),
               "Neutrals calculation included"]

    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.chi2), (prettyID[1], shotnoIOL.chi2)],
                         yrange=[-2, 2.],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_j$", r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                         textSpace=.065,
                         marginBottom=.2,
                         marginLeft=0.095,
                         capAdj=0.15,
                         yLabelAdj=-.25,
                         xLabelAdj=-.05,
                         size=(16, 12))


def chiComp2(shot, shotnoIOL):
    prettyID = [r'$Q^{diff}_{j,L}=Q^{total}_j-Q^{conv}_j$ w/ IOL',
                r'$Q^{diff}_{j,H}=Q^{total}_j-Q^{conv}_j$ w/out IOL']

    title = r"Comparison of Ion Heat Conductivity w/ and w/out IOL correction"

    adjustments = {0: 1.}
    caption = ["Main ion heat conductivity in the edge for DIII-D shot %s.%s w/ and w/out IOL" % (str(SHOT),str(TIMEID)),
               "and convective heat flow, neutrals calculation included"]

    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.chi3), (prettyID[1], shotnoIOL.chi3)],
                         yrange=[-3., 2.],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_j$", r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                         textSpace=.065,
                         marginBottom=.2,
                         marginLeft=0.095,
                         capAdj=0.15,
                         yLabelAdj=-.25,
                         xLabelAdj=-.05,
                         size=(16, 12))


def chiComp3(shot, shotnoIOL):
    prettyID = [r'$Q^{diff}_{j,L}=Q^{total}_j-Q^{conv}_j-Q^{heatin}_j$ w/ IOL',
                r'$Q^{diff}_{j,H}=Q^{total}_j-Q^{conv}_j-Q^{heatin}_j$ w/out IOL']

    title = r"Comparison of Ion Heat Conductivity w/ and w/out IOL correction"

    adjustments = {0: 1.}
    caption = ["Main ion heat conductivity in the edge for DIII-D shot %s.%s w/ and w/out IOL" % (str(SHOT),str(TIMEID)),
               "convective heat flow, and work done on plasma, neutrals calculation included"]

    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.chi4), (prettyID[1], shotnoIOL.chi4)],
                         yrange=[-3., 2.],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_j$", r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                         textSpace=.065,
                         marginBottom=.2,
                         marginLeft=0.095,
                         capAdj=0.15,
                         yLabelAdj=-.25,
                         xLabelAdj=-.05,
                         size=(16, 12))


def chiComp4(shot, shotnoIOL):
    prettyID = [r'$Q^{diff}_{j,L}=Q^{total}_j-Q^{conv}_j-Q^{heatin}_j-Q^{visc}_j$ w/ IOL',
                r'$Q^{diff}_{j,H}=Q^{total}_j-Q^{conv}_j-Q^{heatin}_j-Q^{visc}_j$ w/out IOL']

    title = r"Comparison of Ion Heat Conductivity w/ and w/out IOL correction"

    adjustments = {0: 0.}
    caption = ["Main ion heat conductivity in the edge for DIII-D shot %s.%s w/ and w/out IOL correction" % (str(SHOT),str(TIMEID)),
               "convective heat flow,  work done on plasma and visc. heat, neutrals calculation included"]

    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.chi5), (prettyID[1], shotnoIOL.chi5)],
                         yrange=[-5., 5.],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_j$", r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                         textSpace=.065,
                         marginBottom=.2,
                         marginLeft=0.095,
                         capAdj=0.15,
                         yLabelAdj=-.25,
                         xLabelAdj=-.05,
                         size=(16, 12))


def chieComp(shot, shotnoIOL):
    prettyID = [r'$\chi_e$ w/ IOL',
                r'$\chi_e$ w/out IOL']

    title = r"Comparison of Electron Heat Conductivity w/ and w/out IOL correction"

    adjustments = {0: 1.}
    caption = ["Main electron heat conductivity in the edge for DIII-D shot %s.%s w/ and w/out IOL correction" % (str(SHOT),str(TIMEID)),
               "neutrals calculation included"]

    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.chie), (prettyID[1], shotnoIOL.chie)],
                         yrange=[-50.,0.],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_e$", r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                         textSpace=.02,
                         marginBottom=.25,
                         marginLeft=0.095,
                         capAdj=-.15,
                         xLabelAdj=-0.05,
                         yLabelAdj=-0.,
                         size=(16, 12))


###############################################################################
#
#   Deactivate neutrals
#
###############################################################################

def chiComp1neuts(shot, shotnoneuts):
    prettyID = [r'$Q^{diff}_{j,L}=Q^{total}_j$ w/ neutrals',
                r'$Q^{diff}_{j,H}=Q^{total}_j$ w/out neutrals']

    title = r"Comparison of Ion Heat Conductivity w/ and w/out neutrals"

    adjustments = {0: -1.}
    caption = ["Ion heat conductivity in the edge for DIII-D shot %s.%s w/ and w/out neutrals, IOL corrected" % (str(SHOT),str(TIMEID))]

    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.chi2), (prettyID[1], shotnoneuts.chi2)],
                         yrange=[-2., 2.],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_j$", r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                         textSpace=.055,
                         #                    marginBottom=.15,
                         marginLeft=.1,
                         yLabelAdj=-.25,
                         size=(16, 12))


def chiComp2neuts(shot, shotnoneuts):
    prettyID = [r'$Q^{diff}_{j,L}=Q^{total}_j-Q^{conv}_j$ w/ neutrals',
                r'$Q^{diff}_{j,H}=Q^{total}_j-Q^{conv}_j$ w/out neutrals']

    title = r"Comparison of Ion Heat Conductivity w/ and w/out neutrals"

    adjustments = {0: -.5}
    caption = ["Main ion heat conductivity in the edge for DIII-D shot %s.%s w/ and w/out neutrals" % (str(SHOT),str(TIMEID)),
               "IOL corrected, convective heat subtracted"]

    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.chi3), (prettyID[1], shotnoneuts.chi3)],
                         yrange=[-5., 5.],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_j$", r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                         textSpace=.055,
                         marginBottom=.15,
                         marginLeft=0.095,
                         yLabelAdj=-.25,
                         size=(16, 12))


def chiComp3neuts(shot, shotnoneuts):
    prettyID = [r'$Q^{diff}_{j,L}=Q^{total}_j-Q^{conv}_j-Q^{heatin}_j$ w/ neutrals',
                r'$Q^{diff}_{j,H}=Q^{total}_j-Q^{conv}_j-Q^{heatin}_j$ w/out neutrals']

    title = r"Comparison of Ion Heat Conductivity w/ and w/out neutrals"

    adjustments = {0: -1.}
    caption = ["Main ion heat conductivity in the edge for DIII-D shot %s.%s w/ and w/out neutrals" % (str(SHOT),str(TIMEID)),
               "convective heat flow, and work done on plasma, IOL corrected"]

    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.chi4), (prettyID[1], shotnoneuts.chi4)],
                         yrange=[-2., 3.],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_j$", r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                         textSpace=.065,
                         marginBottom=.15,
                         marginLeft=0.095,
                         yLabelAdj=-.25,
                         size=(16, 12))


def chiComp4neuts(shot, shotnoneuts):
    prettyID = [r'$Q^{diff}_{j,L}=Q^{total}_j-Q^{conv}_j-Q^{heatin}_j-Q^{visc}_j$ w/ neutrals',
                r'$Q^{diff}_{j,H}=Q^{total}_j-Q^{conv}_j-Q^{heatin}_j-Q^{visc}_j$ w/out neutrals']

    title = r"Comparison of Ion Heat Conductivity w/ and w/out neutrals"

    adjustments = {0: -1.}
    caption = ["Main ion heat conductivity in the edge for DIII-D shot %s.%s w/ and w/out neutrals" % (str(SHOT),str(TIMEID)),
               "convective heat flow,  work done on plasma and visc., IOL corrected"]

    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.chi5), (prettyID[1], shotnoneuts.chi5)],
                         yrange=[-2., 2.],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_j$", r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                         textSpace=.065,
                         marginBottom=.2,
                         marginLeft=0.095,
                         capAdj=0.1,
                         xLabelAdj=-0.05,
                         yLabelAdj=-.25,
                         size=(16, 12))


def chieCompneuts(shot, shotnoneuts):
    prettyID = [r"$\chi_e$ w/ neutrals",
                r"$\chi_e$ w/out neutrals"]

    title = r"Comparison of Electron Heat Conductivity w/ and w/out neutrals"

    adjustments = {0:-1.}
    caption = ["Electron heat conductivity in the edge for DIII-D shot %s.%s w/ and w/out neutrals" % (str(SHOT),str(TIMEID)),
               "IOL corrected"]

    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.chie), (prettyID[1], shotnoneuts.chie)],
                         yrange=[-45., 5.],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_e$", r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                         textSpace=.02,
                         marginBottom=.2,
                         marginLeft=0.095,
                         xLabelAdj=-0.025,
                         capAdj=0.15,
                         yLabelAdj=-.05,
                         size=(16, 12))

    # prettyID = [r"Term 1",
    #             r"Term 2"]
    #
    # title = r"Comparison of Electron Heat Conductivity Terms"
    #
    # adjustments = {}
    # caption = ["Terms in electron heat conductivity in the edge for DIII-D shot %s.%s" % (str(SHOT),str(TIMEID)),
    #            "IOL corrected. Term1 = 'diffusive' piece, Term2 = 'convective' piece"]
    #
    # term1=[a/(b*shot.xk*c) for a, b, c in zip(shot.qHeate,shot.xne, shot.xte)]
    # term2=[-1.5*a/b for a, b in zip(shot.gameltemp,shot.xne)]
    #
    # graphs.prettyCompare(('rhor', shot.rhor[:199]), [(prettyID[0], term1[:199]), (prettyID[1], term2[:199])],
    #                      yrange=[-10, 100],
    #                      datalabels=[prettyID[0], prettyID[1]],
    #                      title=title,
    #                      ylabel=[r"$\frac{\chi_e}{L_{T_e}}$", r'$\left[\frac{m^2}{s}\right]$'],
    #                      caption=caption,
    #                      adjust=adjustments,
    #                      xTickremove=None,
    #                      textSpace=.02,
    #                      marginBottom=.2,
    #                      marginLeft=0.095,
    #                      xLabelAdj=-0.025,
    #                      capAdj=0.15,
    #                      yLabelAdj=-.05,
    #                      size=(16, 12))





###############################################################################
#
#    Q Comparison
#
###############################################################################


def qComp1(shot, shotnoIOL):
    prettyID = [r'$Q^{total}_{j}$ w/ IOL',
                r'$Q^{total}_{j}$ w/out IOL']

    caption = ["Total heat flux for DIII-D shot %s.%s w/ and w/out IOL correction, neutrals calculation included" % (str(SHOT),str(TIMEID))]
    title = r"$\bf{Q}$ term w/ and w/out IOL correction"
    adjustments = {
    }
    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.q2), (prettyID[1], shotnoIOL.q2)],
                         yrange=[0.E4, 3.E4],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$q$", r"$\left[\frac{W}{m^2}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-.8,
                         marginLeft=0.15,
                         size=(16, 12))


def qComp2(shot, shotnoIOL):
    prettyID = [r'$Q^{conv}_{j}$ w/ IOL',
                r'$Q^{conv}_{j}$ w/out IOL']

    caption = [
        "Convective heat flux for DIII-D shot %s.%s w/ and w/out IOL correction, neutrals calculation included" % (str(SHOT),str(TIMEID))]
    title = r"$\bf{Q}$ term w/ and w/out IOL correction"
    adjustments = {1, -.5}
    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.q3), (prettyID[1], shotnoIOL.q3)],
                         yrange=[0E4, 5.E3],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$q$", r"$\left[\frac{W}{m^2}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-.8,
                         marginLeft=0.15,
                         size=(16, 19))


def qComp3(shot, shotnoIOL):
    prettyID = [r'$Q^{heatin}_{j}$ w/ IOL',
                r'$Q^{heatin}_{j}$ w/out IOL']

    caption = [
        "Work done by pressure for DIII-D shot %s.%s w/ and w/out IOL correction, neutrals calculation included" % (str(SHOT),str(TIMEID))]
    title = r"$\bf{Q}$ term w/ and w/out IOL correction"
    adjustments = {}
    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.q4), (prettyID[1], shotnoIOL.q4)],
                         yrange=[-25., 25],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$q$", r"$\left[\frac{W}{m^2}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-.8,
                         marginLeft=0.15,
                         size=(16, 19))


def qComp4(shot, shotnoIOL):
    prettyID = [r'$Q^{visc}_{j}$ w/ IOL',
                r'$Q^{visc}_{j}$ w/out IOL']

    caption = ["Viscous heating fluxDIII-D shot %s.%s w/ and w/out IOL correction" % (str(SHOT),str(TIMEID))]
    title = r"$\bf{Q}$ term w/ and w/out IOL correction"
    adjustments = {
    }
    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.q5), (prettyID[1], shotnoIOL.q5)],
                         yrange=[-50., 100],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$q$", r"$\left[\frac{W}{m^2}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-.8,
                         marginLeft=0.15,
                         size=(16, 19))


###############################################################################
#
#   Deactivate neutrals
#
###############################################################################
def qComp1neuts(shot, shotnoneuts):
    prettyID = [r'$Q^{total}_{j}$ w/ neutrals',
                r'$Q^{total}_{j}$ w/out neutrals']

    caption = ["Total heat flux for DIII-D shot %s.%s w/ and w/out neutrals" % (str(SHOT),str(TIMEID))]
    title = r"$\bf{Q}$ term w/ and w/out neutrals"
    adjustments = {0, -1.5}
    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.q2), (prettyID[1], shotnoneuts.q2)],
                         yrange=[0.E4, 3.E4],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$q$", r"$\left[\frac{W}{m^2}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-.8,
                         marginLeft=0.15,
                         size=(16, 12))


def qComp2neuts(shot, shotnoneuts):
    prettyID = [r'$Q^{conv}_{j}$ w/ neutrals',
                r'$Q^{conv}_{j}$ w/out neutrals']

    caption = ["Convective heat flux for DIII-D shot %s.%s w/ and w/out neutrals, IOL corrected" % (str(SHOT),str(TIMEID))]
    title = r"$\bf{Q}$ term w/ and w/out neutrals"
    adjustments = {}
    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.q3), (prettyID[1], shotnoneuts.q3)],
                         yrange=[0E4, 5.E3],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$q$", r"$\left[\frac{W}{m^2}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-.8,
                         marginLeft=0.15,
                         size=(16, 19))


def qComp3neuts(shot, shotnoneuts):
    prettyID = [r'$Q^{heatin}_{j}$ w/ neutrals',
                r'$Q^{heatin}_{j}$ w/out neutrals']

    caption = ["Work done by pressure for DIII-D shot %s.%s w/ and w/out neutrals, IOL corrected" % (str(SHOT),str(TIMEID))]
    title = r"$\bf{Q}$ term w/ and w/out neutrals"
    adjustments = {0: 0.5}
    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.q4), (prettyID[1], shotnoneuts.q4)],
                         yrange=[-25., 25],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$q$", r"$\left[\frac{W}{m^2}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-.8,
                         marginLeft=0.15,
                         size=(16, 19))


def qComp4(shot, shotnoneuts):
    prettyID = [r'$Q^{visc}_{j}$ w/ neutrals',
                r'$Q^{visc}_{j}$ w/out neutrals']

    caption = ["Viscous heat flux DIII-D shot %s.%s w/ and w/out neutrals, IOL corrected" % (str(SHOT),str(TIMEID))]
    title = r"$\bf{Q}$ term w/ and w/out neutrals"
    adjustments = {
    }
    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.q5), (prettyID[1], shotnoneuts.q5)],
                         yrange=[-50., 100],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$q$", r"$\left[\frac{W}{m^2}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-.8,
                         marginLeft=0.15,
                         size=(16, 19))


def qieComp1(shot, shotnoIOL):
    prettyID = [r'$Q^{ie}_{j}$ w/ IOL',
                r'$Q^{ie}_{j}$ w/out IOL']

    caption = ["Ion-electron heat exchange for DIII-D shot %s.%s w/ and w/out IOL correction" % (str(SHOT),str(TIMEID))]
    title = r"$\bf{Q}$ term w/ and w/out IOL correction"
    adjustments = {1, -.5}
    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.qie), (prettyID[1], shotnoIOL.qie)],
                         yrange=[0.E5, 5.E5],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$q$", r"$\left[\frac{W}{m^2}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-1.0,
                         xLabelAdj=-.03,
                         capAdj=0.2,
                         marginBottom=.2,
                         marginLeft=0.15,
                         size=(16, 19))

    prettyID= [r'$T_{e}$',
               r'$T_{j}$']
    caption = ["Ion and electron temperatures for DIII-D shot %s.%s" % (str(SHOT),str(TIMEID))]
    title = r"Temperature comparison for %s.%s" % (str(SHOT),str(TIMEID))

    adjustmenets={}
    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.xte), (prettyID[1], shotnoIOL.xti)],
                         yrange=[0., 5.E2],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$T$", r"$\left[eV\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-.5,
                         xLabelAdj=-.03,
                         capAdj=0.2,
                         marginBottom=.2,
                         marginLeft=0.15,
                         size=(16, 19))


def fluxComp(shot, shotnoneuts):
    prettyID = [r'$\Gamma_{r,j}$ w/ neutrals',
                r'$\Gamma_{r,j}$ w/out neutrals']

    caption = ["Ion radial particle flux for DIII-D shot %s.%s w/ and w/out neutrals" % (str(SHOT),str(TIMEID))]
    title = r"$\Gamma_{r,j}$  w/ and w/out neutrals"
    adjustments = {}
    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.gamma), (prettyID[1], shotnoneuts.gamma)],
                         yrange=[1.E18, 1.E20],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$\Gamma_{r,j}$", r"$\left[\frac{\#}{m^2 s}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-.8,
                         xLabelAdj=-0.025,
                         marginLeft=0.15,
                         marginBottom=0.2,
                         size=(16, 19))

    prettyID = [r'$\Gamma_{r,j}$ w/ IOL corr.',
                r'$\Gamma_{r,j}$ w/out IOL corr']

    caption = ["Ion radial particle flux for DIII-D shot %s.%s w/ and w/out IOL Correction" % (str(SHOT),str(TIMEID))]
    title = r"$\Gamma_{r,j}$  w/ and w/out IOL corr"
    adjustments = {}
    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.gamma), (prettyID[1], shotnoIOL.gamma)],
                         yrange=[0.E18, 1.E20],
                         datalabels=[prettyID[0], prettyID[1]],
                         title=title,
                         ylabel=[r"$\Gamma_{r,j}$", r"$\left[\frac{\#}{m^2 s}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-.8,
                         xLabelAdj=-0.025,
                         marginLeft=0.15,
                         marginBottom=0.2,
                         size=(16, 19))

def qSources(shot):


    prettyID = [r'$q^{nbi}_{e}$',
                r'$q_{radcool,e}$',
                r'$q_{ion,e}$',
                r'$q_{ie}$']
    #yrange=yRangeFind([shot.qnbe,shot.coolion,shot.radcool,shot.qie])
    yrange=[0,1E5]
    caption = ["Heat sources/sinks for DIII-D shot %s.%s" % (str(SHOT), str(TIMEID))]
    title = r'Heat sources/sinks for DIII-D Shot %s.%s' % (str(SHOT), str(TIMEID))
    adjustments = {}
    graphs.prettyCompare(('rhor', shot.rhor),
                         [(prettyID[0], shot.qnbe),
                          #(prettyID[1],shot.radcool),
                          (prettyID[2], shot.coolion),
                          (prettyID[3],shot.qie)],
                         yrange=yrange,
                         datalabels=[prettyID[0],
                         #            prettyID[1],
                                     prettyID[2],
                                     prettyID[3]],
                         title=title,
                         ylabel=[r"q "],
                         caption=caption,
                         adjust=adjustments,
                         #                         textSpace=.02,
                         yLabelAdj=-.8,
                         xLabelAdj=-.035,
                         marginLeft=0.15,
                         marginBottom=.2,
                         size=(16, 19),
                         legend=True,
                         corePlot=True)

    prettyID = [r'$Q_{e}$']
    #yrange=yRangeFind([shot.qnbe,shot.coolion,shot.radcool,shot.qie])
    yrange=yRangeFind([shot.qHeate])
    caption = ["Total heat flux for DIII-D shot %s.%s" % (str(SHOT), str(TIMEID))]
    title = r'Heat fluxes for DIII-D Shot %s.%s' % (str(SHOT), str(TIMEID))
    adjustments = {}
    graphs.prettyCompare(('rhor', shot.rhor),
                         [(prettyID[0], shot.qHeate)],
                         yrange=yrange,
                         datalabels=[prettyID[0]],
                         title=title,
                         ylabel = [r"$\Q_{e,r}", r'$\left[\frac{W}{^3}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         #                         textSpace=.02,
                         yLabelAdj=-.8,
                         xLabelAdj=-.035,
                         marginLeft=0.15,
                         marginBottom=.2,
                         size=(16, 19),
                         legend=True)


if __name__ == "__main__":

    FORCERUN=True

    import matplotlib
    #   IOL Sensitivity
    print matplotlib.__path__
    shotargs = {'shotid': 118890,
                'timeid': 1560,
                'runid': 'r90',
                'nbRun': True,
                'IOL': True,
                'quiet': True,
                'reNeut': False,
                'gt3Method': 'coreiolnbineuts'}
    try:
        if FORCERUN: raise("")
        shot = pickle.load(open("Outputs/s%s.%s.dat" % (str(SHOT),str(TIMEID)), "rb"))
    except Exception as e:
        print e
        shot = GTEDGE3_cli.run(shotargs)
        with open("Outputs/s%s.%s.dat" % (str(SHOT),str(TIMEID)), "wb") as f:
            try:
                pickle.dump(shot, f)
            except Exception as e:
                print e
        f.close()

    qSources(shot)
#    plt.show(block=True)
#    trash=raw_input()

    shotargs = {'shotid': 118890,
                'timeid': 1560,
                'runid': 'r90',
                'nbRun': True,
                'IOL': False,
                'quiet': True,
                'reNeut': False,
                'gt3Method': 'corenbineuts'}

    try:
        if FORCERUN: raise("")
        shotnoIOL = pickle.load(open("Outputs/s%s.%s.noIOL.dat" % (str(SHOT),str(TIMEID)), "rb"))
    except Exception as e:
        print e
        shotnoIOL = GTEDGE3_cli.run(shotargs)
        with open("Outputs/s%s.%s.noIOL.dat" % (str(SHOT),str(TIMEID)), "wb") as f:
            pickle.dump(shotnoIOL, f)
        f.close()

    # chiComp1(shot,shotnoIOL)
    # chiComp2(shot,shotnoIOL)
    # chiComp3(shot,shotnoIOL)
    chiComp4(shot, shotnoIOL)

    chieComp(shot, shotnoIOL)
    #    qComp1(shot,shotnoIOL)
    #    qComp2(shot,shotnoIOL)
    #    qComp3(shot,shotnoIOL)

    #   Neutrals sensitivity

    shotargs = {'shotid': 118890,
                'timeid': 1560,
                'runid': 'r90',
                'nbRun': True,
                'IOL': True,
                'quiet': True,
                'reNeut': False,
                'gt3Method': 'coreiolnbi'}
    try:
        if FORCERUN: raise("")
        shotnoneuts = pickle.load(open("Outputs/s%s.%s.noneuts.dat" % (str(SHOT),str(TIMEID)), "rb"))
    except Exception as e:
        print e
        shotnoneuts = GTEDGE3_cli.run(shotargs)
        with open("Outputs/s%s.%s.noneuts.dat" % (str(SHOT),str(TIMEID)), "wb") as f:
            pickle.dump(shotnoneuts, f)
        f.close()

    #    chiComp1neuts(shot,shotnoneuts)
    #    chiComp2neuts(shot,shotnoneuts)
    #    chiComp3neuts(shot,shotnoneuts)
    chiComp4neuts(shot, shotnoneuts)

    chieCompneuts(shot, shotnoneuts)

    #    qComp1neuts(shot,shotnoneuts)
    #    qComp2neuts(shot,shotnoneuts)
    #    qComp3neuts(shot,shotnoneuts)
    #    qComp4neuts(shot,shotnoIOL)
    #    
    qieComp1(shot, shotnoIOL)
    fluxComp(shot, shotnoneuts)

    ####################################################################################
    #
    #
    #   TODO: Electron chi
    #
    ####################################################################################
    print "Graphing!"
    plt.show(block=True)
