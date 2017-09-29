#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:14:02 2017

@author: jiahuibi
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)


"""
balance = 42
annualInterestRate = 0.2	      
monthlyPaymentRate = 0.04
	      
month=0
while month<12:
    monthlyPayment = monthlyPaymentRate * balance
    monthlyInterestRate = annualInterestRate/12.0
    unpaidBalance = balance - monthlyPayment
    balance = unpaidBalance*(1+monthlyInterestRate)
    month += 1
print("Remaining balance: "+str(round(balance,2)))