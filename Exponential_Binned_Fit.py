#import libraries
import numpy as np
import matplotlib.pyplot as plt
import os,sys,time
import pickle
import ROOT
import array
from ROOT import gStyle,TRandom3, TH1D, TF1, kRed, kBlue, kGreen
from decimal import *
# getcontext().prec=4

# Fill a histogram with n exponential random numbers and fit using ROOT options:

# 1. h1.Fit(Expo)        Neyman chis2
# 2. h1.Fit(Expo,"P")    Pearson chi2
# 3. h1.Fit(Expo,"L")    Likelihood

# Study the bias and the coverage of each method.



# Set style defaults
gStyle.SetOptStat(11);       # only show histogram name and entries
gStyle.SetOptFit(1111);      # display fit results                  
gStyle.SetPadTickX(1);       # right ticks also                    
gStyle.SetPadTickY(1);       # upper ticks also                    
gStyle.SetFuncWidth(3);      # thicker function lines              
gStyle.SetHistLineWidth(3);  # define line width                    

n=40
tau=2.0

# Generate n exponential random numbers with coefficient tau 
x=array.array('d',np.zeros(n))
r=TRandom3(0) #seed=0  ->  different numbers every time

for i in range(0,n):
    x[i]=r.Exp(tau)
                   

# Print generated values (commented in original code)
# for i in x: print(i)

# Draw random values on histogram
h1 = TH1D("h1","Generated Exponential data",20,0,10*tau)
for i in x:
    h1.Fill(i)
h1.Draw()

#Define exponential function. Will use it to fit the histogram.
Expo = TF1("Expo","[a]*exp(-x/[tau])");
Expo.FixParameter(0,n/tau);  # Fix [a] at theoretical value
Expo.SetParameter(1,1);      # Initial value for free parameter [tau]

# (1) Neyman chi2 (default fit, using observed errors)
Expo.SetLineColor(kRed);
fitResult1 = h1.Fit(Expo,"SQ");

# (2) P: Use Pearson chi2 (using expected errors instead of observed errors)
Expo.SetLineColor(kBlue);
fitResult2 = h1.Fit(Expo,"+ SQ P");

# (3) L: Use Loglikelihood method (default is chisquare method)
Expo.SetLineColor(kGreen);
fitResult3 = h1.Fit(Expo,"+ SQ L");

#Default fit is "h1.Fit(Expo)"
#For a better access to results use FitResultPointer objects 
#To see better the output, remove the "quiet" option Q
#Also give a try to "fitResult1.Print()"

print("(1) tau_hat: {0:.4} +/- {1:.3}".format(Decimal(fitResult1.Parameter(1)),Decimal(fitResult1.ParError(1))))
print("(2) tau_hat: {0:.4} +/- {1:.3}".format(Decimal(fitResult2.Parameter(1)),Decimal(fitResult2.ParError(1))))
print("(3) tau_hat: {0:.4} +/- {1:.3}".format(Decimal(fitResult3.Parameter(1)),Decimal(fitResult3.ParError(1))))

# sys.exit(0) # <= Uncomment to see the fits.

################################################################################

nexperiments = 10000;

coverage1 = coverage2 = coverage3 = 0

htau1 = TH1D("htau1","tau_hat: Option 1",200,0,5);
htau2 = TH1D("htau2","tau_hat: Option 2",200,0,5);
htau3 = TH1D("htau3","tau_hat: Option 3",200,0,5);


for iexp in range(0,nexperiments):
    h1.Reset();
    for i in range(0,n):
        h1.Fill(r.Exp(tau))
    Expo.SetParameter(1,1);

    fitResult1 = h1.Fit(Expo,"SQN");    # option Q avoids too much printout
    fitResult2 = h1.Fit(Expo,"SQN P");  # option N avoids adding function histogram
    fitResult3 = h1.Fit(Expo,"SQN L"); 
    
    tau_hat_1 = fitResult1.Parameter(1);
    tau_err_1 = fitResult1.ParError(1);

    tau_hat_2 = fitResult2.Parameter(1);
    tau_err_2 = fitResult2.ParError(1);

    tau_hat_3 = fitResult3.Parameter(1);    
    tau_err_3 = fitResult3.ParError(1);
    
    htau1.Fill(tau_hat_1);
    htau2.Fill(tau_hat_2);
    htau3.Fill(tau_hat_3);

    if (tau > tau_hat_1-tau_err_1 and tau < tau_hat_1+tau_err_1): coverage1+=1;
    if (tau > tau_hat_2-tau_err_2 and tau < tau_hat_2+tau_err_2): coverage2+=1;
    if (tau > tau_hat_3-tau_err_3 and tau < tau_hat_3+tau_err_3): coverage3+=1;  


print("(1) <tau_hat>: {0:.4} ".format(htau1.GetMean()))
print("(2) <tau_hat>: {0:.4} ".format(htau2.GetMean()))
print("(3) <tau_hat>: {0:.4} ".format(htau3.GetMean()))


print("Coverage for the 68% Confidence Intervals:")

# cout<<setprecision(1);
print("(1) {0:.3} %".format(float(coverage1)/nexperiments*100))
print("(2) {0:.3} %".format(float(coverage2)/nexperiments*100))
print("(3) {0:.3} %".format(float(coverage3)/nexperiments*100))

htau1.SetLineColor(kRed);
htau2.SetLineColor(kBlue);
htau3.SetLineColor(kGreen);

htau3.Draw("");
htau2.Draw("same");
htau1.Draw("same");