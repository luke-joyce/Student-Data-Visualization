import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import sys

def GPAhist(filepath):
	student_data = pd.read_json(filepath, orient='split')
	student_data.rename(columns={0 : 'Name', 1 : 'GPA'}, inplace=True)
	student_data.head()
	student_data.sort_values(by=['Name'])


	fig, ax = plt.subplots(1,1,figsize=(20,10))
	plt.hist(student_data['GPA'], label=['GPA'], rwidth = 0.9, bins = None, density = True)

	ax.set_title("Student Grade Point Averages")
	ax.set_xlabel('GPA')
	ax.set_ylabel('Density')
	plt.legend()

	plt.savefig('GPA_histo.png')
	print('exiting program')


def Scoreshist(filepath):

	student_data = pd.read_json(filepath, orient='split')
	student_data.rename(columns={0 : 'Name', 1 : 'Score'}, inplace=True)
	student_data.head()
	student_data.sort_values(by=['Name'])


	fig, ax = plt.subplots(1,1,figsize=(20,10))
	plt.hist(student_data['Score'], label=['Score'], bins = None, density = True)
	
	title = "Student Scores for " + filepath
	ax.set_title(title)
	ax.set_xlabel('Score')
	ax.set_ylabel('Density')
	plt.legend()

	plt.savefig('Scores_histo.png')
	print('exiting program')




theinput = input("Student Data or Classes? ('1' for Student Data or '2' for Classes): ")

text = int(theinput)

while(text != 0):
	if(text==1):
		choice = input("Generate Data for GPA or Age? ('1' for GPA and '2' for Age): ")
		if(choice == 1):
			GPAhist('student_data.csv')
			exit()
		else:
			exit()
			
		
	elif(text==2):
		testNum = input("Which Test?")
		if(testNum == 1):
			Scoreshist('Test1.json')
		elif(testNum==2):
			Scoreshist('Test2.json')
		elif(testNum==3):
			Scoreshist('Test3.json')
		else:
			exit()
	else:
		print('Enter a valid option: ')
	
