#Author: Marie-Odile P. Fortier (mfortier2@ucmerced.edu)
#Date: 7/25/2014, revised 9/25/2014, revised 2/28/2016, revised 10/15/2020 to Python 3 version (this code)
#Python code to run a baseline LCA scenario analysis
#Works for a comma-delimited text file of parameter inputs and ranges
#Make sure that exponents are ** and not ^.
#Make sure that no dashes appear in variable names, only letters, numbers, and underscores.
#Make sure that your parameter text file has no empty lines (including at the very end of the file).
#IMPORTANT: Label process impact calculations with a variable that begins with "Process_" for the program to recognize it as a process impact scaled to your functional unit.
#In accordance with the Creative Commons license type CC BY-NC-SA (Attribution-NonCommercial-ShareAlike), please cite this script as "GERLCA_scenario_analysis" version 1. 

from math import *
import os

print('This program will run a baseline scenario analysis for a given LCA model based on baseline parameter values.')
print('This program works for a comma-delimited text file of LCA parameter ranges with headers and with the following columns in order: input parameter name, minimum value, baseline value, and maximum value.')
print('IMPORTANT: Label process impact calculations with a variable that begins with "Process_" for the program to recognize it as a process impact scaled to your functional unit.')
workingdirectory=input('Enter the file path to your working folder:')

os.chdir(workingdirectory)

LCA_Parameter_ranges=input('Enter the name of your parameter range file:')
LCA_Baseline_Case_results=input('Enter a text file name for your LCA baseline case results:')

LCA_parameter_ranges=open(LCA_Parameter_ranges,'r')
LCA_parameter_ranges=LCA_parameter_ranges.readlines()
del LCA_parameter_ranges[0]
parameterlist=[]

for oneline in LCA_parameter_ranges:
    oneparameter=oneline.split(',')
    parameterlist.append(oneparameter)

parameternames=[r[0] for r in parameterlist]
pbaseline=list(map(float,[r[2] for r in parameterlist]))

parameterdictbaseline=dict(list(zip(parameternames,pbaseline)))
for x,y in parameterdictbaseline.items():
    exec('%s = y' % x)

#Copy and paste your equations below here:



#Do not alter the rest of the code below.

Total_Impact=0

BaseCase_outputs_populate=[]
for name in list(vars().keys()):
    if name.startswith('Process_'):
        listline=(name,eval(name))
        additional_impact=eval(name)
        Total_Impact=Total_Impact+additional_impact
        BaseCase_outputs_populate.append(listline)

Total_Impact_line=('Total_Impact',Total_Impact)
BaseCase_outputs_populate.append(Total_Impact_line)

BaseCase_outputs=open(LCA_Baseline_Case_results,'w')
BaseCase_outputslist=[]

for i in BaseCase_outputs_populate:
        BaseCase_outputslist.append(list(i))

outputlines=[]
for i in range(len(BaseCase_outputslist)):
    outputlines.append(','.join(map(str,BaseCase_outputslist[i])))
BaseCase_outputs.writelines('\n'.join(outputlines))
BaseCase_outputs.close()

print('Your LCA baseline case results are ready!')
