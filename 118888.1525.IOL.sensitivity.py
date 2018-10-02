#!/usr/bin/python
"""
Created on Thu Dec 28 02:13:04 2017

@author: Jonathan
"""
###############################################################################
#
#    Shot 118888.1525 sensitivity study of IOL and neutrals
#
###############################################################################

import GTEDGE3_cli
import lib.graphs.graphs as graphs
import matplotlib.pyplot as plt
import pickle

###############################################################################
#
#    Chi Comparison
#
###############################################################################

def chiComp1(shot,shotnoIOL):

    prettyID=[r'$Q^{diff}_{j,L}=Q^{total}_j$ w/ IOL',
              r'$Q^{diff}_{j,L}=Q^{total}_j$ w/out IOL']
    
    title=r"Comparison of Ion Heat Conductivity w/ and w/out IOL"
              
    adjustments={}
    caption=["Ion heat conductivity in the edge for DIII-D shot 118888.1525 w/ and w/out IOL correction",
             "Neutrals calculation included"]   
    
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.chi2),(prettyID[1],shotnoIOL.chi2)],
                         yrange=[-2,2.],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_j$",r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                         textSpace=.065,
                         marginBottom=.2,
                         marginLeft=0.095,
                         capAdj=0.15,
                         yLabelAdj=-.25,
                         xLabelAdj=-.05,
                         size=(16,12))

def chiComp2(shot,shotnoIOL):
    prettyID=[r'$Q^{diff}_{j,L}=Q^{total}_j-Q^{conv}_j$ w/ IOL',
              r'$Q^{diff}_{j,H}=Q^{total}_j-Q^{conv}_j$ w/out IOL']
    
    title=r"Comparison of Ion Heat Conductivity w/ and w/out IOL correction"
              
    adjustments={0:1.}
    caption=["Main ion heat conductivity in the edge for DIII-D shot 118888.1525 w/ and w/out IOL",
            "and convective heat flow, neutrals calculation included"]   
    
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.chi3),(prettyID[1],shotnoIOL.chi3)],
                         yrange=[-2.,2.],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_j$",r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                         textSpace=.065,
                         marginBottom=.2,
                         marginLeft=0.095,
                         capAdj=0.15,
                         yLabelAdj=-.25,
                         xLabelAdj=-.05,
                         size=(16,12))
def chiComp3(shot,shotnoIOL):
    prettyID=[r'$Q^{diff}_{j,L}=Q^{total}_j-Q^{conv}_j-Q^{heatin}_j$ w/ IOL',
              r'$Q^{diff}_{j,H}=Q^{total}_j-Q^{conv}_j-Q^{heatin}_j$ w/out IOL']
    
    title=r"Comparison of Ion Heat Conductivity w/ and w/out IOL correction"
              
    adjustments={0:1.}
    caption=["Main ion heat conductivity in the edge for DIII-D shot 118888.1525 w/ and w/out IOL",
            "convective heat flow, and work done on plasma, neutrals calculation included"]   
    
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.chi4),(prettyID[1],shotnoIOL.chi4)],
                         yrange=[-2.,2.],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_j$",r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                         textSpace=.065,
                         marginBottom=.2,
                         marginLeft=0.095,
                         capAdj=0.15,
                         yLabelAdj=-.25,
                         xLabelAdj=-.05,
                         size=(16,12))
    
def chiComp4(shot,shotnoIOL):
    prettyID=[r'$Q^{diff}_{j,L}=Q^{total}_j-Q^{conv}_j-Q^{heatin}_j-Q^{visc}_j$ w/ IOL',
              r'$Q^{diff}_{j,H}=Q^{total}_j-Q^{conv}_j-Q^{heatin}_j-Q^{visc}_j$ w/out IOL']
    
    title=r"Comparison of Ion Heat Conductivity w/ and w/out IOL correction"
              
    adjustments={0:1.}       
    caption=["Main ion heat conductivity in the edge for DIII-D shot 118888.1525 w/ and w/out IOL correction",
            "convective heat flow,  work done on plasma and visc. heat, neutrals calculation included"]   
    
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.chi5),(prettyID[1],shotnoIOL.chi5)],
                         yrange=[-2.,2.],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_j$",r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                         textSpace=.065,
                         marginBottom=.2,
                         marginLeft=0.095,
                         capAdj=0.15,
                         yLabelAdj=-.25,
                         xLabelAdj=-.05,
                         size=(16,12))


def chieComp(shot, shotnoIOL):
    prettyID = [r'$\chi_e$ w/ IOL',
                r'$\chi_e$ w/out IOL']

    title = r"Comparison of Electron Heat Conductivity w/ and w/out IOL correction"

    adjustments = {0: 1.}
    caption = ["Main electron heat conductivity in the edge for DIII-D shot 118888.1525 w/ and w/out IOL correction",
               "neutrals calculation included"]

    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.chie), (prettyID[1], shotnoIOL.chie)],
                         yrange=[0., 20.],
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
                         
