# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:51:36 2024

@author: joach
"""

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = inputFile.readlines()
data = [list(map(int, line.split())) for line in file]

def CheckReportSafe(report):
    if report == sorted(report) or report == sorted(report, reverse=True):
        for i in range(len(report)-1):
            if not 1 <= abs(report[i+1] - report[i]) <= 3:
                return False
        return True
    
    else:
        return False
    
def ProblemDampener(report):
    for i in range(len(report)):
        dampedReport = report.copy()
        dampedReport.pop(i)
        if CheckReportSafe(dampedReport):
            return True
    return False
    
def CountSafeReports(allReports, dampenerOn):
    safeReportsNum = 0
    safeReports = []
    for report in allReports:
        if CheckReportSafe(report):
            safeReportsNum += 1
            safeReports.append(report)
        elif dampenerOn:
            if ProblemDampener(report):
                safeReportsNum += 1
                safeReports.append(report)
        
    return safeReportsNum, safeReports

num, safe1 = CountSafeReports(data, True)
                    
