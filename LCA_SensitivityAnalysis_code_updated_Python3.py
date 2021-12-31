#Author: Marie-Odile P. Fortier (mfortier2@ucmerced.edu)
#Date: Revised from original July 2014 code on 10/16/14, 10/22/2014, 3/27/2016, 3/29/2016, revised to Python 3 version on 10/15/2020, and revised comments on 12/31/2021 for GitHub distribution (this code).
#Python 3 code to run a sensitivity analysis for a life cycle assessment (LCA) model, for one impact category.
#Licensed under GNU General Public License v3.0: "Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights." 

#Information on setup and use of this code:
#Works for a comma-delimited text file of parameter inputs and ranges
#Make sure that exponents are ** and not ^.
#Make sure that no dashes appear in variable names, only letters, numbers, and underscores.
#Make sure that your parameter text file has no empty lines (including at the very end of the file).
#IMPORTANT: Label process impact calculations with a variable that begins with "Process_" for the program to recognize it as a process impact scaled to your functional unit.

from math import *
from collections import OrderedDict
import os

print('This program will produce a sensitivity analysis for a life cycle assessment by analyzing new results as each parameter is changed to its minimum or maximum value, one at a time.')
print('This program works for a comma-delimited text file of LCA parameter ranges with headers and with the following columns in order: input parameter name, minimum value, baseline value, and maximum value.')
print('IMPORTANT: Label process impact calculations with a variable that begins with "Process_" for the program to recognize it as a process impact scaled to your functional unit.')
print('')
workingdirectory=input('Enter the file path to your working folder, where your parameter text file can be found:')

os.chdir(workingdirectory)

LCA_Parameter_ranges=input('Enter the name of your parameter range file (with .txt at the end):')
LCA_sensitivity_results=input('Enter a text file name for your sensitivity analysis results (with .txt at the end):')

LCA_parameter_ranges=open(LCA_Parameter_ranges,'r')
LCA_parameter_ranges=LCA_parameter_ranges.readlines()
del LCA_parameter_ranges[0]
parameterlist=[]

for oneline in LCA_parameter_ranges:
    oneparameter=oneline.split(',')
    parameterlist.append(oneparameter)

parameternames=[r[0] for r in parameterlist]
pmin=list(map(float,[r[1] for r in parameterlist]))
pbase=list(map(float,[r[2] for r in parameterlist]))
pmax=list(map(float,[r[3] for r in parameterlist]))
prange=list(zip(pmin,pmax))

minparameterresults=[]
parametermindict=OrderedDict(list(zip(parameternames,pmin)))
baseparameterresults=[]
parameterdictbase=OrderedDict(list(zip(parameternames,pbase)))
maxparameterresults=[]
parametermaxdict=OrderedDict(list(zip(parameternames,pmax)))

def LCA_equations(parameternames):
    #INSERT EQUATIONS HERE, with a ONE-TAB INDENT:



    #Do not alter the rest of the code below.
    
    Total_Impact=0
    for name in list(vars().keys()):
        if name.startswith('Process_'):
            additional_impact=eval(name)
            Total_Impact=Total_Impact+additional_impact
    return float(Total_Impact)


parameterdictbase=OrderedDict(list(zip(parameternames,pbase)))
for x,y in parameterdictbase.items():
    exec('%s = y' % x)

Total_Impact=LCA_equations(pbase)
        
baseparameterresults=[]
for i in parameternames:
    baseparameterresults.append(Total_Impact)


minparameterresults=[]
parametermindict=OrderedDict(list(zip(parameternames,pmin)))
for x,y in parametermindict.items():
    for z,w in parameterdictbase.items():
        exec('%s = w' % z)
    exec('%s = y' % x)
    sendthesevalues=[]
    for i in parameternames:
        x=globals()[i]
        sendthesevalues.append(x)
    Total_Impact=LCA_equations(sendthesevalues)
    minparameterresults.append(Total_Impact)


maxparameterresults=[]
parametermaxdict=OrderedDict(list(zip(parameternames,pmax)))
for x,y in parametermaxdict.items():
    for z,w in parameterdictbase.items():
        exec('%s = w' % z)
    exec('%s = y' % x)
    sendthesevalues=[]
    for i in parameternames:
        x=globals()[i]
        sendthesevalues.append(x)
    Total_Impact=LCA_equations(sendthesevalues)
    maxparameterresults.append(Total_Impact)


Sensitivity_outputs1=list(zip(parameternames,minparameterresults,baseparameterresults,maxparameterresults))
Sensitivity_outputslist=[]
for i in Sensitivity_outputs1:
    Sensitivity_outputslist.append(list(i))
Sensitivity_outputs=open(LCA_sensitivity_results,'w')
outputlines=[]
for i in range(len(Sensitivity_outputslist)):
    outputlines.append(','.join(map(str,Sensitivity_outputslist[i])))
Sensitivity_outputs.writelines('\n'.join(outputlines))
Sensitivity_outputs.close()

print('Your LCA sensitivity analysis results are ready!')
