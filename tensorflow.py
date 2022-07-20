#IMPORTING MODULES
import matplotlib.pyplot as plt
from prettytable import PrettyTable






#TAKING INITIAL INPUTS FROM TEACHER
subjects = input("Enter the name of the subjects in order of the file separated by a space ").split()
max_marks = int(input('Please enter the maximum marks of each subject(out of which marks were given):'))
no_of_subjects = len(subjects)

with open("student marks.txt","r",encoding = "ascii") as file:
    lines = file.readlines()
    firstline = lines[0]
    firstline = firstline.split(" ")
    firstline[-1] = firstline[-1].strip()
    n = len(firstline) - 1

        
if no_of_subjects != n :
    raise Exception("The number of subjects you mentioned does not match the number of subjects in 'student marks.txt' file")




#MAKING 'MYDICTIONARY' =>  NAME : MARKS
mydictionary = {}
student_marks = open("student marks.txt","r",encoding = "ascii")
for i in student_marks :
    templist = i.split(" ")
    tempname = templist[0]
    tempmarks = templist[1:no_of_subjects+1]
    mydictionary[tempname] = tempmarks
    templist = []
    tempmarks = []

student_marks.close()







#MAKING A NESTED DICTIONARY => SUBJECTS:{NAME:SUBJECT_MARKS} 
onedictionary = {}
big = {}
for j in range(no_of_subjects) :
    student_marks = open("student marks.txt","r",encoding = "ascii")
    for i in student_marks :
        templist = i.split(" ")
        templist[-1] = templist[-1].strip()   #remove '\n'
        onedictionary[templist[0]] = templist[j+1]
    big[subjects[j]] = onedictionary
    onedictionary = {}
    
student_marks.close()





#PROGRAMM STARTS AND STUDENT ENTERS HIS/HER NAME
name = input('enter the name of the student ')



#DEFINING LIST OF MARKS(STRING) OF STUDENT
marks = mydictionary[name]    



#PRINT STUDENT'S NAME 
print("###################################################################################################")
print("###################################################################################################")
print("###############################  REPORT CARD  #####################################################")
print("###################################################################################################")
print("###################################################################################################")
print("\n\nSTUDENT'S NAME ==>  ",name,"\n\n")







#DEFINING TOTAL MARKS(INTEGERS)
for i in range(no_of_subjects):
    marks[i] = int(marks[i])
totalmarks = sum(marks)


#DEFINING DICTIONARY TOTALMARKSDICT => NAME:TOTAL MARKS 
totalmarksdict = {}

a = mydictionary.keys()
b = list(a)
for j in range(len(mydictionary)):
    tempmarks = mydictionary[b[j]]
    for i in range(no_of_subjects):
        tempmarks[i] = int(tempmarks[i])
    temptotalmarks = sum(tempmarks)
    totalmarksdict[b[j]] = temptotalmarks




#DEFINING PERCENTAGE(STRINGS) 
percentage = 100*(totalmarks)/(no_of_subjects * max_marks)
percentage = round(percentage,2)
percentage = str(percentage)+" %"                         







#DEFINING FUNCTIONS GIVING GRADE AS OUTPUT 
def grade(a):
    if 100>=a>=90 :
        grade = 'A+'
    elif 90>a>=80 :
        grade = 'A'
    elif 80>a>=70 :
        grade = 'B+'
    elif 70>a>=60 :
        grade = 'B'
    elif 60>a>=50 :
        grade = 'C+' 
    elif 50>a>=40 :
        grade = 'C' 
    else :
        grade = 'failed'                        
    return grade


#DEFINING FUNCTIONS GIVING GP AS OUTPUT 
def GP(a):
    if 100>=a>=90 :
        GP = 10
    elif 90>a>=80 :
        GP = 9
    elif 80>a>=70 :
        GP = 8
    elif 70>a>=60 :
        GP = 7
    elif 60>a>=50 :
        GP = 6
    elif 50>a>=40 :
        GP = 5
    elif 40>a>=30 :
        GP = 4     
    elif 30>a>=20 :
        GP = 3
    elif 20>a>=10 :
        GP = 2
    else :
        GP = 1

    return GP




#DEFINING FUNCTIONS GIVING OVERALL CGPA AS OUTPUT
def ovr_cgpa():
      sum = 0
      for j in range(no_of_subjects):
           
           sum = sum + GP(int(marks[j]))
      CGPA = sum/no_of_subjects
      return CGPA






#PRINT TABLE CONTAINING MARKS, GRADE AND RANK OF EACH SUBJECT

r = 1

rank_table = PrettyTable(["        subject        ","        marks        ","        grade        ","        rank        "])

for i in range(no_of_subjects) :  
    studentmarks = big[subjects[i]].values()
    studentmarkslist = list(studentmarks)
    for j in range(len(studentmarkslist)):
        if int(studentmarkslist[j]) > int(big[subjects[i]][name]):
            r = r + 1
        else :
            pass
    rank_table.add_row([subjects[i], marks[i],grade(int(marks[i])),r])
    r = 1
    
print(rank_table)





#FINDING TOTAL RANK
r = 1
m = totalmarksdict.values()
n = list(m)
for i in range(len(n)):
    if n[i] > totalmarks:
        r = r+1






#PRINT TABLE CONTAINING TOTAL MARKS AND PERCENTAGE     
print("\n\n")
lasttable = PrettyTable(["     total marks       ","       total percentage     ","     total rank      ","      CGPA      "])
lasttable.add_row([totalmarks,percentage,r,round(ovr_cgpa(),2)])
print(lasttable)






#PRINT TABLE CONTAINING AVERAGE AND HIGHEST MARKS OF CLASS IN EACH SUBJECT
print("\n\n\nCOMPARISON WITH CLASS")
average = {}
highest_marks = {}

for i in range(no_of_subjects):
    l = big[subjects[i]].values()
    m = list(l)
    for j in range(len(m)):
        m[j]=int(m[j])
    average[subjects[i]] = round((sum(m)/len(m)),2)
    m.sort(reverse = True)
    highest_marks[subjects[i]] = m[0]
    
comparison_table = PrettyTable(["          subjects          ","           average of class           ","highest marks in class"])

for i in range(no_of_subjects):
    comparison_table.add_row([subjects[i],average[subjects[i]],highest_marks[subjects[i]]])

print(comparison_table)


    

#SHOWS BAR CHART CONTAINING MARKS OF EACH SUBJECT
xaxis = subjects
yaxis = marks
plt.bar(xaxis,yaxis)
plt.xlabel("subjects")
plt.ylabel("marks")
plt.title("marks in each subject")
plt.show()


#SHOWS PIE CHART CONTAINING MARKS OF EACH SUBJECT
plt.pie(marks, labels = subjects)
plt.title("relative comparison of marks ")
plt.show()