def chiComp1neuts(shot,shotnoneuts):

    prettyID=[r'$Q^{diff}_{j,L}=Q^{total}_j$ w/ neutrals',
              r'$Q^{diff}_{j,H}=Q^{total}_j$ w/out neutrals']
    
    title=r"Comparison of Ion Heat Conductivity w/ and w/out neutrals"
              
    adjustments={0:-1.}
    caption=["Ion heat conductivity in the edge for DIII-D shot 118888.1525 w/ and w/out neutrals, IOL corrected"]
    
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.chi2),(prettyID[1],shotnoneuts.chi2)],
                         yrange=[-2.,2.],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_j$",r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                         textSpace=.055,
    #                    marginBottom=.15,
                         marginLeft=.1,
                         yLabelAdj=-.25,
                         size=(16,12))

def chiComp2neuts(shot,shotnoneuts):
    prettyID=[r'$Q^{diff}_{j,L}=Q^{total}_j-Q^{conv}_j$ w/ neutrals',
              r'$Q^{diff}_{j,H}=Q^{total}_j-Q^{conv}_j$ w/out neutrals']
    
    title=r"Comparison of Ion Heat Conductivity w/ and w/out neutrals"
              
    adjustments={0:-.5}
    caption=["Main ion heat conductivity in the edge for DIII-D shot 118888.1525 w/ and w/out neutrals",
            "IOL corrected, convective heat subtracted"]
    
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.chi3),(prettyID[1],shotnoneuts.chi3)],
                         yrange=[-2., 2.],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_j$",r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                                 textSpace=.055,
                                 marginBottom=.15,
                                 marginLeft=0.095,
                         yLabelAdj=-.25,
                         size=(16,12))

def chiComp3neuts(shot,shotnoneuts):
    prettyID=[r'$Q^{diff}_{j,L}=Q^{total}_j-Q^{conv}_j-Q^{heatin}_j$ w/ neutrals',
              r'$Q^{diff}_{j,H}=Q^{total}_j-Q^{conv}_j-Q^{heatin}_j$ w/out neutrals']
    
    title=r"Comparison of Ion Heat Conductivity w/ and w/out neutrals"
              
    adjustments={0:-1.}
    caption=["Main ion heat conductivity in the edge for DIII-D shot 118888.1525 w/ and w/out neutrals",
            "convective heat flow, and work done on plasma, IOL corrected"]
    
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.chi4),(prettyID[1],shotnoneuts.chi4)],
                         yrange=[-2., 2.],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_j$",r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                                 textSpace=.065,
                                 marginBottom=.15,
                                 marginLeft=0.095,
                         yLabelAdj=-.25,
                         size=(16,12))
    
def chiComp4neuts(shot,shotnoneuts):
    prettyID=[r'$Q^{diff}_{j,L}=Q^{total}_j-Q^{conv}_j-Q^{heatin}_j-Q^{visc}_j$ w/ neutrals',
              r'$Q^{diff}_{j,H}=Q^{total}_j-Q^{conv}_j-Q^{heatin}_j-Q^{visc}_j$ w/out neutrals']
    
    title=r"Comparison of Ion Heat Conductivity w/ and w/out neutrals"
              
    adjustments={0:-1.}
    caption=["Main ion heat conductivity in the edge for DIII-D shot 118888.1525 w/ and w/out neutrals",
            "convective heat flow,  work done on plasma and visc., IOL corrected"]
    
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.chi5),(prettyID[1],shotnoneuts.chi5)],
                         yrange=[-2., 2.],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_j$",r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                                 textSpace=.065,
                                 marginBottom=.2,
                                 marginLeft=0.095,
                         capAdj=0.1,
                         xLabelAdj=-0.05,
                         yLabelAdj=-.25,
                         size=(16,12))


def chieCompneuts(shot, shotnoneuts):
    prettyID = [r"$\chi_e$ w/ neutrals",
                r"$\chi_e$ w/out neutrals"]

    title = r"Comparison of Electron Heat Conductivity w/ and w/out neutrals"

    adjustments = {0: -1.}
    caption = ["Main electron heat conductivity in the edge for DIII-D shot 118888.1525 w/ and w/out neutrals",
               "IOL corrected"]

    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.chie), (prettyID[1], shotnoneuts.chie)],
                         yrange=[0., 20.],
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

                       
###############################################################################
#
#    Q Comparison
#
###############################################################################


