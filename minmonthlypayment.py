#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:46:48 2017

@author: jiahuibi
"""

initbalance = 3329
annualInterestRate = 0.2
fixedMonthlyPayment = 10
monthlyInterestRate = annualInterestRate/12.0

def calculate(month,balance,fixedMonthlyPayment,monthlyInterestRate):
    balance = initbalance
    month=0
    while month<12:
        unpaidBalance = balance-fixedMonthlyPayment
        balance = unpaidBalance *(monthlyInterestRate+1)
        month += 1
    return balance
while calculate(month,balance,fixedMonthlyPayment,monthlyInterestRate)>0:
    fixedMonthlyPayment += 10
    calculate(month,balance,fixedMonthlyPayment,monthlyInterestRate)
print("Lowest Payment: "+str(fixedMonthlyPayment))
    