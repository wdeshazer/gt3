#!/usr/bin/python
"""
Created on Thu Dec 28 02:13:04 2017

@author: Jonathan
"""
###############################################################################
#
#    Shot 118888.1570 sensitivity study of IOL and neutrals
#
###############################################################################

import GTEDGE3_cli
import graphs as graphs
import matplotlib.pyplot as plt
import pickle

###############################################################################
#
#    Chi Comparison
#
###############################################################################

if __name__=="__main__":

#   IOL Sensitivity

    shotargs={'shotid':118888,
              'timeid':1570,
              'runid':'r88',
              'nbRun':True,
              'IOL':True,
              'quiet':True,
              'reNeut':False,
              'gt3Method':'radialtrans'}
    try:
        shot=pickle.load(open("Outputs/s118888.1570.dat", "rb"))
    except:
        shot=GTEDGE3_cli.runGT3(shotargs)
        with open("Outputs/s118888.1570.dat","wb") as f:
            pickle.dump(shot,f)
        f.close()