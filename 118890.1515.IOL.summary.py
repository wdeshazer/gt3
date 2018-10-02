# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 02:13:04 2017

@author: Jonathan
"""
###############################################################################
#
#    Shot 118890.1515 comparison of chis and qs w/ and w/out IOL
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

    prettyID=[r'$Q^{cond}_{j,L}=Q^{total}_j$ w/ IOL',
              r'$Q^{cond}_{j,H}=Q^{total}_j$ w/out IOL']
    
    title=r"Comparison of Ion Heat Diffusivity w/ and w/out IOL"
              
    adjustments={}       
    caption=["Ion heat diffusivities in the edge for DIII-D shot 118890 w/ and w/out IOL corr."]   
    
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.chi2),(prettyID[1],shotnoIOL.chi2)],
                                 yrange=[0.,3.],
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

def chiComp2(shot,shotnoIOL):
    prettyID=[r'$Q^{cond}_{j,L}=Q^{total}_j-Q^{conv}_j$ w/ IOL',
              r'$Q^{cond}_{j,H}=Q^{total}_j-Q^{conv}_j$ w/out IOL']
    
    title=r"Comparison of Ion Heat Diffusivity w/ and w/out IOL"
              
    adjustments={0:1.}       
    caption=["Main ion heat diffusivities in the edge for DIII-D shot 118890 w/ and w/out IOL corr.",
            "and convective heat flow"]   
    
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.chi3),(prettyID[1],shotnoIOL.chi3)],
                                 yrange=[0.,3.],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_j$",r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                                 textSpace=.055,
    #                             marginBottom=.15,
                                 marginLeft=0.095,
                         yLabelAdj=-.25,
                         size=(16,12))
def chiComp3(shot,shotnoIOL):
    prettyID=[r'$Q^{cond}_{j,L}=Q^{total}_j-Q^{conv}_j-Q^{heatin}_j$ w/ IOL',
              r'$Q^{cond}_{j,H}=Q^{total}_j-Q^{conv}_j-Q^{heatin}_j$ w/out IOL']
    
    title=r"Comparison of Ion Heat Diffusivity w/ and w/out IOL"
              
    adjustments={0:1.}       
    caption=["Main ion heat diffusivities in the edge for DIII-D shot 118890 w/ and w/out IOL corr.",
            "convective heat flow, and work done on plasma"]   
    
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.chi4),(prettyID[1],shotnoIOL.chi4)],
                                 yrange=[0.,3.],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_j$",r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                                 textSpace=.065,
    #                             marginBottom=.15,
                                 marginLeft=0.095,
                         yLabelAdj=-.25,
                         size=(16,12))
    
def chiComp4(shot,shotnoIOL):
    prettyID=[r'$Q^{cond}_{j,L}=Q^{total}_j-Q^{conv}_j-Q^{heatin}_j-Q^{visc}_j$ w/ IOL',
              r'$Q^{cond}_{j,H}=Q^{total}_j-Q^{conv}_j-Q^{heatin}_j-Q^{visc}_j$ w/out IOL']
    
    title=r"Comparison of Ion Heat Diffusivity Between L-H-Mode transition"
              
    adjustments={0:1.}       
    caption=["Main ion heat diffusivities in the edge for DIII-D shot 118890 w/ and w/out IOL corr.",
            "convective heat flow,  work done on plasma and visc. heat "]   
    
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.chi5),(prettyID[1],shotnoIOL.chi5)],
                                 yrange=[0.,3.],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$\chi_j$",r'$\left[\frac{m^2}{s}\right]$'],
                         caption=caption,
                         adjust=adjustments,
                         xTickremove=None,
                                 textSpace=.065,
    #                             marginBottom=.15,
                                 marginLeft=0.095,
                         yLabelAdj=-.25,
                         size=(16,12))

###############################################################################
#
#    Q Comparison
#
###############################################################################


def qComp1(shot,shotnoIOL): 
    prettyID=[r'$Q^{total}_{j}$ w/ IOL',
              r'$Q^{total}_{j}$ w/out IOL']
    
    caption=["Total heat flux for DIII-D shot 118890 w/ and w/out IOL corr." ]
    title=r"$\bf{Q}$ term comparison"
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
    prettyID=[r'$q^{conv}_{j}$ w/ IOL',
              r'$q^{conv}_{j}$ w/out IOL']
    
    caption=["Convective heat flux for DIII-D shot 118890 w/ and w/out IOL corr." ]
    title=r"$\bf{Q}$ term comparison"
    adjustments={
            }
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.q3),(prettyID[1],shotnoIOL.q3)],
                         yrange=[0E4,2.E3],
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
    prettyID=[r'$q^{heatin}_{j}$ w/ IOL',
              r'$q^{heatin}_{j}$ w/out IOL']
    
    caption=["Work done by pressure for DIII-D shot 118890 w/ and w/out IOL corr."]
    title=r"$\bf{Q}$ term comparison"
    adjustments={
            }
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
    prettyID=[r'$q^{visc}_{j}$ w/ IOL',
              r'$q^{visc}_{j}$ w/out IOL']
    
    caption=["Viscous heating fluxDIII-D shot 118890 w/ and w/out IOL corr."]
    title=r"$\bf{Q}$ term comparison"
    adjustments={
            }
    graphs.prettyCompare(('rhor',shot.rhor),[(prettyID[0],shot.q5),(prettyID[1],shotnoIOL.q5)],
                         yrange=[-500.,500.],
                         datalabels=[prettyID[0],prettyID[1]],
                         title=title,
                         ylabel=[r"$q$",r"$\left[\frac{W}{m^2}\right]$"],
                         caption=caption,
                         adjust=adjustments,
                         textSpace=.02,
                         yLabelAdj=-.8,
                         marginLeft=0.15,
                         size=(16,19)) 





if __name__=="__main__":

    shotargs={'shotid':118890,
              'timeid':1515,
              'runid':'r90',
              'nbRun':True,
              'IOL':True,
              'quiet':True}
    shot=GTEDGE3_cli.run(shotargs)
    with open("Outputs/s118890.1515.dat","wb") as f:
        pickle.dump(shot,f)
    f.close()
    

    shotargs={'shotid':118890,
              'timeid':1515,
              'runid':'r90',
              'nbRun':True,
              'IOL':False,
              'quiet':True}
    
    shotnoIOL=GTEDGE3_cli.run(shotargs)
    with open("Outputs/s118890.1515.noIOL.dat","wb") as f:
        pickle.dump(shotnoIOL,f)
    f.close()
    
    chiComp1(shot,shotnoIOL)
    chiComp2(shot,shotnoIOL)
    chiComp3(shot,shotnoIOL)
    chiComp4(shot,shotnoIOL)


    qComp1(shot,shotnoIOL)
    qComp2(shot,shotnoIOL)
    qComp3(shot,shotnoIOL)
    qComp4(shot,shotnoIOL)
#    
#    qieComp1(shot,shotnoIOL)
    
    plt.show(block=True)