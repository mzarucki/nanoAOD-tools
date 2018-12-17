import ROOT
import os
import numpy as np
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module



class lumiWeightProducer(Module):

    def __init__(self, lumiScaleFactor):
        self.lumiScaleFactor = lumiScaleFactor

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("weight", "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass


    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        genWeight = getattr(event, "genWeight")
        weight = self.lumiScaleFactor * genWeight

        self.out.fillBranch("weight", weight)
        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

metSig = lambda : lumiWeightProducer( 1 )