def qComp1(shot,shotnoIOL): 
    prettyID=[r'$Q^{total}_{j}$ w/ IOL',
              r'$Q^{total}_{j}$ w/out IOL']
    
    caption=["Total heat flux for DIII-D shot 118888.1525 w/ and w/out IOL correction, neutrals calculation included" ]
    title=r"$\bf{Q}$ term w/ and w/out IOL correction"
    adjustments={
            }
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.q2),(prettyID[1],shotnoIOL.q2)],
                         yrange=[0.E4,3.E4],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$q$",r"$\left[\frac{W}{m^2}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-.8,
                         marginLeft=0.15,
                         size=(16,12))  

def qComp2(shot,shotnoIOL):
    prettyID=[r'$Q^{conv}_{j}$ w/ IOL',
              r'$Q^{conv}_{j}$ w/out IOL']
    
    caption=["Convective heat flux for DIII-D shot 118888.1525 w/ and w/out IOL correction, neutrals calculation included" ]
    title=r"$\bf{Q}$ term w/ and w/out IOL correction"
    adjustments={1,-.5}
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.q3),(prettyID[1],shotnoIOL.q3)],
                         yrange=[0E4,5.E3],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$q$",r"$\left[\frac{W}{m^2}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-.8,
                         marginLeft=0.15,
                         size=(16,19))  

def qComp3(shot,shotnoIOL):
    prettyID=[r'$Q^{heatin}_{j}$ w/ IOL',
              r'$Q^{heatin}_{j}$ w/out IOL']
    
    caption=["Work done by pressure for DIII-D shot 118888.1525 w/ and w/out IOL correction, neutrals calculation included"]
    title=r"$\bf{Q}$ term w/ and w/out IOL correction"
    adjustments={}
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.q4),(prettyID[1],shotnoIOL.q4)],
                         yrange=[-25.,25],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$q$",r"$\left[\frac{W}{m^2}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-.8,
                         marginLeft=0.15,
                         size=(16,19))  

def qComp4(shot,shotnoIOL):
    prettyID=[r'$Q^{visc}_{j}$ w/ IOL',
              r'$Q^{visc}_{j}$ w/out IOL']
    
    caption=["Viscous heating fluxDIII-D shot 118888.1525 w/ and w/out IOL correction"]
    title=r"$\bf{Q}$ term w/ and w/out IOL correction"
    adjustments={
            }
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.q5),(prettyID[1],shotnoIOL.q5)],
                         yrange=[-50.,100],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$q$",r"$\left[\frac{W}{m^2}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-.8,
                         marginLeft=0.15,
                         size=(16,19)) 

###############################################################################
#
#   Deactivate neutrals
#
###############################################################################
def qComp1neuts(shot,shotnoneuts): 
    prettyID=[r'$Q^{total}_{j}$ w/ neutrals',
              r'$Q^{total}_{j}$ w/out neutrals']
    
    caption=["Total heat flux for DIII-D shot 118888.1525 w/ and w/out neutrals" ]
    title=r"$\bf{Q}$ term w/ and w/out neutrals"
    adjustments={0,-1.5}
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.q2),(prettyID[1],shotnoneuts.q2)],
                         yrange=[0.E4,3.E4],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$q$",r"$\left[\frac{W}{m^2}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-.8,
                         marginLeft=0.15,
                         size=(16,12))  

def qComp2neuts(shot,shotnoneuts):
    prettyID=[r'$Q^{conv}_{j}$ w/ neutrals',
              r'$Q^{conv}_{j}$ w/out neutrals']
    
    caption=["Convective heat flux for DIII-D shot 118888.1525 w/ and w/out neutrals, IOL corrected" ]
    title=r"$\bf{Q}$ term w/ and w/out neutrals"
    adjustments={}
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.q3),(prettyID[1],shotnoneuts.q3)],
                         yrange=[0E4,5.E3],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$q$",r"$\left[\frac{W}{m^2}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-.8,
                         marginLeft=0.15,
                         size=(16,19))  

def qComp3neuts(shot,shotnoneuts):
    prettyID=[r'$Q^{heatin}_{j}$ w/ neutrals',
              r'$Q^{heatin}_{j}$ w/out neutrals']
    
    caption=["Work done by pressure for DIII-D shot 118888.1525 w/ and w/out neutrals, IOL corrected"]
    title=r"$\bf{Q}$ term w/ and w/out neutrals"
    adjustments={0:0.5}
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.q4),(prettyID[1],shotnoneuts.q4)],
                         yrange=[-25.,25],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$q$",r"$\left[\frac{W}{m^2}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-.8,
                         marginLeft=0.15,
                         size=(16,19))  

def qComp4(shot,shotnoneuts):
    prettyID=[r'$Q^{visc}_{j}$ w/ neutrals',
              r'$Q^{visc}_{j}$ w/out neutrals']
    
    caption=["Viscous heat flux DIII-D shot 118888.1525 w/ and w/out neutrals, IOL corrected"]
    title=r"$\bf{Q}$ term w/ and w/out neutrals"
    adjustments={
            }
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.q5),(prettyID[1],shotnoneuts.q5)],
                         yrange=[-50.,100],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$q$",r"$\left[\frac{W}{m^2}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-.8,
                         marginLeft=0.15,
                         size=(16,19)) 



