#Author: Marie-Odile P. Fortier (mfortier2@ucmerced.edu)
#Date: 7/22/2014 to 7/24/2014, modified on 3/29/2016, 4/25/2018, 7/11/2018, and 9-10/2018; revised to Python 3 version in October 2020; weighed distributions fixed on 12/8/2021; revised comments on 12/31/2021 for GitHub distribution (this code).
#Python 3 code to run a Monte Carlo analysis for a life cycle assessment (LCA) model, for one impact category, which also provides the input parameter values used in each Monte Carlo simulation among the results.
#Licensed under GNU General Public License v3.0: "Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights." 

#Information on setup and use of this code:
#Works for a comma-delimited text file of parameter inputs and ranges
#Make sure that exponents are ** and not ^.
#Make sure that no dashes appear in variable names, only letters, numbers, and underscores.
#Make sure that your parameter text file has no empty lines (including at the very end of the file).
#IMPORTANT: Label process impact calculations with a variable that begins with "Process_" for the program to recognize it as a process impact scaled to your functional unit.
#IMPORTANT: Please see the comments for each distribution type and how the input parameter file should be set up for that distribution type, within the code below.


from math import *
from random import *
from collections import OrderedDict
import os

print('This program will produce a Monte Carlo analysis for a life cycle assessment with different probability distributions of parameter inputs: weighed, raw data, uniform, normal, triangular, lognormal, and Weibull.')
print('This program works for a comma-delimited text file of LCA parameter ranges with headers and with the following columns in order: input parameter name, minimum value, baseline value, maximum value, and distribution type.')
print('')
print('For parameters with raw data to define their probability distribution, label these as "rawdata" for distribution type and prepare a text file containing a single column of each possible value, naming the text file as the parameter name.')
print('For each "weighed" parameter, create a text file titled with the parameter name that contains a column with the values followed by a comma and their probability of occurring.')
print('')
workingdirectory=input('Enter the file path to your working folder:')

os.chdir(workingdirectory)

LCA_Parameter_ranges=input('Enter the name of your parameter range file (with .txt at the end):')
MonteCarlo_runs=int(input('Enter the number of Monte Carlo runs:'))
LCA_MonteCarlo_results=input('Enter a text file name for your Monte Carlo results (with .txt at the end):')

LCA_parameter_ranges=open(LCA_Parameter_ranges,'r')
LCA_parameter_ranges=LCA_parameter_ranges.readlines()
del LCA_parameter_ranges[0]
parameterlist=[]

for oneline in LCA_parameter_ranges:
    oneparameter=oneline.split(',')
    parameterlist.append(oneparameter)

parameternames=[r[0] for r in parameterlist]
pmin=list(map(float,[r[1] for r in parameterlist]))
pnominal=list(map(float,[r[2] for r in parameterlist]))
pmax=list(map(float,[r[3] for r in parameterlist]))
distributiontype=list(map(str,[r[4] for r in parameterlist]))
prange=list(zip(parameternames,pmin,pnominal,pmax,distributiontype))

parameterdictnominal=dict(list(zip(parameternames,pnominal)))
for x,y in parameterdictnominal.items():
    exec('%s = y' % x)

MonteCarlo_outputs=open(LCA_MonteCarlo_results,'w')
MonteCarlo_outputlist=[]
n=1
parameterheader=["Total_result"]+parameternames
MonteCarlo_outputlist.append(parameterheader)

for n in range(1,(MonteCarlo_runs+1)):
    pvaluespicked=[]
    for pname,minimum,baseline,maximum,distributiontype in prange:
        if distributiontype=="weighed\n" or distributiontype=="weighed":
            Weighed_parameter_probabilities=str(pname)+'.txt'
            Weighed_parameter_probabilities=open(Weighed_parameter_probabilities,'r')
            Weighed_parameter_probabilities=Weighed_parameter_probabilities.readlines()
            weighed_parameter_prob_list=[]
            for oneline in Weighed_parameter_probabilities:
                onevalue=oneline.split(',')
                weighed_parameter_prob_list.append(onevalue)
            weighedparametervalue=list(map(float,[r[0] for r in weighed_parameter_prob_list]))
            weighedprob=list(map(float,[r[1] for r in weighed_parameter_prob_list]))
            weighedprobdictionary=dict(list(zip(weighedparametervalue,weighedprob)))
            pvalue=choice(weighedparametervalue,weights=weighedprob,k=1)
            pvalue=pvalue[0]
        if distributiontype=="rawdata\n" or distributiontype=="rawdata":
            Rawdata_parameter_probabilities=str(pname)+'.txt'
            Rawdata_parameter_probabilities=open(Rawdata_parameter_probabilities,'r')
            Rawdata_parameter_probabilities=Rawdata_parameter_probabilities.readlines()
            Rawdata_parameter_prob_list=[]
            for oneline in Rawdata_parameter_probabilities:
                Rawdata_parameter_prob_list.append(float(oneline))
            pvalue=choice(Rawdata_parameter_prob_list)
        if distributiontype=="uniform\n" or distributiontype=="uniform":
            pvalue=uniform(minimum,maximum)
        if distributiontype=="normal\n" or distributiontype=="normal":
            pvalue=normalvariate(baseline,((maximum-baseline)/2.0)) #this is based on the maximum being two standard deviations above the baseline.
            while pvalue<minimum:
                pvalue=normalvariate(baseline,((maximum-baseline)/2.0))  #this is based on the maximum being two standard deviations above the baseline.

        #Edit the parameter names in quotation marks:

            if pname=="" or pname=="" or pname=="":
                while pvalue>maximum:
                    pvalue=normalvariate(baseline,((maximum-baseline)/2.0))  #this is based on the maximum being two standard deviations above the baseline. 

        if distributiontype=="triangular\n" or distributiontype=="triangular":
            pvalue=triangular(minimum,maximum,baseline)
        if distributiontype=="lognormal\n" or distributiontype=="lognormal":
            pvalue=lognormvariate(baseline,maximum)
            #for lognormvariate, the location is the baseline and the scale is the maximum, from the Minitab lognormal distribution fits.
            while pvalue<minimum:
                pvalue=lognormvariate(baseline,maximum)
        if distributiontype=="Weibull\n" or distributiontype=="Weibull":
            pvalue=weibullvariate(baseline,maximum)
            #for Weibull distribution, the scale (or alpha) is the baseline and the shape (or beta) is the maximum.
            while pvalue<minimum:
                pvalue=weibullvariate(baseline,maximum)
        pvaluespicked.append(pvalue)
        
    parameterdict=dict(list(zip(parameternames,pvaluespicked)))
    for x,y in parameterdict.items():
        exec('%s = y' % x)

    #Copy and paste your equations below here with ONE INDENT:



    #Do not alter the rest of the code below.
        
    Total_Impact=0
    for name in list(vars().keys()):
        if name.startswith('Process_'):
            additional_impact=eval(name)
            Total_Impact=Total_Impact+additional_impact
    resultswithparametervalues=[Total_Impact]+pvaluespicked
    MonteCarlo_outputlist.append(resultswithparametervalues)
    parameterdict.clear()
    print(str(n)+'...')

outputlines=[]
for i in range(len(MonteCarlo_outputlist)):
    outputlines.append(','.join(map(str,MonteCarlo_outputlist[i])))
MonteCarlo_outputs.writelines('\n'.join(outputlines))
MonteCarlo_outputs.close()

print('Your LCA Monte Carlo results are ready!')
