# -*- coding: utf-8 -*-
# =============================================================================
# Created by: Natalie LaLuzerne
# =============================================================================
import csv

dirname = r"C:\Users\nlalu\Documents\EECS_581"

diagnosis = "diagnoses.csv"

classification = "classifications.csv"

classifications = []

with open(dirname + "\\" + classification) as classificationfile:
    cs = list(csv.reader(classificationfile))

with open(dirname + "\\" + diagnosis) as diagnosisfile:
    diagnoses = list(csv.reader(diagnosisfile))
    
for file in cs:
    if(file[1] == 'N' and file[2] == 'Y'):
        classifications.append([file[0], "RIGHT"])  
    elif(file[1] == 'Y' and file[2] == 'N'):
        classifications.append([file[0], "LEFT"])  
    else:
        classifications.append([file[0], "NONE"])
        
total = 0
correct = 0
incorrect = 0

leftleftCorrect = 0
rightrightCorrect = 0

rightLeftIncorrect = 0
leftRightIncorrect = 0

noneCorrect = 0
noneRightIncorrect = 0
noneLeftIncorrect = 0
rightNoneIncorrect = 0
leftNoneIncorrect = 0

leftTotal = 0
rightTotal = 0
noneTotal = 0

for i in range(len(diagnoses)):
    if(classifications[i][0] in diagnoses[i][0]):
        total += 1
        if(diagnoses[i][1] == 'LEFT'):
            leftTotal += 1
        elif(diagnoses[i][1] == 'RIGHT'):
            rightTotal += 1
        else:
            noneTotal += 1
        
        if(classifications[i][1] == diagnoses[i][1]):
            if(diagnoses[i][1] == 'LEFT'):
                leftleftCorrect += 1
            elif(diagnoses[i][1] == 'RIGHT'):
                rightrightCorrect += 1
            else:
                noneCorrect += 1
            
            correct += 1
        else:
            if(classifications[i][1] == 'LEFT' and diagnoses[i][1] == 'RIGHT'):
                rightLeftIncorrect += 1
            elif(classifications[i][1] == 'RIGHT' and diagnoses[i][1] == 'LEFT'):
                leftRightIncorrect += 1
            elif(classifications[i][1] == 'NONE' and diagnoses[i][1] == 'RIGHT'):
                rightNoneIncorrect += 1
            elif(classifications[i][1] == 'NONE' and diagnoses[i][1] == 'LEFT'):
                leftNoneIncorrect += 1
            elif(classifications[i][1] == 'LEFT' and diagnoses[i][1] == 'NONE'):
                noneLeftIncorrect += 1
            elif(classifications[i][1] == 'RIGHT' and diagnoses[i][1] == 'NONE'):
                noneRightIncorrect += 1
            
            incorrect += 1
                        
correctPercentage = (correct / total) * 100
incorrectPercentage = (incorrect / total) * 100
rightCorrectPercentage = (rightrightCorrect / rightTotal) * 100
leftCorrectPercentage = (leftleftCorrect / leftTotal) * 100
noneCorrectPercentage = (noneCorrect / noneTotal) * 100
correctPositiveDiagnosesPercentage = ((rightrightCorrect + leftleftCorrect) / (rightTotal + leftTotal)) * 100
rightleftIncorrectPercentage = (rightLeftIncorrect / rightTotal) * 100
leftrightIncorrectPercentage = (leftRightIncorrect / leftTotal) * 100
rightNoneIncorrectPercentage = (rightNoneIncorrect / rightTotal) * 100
leftNoneIncorrectPercentage = (leftNoneIncorrect / leftTotal) * 100
noneRightIncorrectPercentage = (noneRightIncorrect / noneTotal) * 100
noneLeftIncorrectPercentage = (noneLeftIncorrect / noneTotal) * 100
            
print("Total correct: " + str(correct) + " correct out of " + str(total) + ", " + str(correctPercentage) + "%")
print("Total incorrect: " + str(incorrect) + " incorrect out of " + str(total) + ", " + str(incorrectPercentage) + "%")
print('\n')
print("Left Diagnoses correct: " + str(leftleftCorrect) + " correct out of " + str(leftTotal) + ", " + str(leftCorrectPercentage) + "%")
print("Right Diagnoses correct: " + str(rightrightCorrect) + " correct out of " + str(rightTotal) + ", " + str(rightCorrectPercentage) + "%")
print("Positive Diagnoses correct: " + str(leftleftCorrect + rightrightCorrect) + " correct out of " + str(leftTotal + rightTotal) + ", " + str(correctPositiveDiagnosesPercentage) + "%")
print("None Diagnoses correct: " + str(noneCorrect) + " correct out of " + str(noneTotal) + ", " + str(noneCorrectPercentage) + "%")
print('\n')
print("Left Diagnoses, actual right: " + str(leftRightIncorrect) + " incorrect out of " + str(leftTotal) + ", " + str(leftrightIncorrectPercentage) + "%")
print("Right Diagnoses, actual left: " + str(rightLeftIncorrect) + " incorrect out of " + str(rightTotal) + ", " + str(rightleftIncorrectPercentage) + "%")
print('\n')
print("Left Diagnosis, actual none: " + str(leftNoneIncorrect) + " incorrect out of " + str(leftTotal) + ", " + str(leftNoneIncorrectPercentage) + "%")
print("Right Diagnosis, actual none: " + str(rightNoneIncorrect) + " incorrect out of " + str(rightTotal) + ", " + str(rightNoneIncorrectPercentage) + "%")
print('\n')
print("None Diagnosis, actual right: " + str(noneRightIncorrect) + " incorrect out of " + str(noneTotal) + ", " + str(noneRightIncorrectPercentage) + "%")
print("None Diagnosis, actual left: " + str(noneLeftIncorrect) + " incorrect out of " + str(noneTotal) + ", " + str(noneLeftIncorrectPercentage) + "%")
      