def qieComp1(shot,shotnoIOL):
    prettyID=[r'$Q^{ie}_{j}$ w/ IOL',
              r'$Q^{ie}_{j}$ w/out IOL']
    
    caption=["Ion-electron heat exchange for DIII-D shot 118888.1525 w/ and w/out IOL correction"]
    title=r"$\bf{Q}$ term w/ and w/out IOL correction"
    adjustments={1,-.5}
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.qie),(prettyID[1],shotnoIOL.qie)],
                         yrange=[-2.E5, 2.E5],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$q$",r"$\left[\frac{W}{m^2}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-1.0,
                         xLabelAdj=-.03,
                         capAdj=0.2,
                         marginBottom=.2,
                         marginLeft=0.15,
                         size=(16,19)) 

def fluxComp(shot,shotnoneuts):
    prettyID = [r'$\Gamma_{r,j}$ w/ neutrals',
                r'$\Gamma_{r,j}$ w/out neutrals']

    caption = ["Ion radial particle flux for DIII-D shot 118888.1525 w/ and w/out neutrals"]
    title = r"$\Gamma_{r,j}$  w/ and w/out neutrals"
    adjustments = {}
    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.gamma), (prettyID[1], shotnoneuts.gamma)],
                         yrange=[0.E18, 3.E19],
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

    caption = ["Ion radial particle flux for DIII-D shot 118888.1525 w/ and w/out IOL Correction"]
    title = r"$\Gamma_{r,j}$  w/ and w/out IOL corr"
    adjustments = {}
    graphs.prettyCompare(('rhor', shot.rhor), [(prettyID[0], shot.gamma), (prettyID[1], shotnoIOL.gamma)],
                         yrange=[0.E18, 5.E19],
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

if __name__=="__main__":

#   IOL Sensitivity

    shotargs={'shotid':118888,
              'timeid':1525,
              'runid':'r88',
              'nbRun':True,
              'IOL':True,
              'quiet':True,
              'reNeut':False,
              'gt3Method':'coreiolnbineuts'}
    try:
        shot=pickle.load(open("Outputs/s118888.1525.dat", "rb"))
    except:
        shot=GTEDGE3_cli.run(shotargs)
        with open("Outputs/s118888.1525.dat","wb") as f:
            pickle.dump(shot,f)
        f.close()
    

    shotargs={'shotid':118888,
              'timeid':1525,
              'runid':'r88',
              'nbRun':True,
              'IOL':False,
              'quiet':True,
              'reNeut':False,
              'gt3Method':'corenbineuts'}
    
    try:
        shotnoIOL=pickle.load(open("Outputs/s118888.1525.noIOL.dat","rb"))
    except:
        shotnoIOL=GTEDGE3_cli.run(shotargs)
        with open("Outputs/s118888.1525.noIOL.dat","wb") as f:
            pickle.dump(shotnoIOL,f)
        f.close()
    
    #chiComp1(shot,shotnoIOL)
    #chiComp2(shot,shotnoIOL)
    #chiComp3(shot,shotnoIOL)
    #chiComp4(shot,shotnoIOL)

    chieComp(shot,shotnoIOL)
#    qComp1(shot,shotnoIOL)
#    qComp2(shot,shotnoIOL)
#    qComp3(shot,shotnoIOL)

    
#   Neutrals sensitivity
    


    shotargs={'shotid':118888,
              'timeid':1525,
              'runid':'r88',
              'nbRun':True,
              'IOL':True,
              'quiet':True,
              'reNeut':False,
              'gt3Method':'coreiolnbi'}
    try:
        shotnoneuts=pickle.load(open("Outputs/s118888.1525.noneuts.dat","rb"))
    except:
        shotnoneuts=GTEDGE3_cli.run(shotargs)
        with open("Outputs/s118888.1525.noneuts.dat","wb") as f:
            pickle.dump(shotnoneuts,f)
        f.close()
    
#    chiComp1neuts(shot,shotnoneuts)
#    chiComp2neuts(shot,shotnoneuts)
#    chiComp3neuts(shot,shotnoneuts)
    #chiComp4neuts(shot,shotnoneuts)

    chieCompneuts(shot,shotnoneuts)

#    qComp1neuts(shot,shotnoneuts)
#    qComp2neuts(shot,shotnoneuts)
#    qComp3neuts(shot,shotnoneuts)
#    qComp4neuts(shot,shotnoIOL)
#    
    #qieComp1(shot,shotnoIOL)
    fluxComp(shot, shotnoneuts)


####################################################################################
#
#
#   TODO: Electron chi
#
####################################################################################

    plt.show(block=True)