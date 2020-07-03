{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "####                        (**** GPA Calculation of Four Subjects ****)\n",
    "\n",
    "Name_of_Subjects = []\n",
    "Credit_hours = []\n",
    "Marks_Obtained = []\n",
    "\n",
    "# First loop to take all the inputs from the user\n",
    "for i in range(4):\n",
    "    Name_of_Subject = input(\"Enter Subject Name: \")\n",
    "    Name_of_Subjects.append(Name_of_Subject)\n",
    "    \n",
    "    Credit_hours_of_subject = float(input(\"Enter Subject Credit Hours: \"))\n",
    "    Credit_hours.append(Credit_hours_of_subject)\n",
    "    \n",
    "    Marks_obtained_in_each_subject = int(input(\"Enter Obtained Marks: \"))\n",
    "    Marks_Obtained.append(Marks_obtained_in_each_subject)\n",
    "\n",
    "GPA = [] \n",
    "# Second Loop to calculate the gpa of each subject \n",
    "for i in Marks_Obtained:\n",
    "    marks = (i / 100) * 100\n",
    "    \n",
    "    if marks >= 90:\n",
    "        GPA.append(4.0)\n",
    "        print(marks, \".You got A grade\")\n",
    "    elif marks >= 85 and marks <= 89:\n",
    "        GPA.append(3.7)\n",
    "        print(marks, \".You got A- grade\")\n",
    "    elif marks >= 80 and marks <= 84:\n",
    "        GPA.append(3.3)\n",
    "        print(marks, \".You got B+ grade\")\n",
    "    elif marks >= 75 and marks <= 79:\n",
    "        GPA.append(3.0)\n",
    "        print(marks, \".You got B grade\")\n",
    "    elif marks >= 70 and marks <= 74:\n",
    "        GPA.append(2.7)\n",
    "        print(marks, \".You got B- grade\")\n",
    "    elif marks >= 65 and marks <= 69:\n",
    "        GPA.append(2.3)\n",
    "        print(marks, \".You got C+ grade\")\n",
    "    elif marks >= 60 and marks <= 64:\n",
    "        GPA.append(2.0)\n",
    "        print(marks, \".You got C- grade\")\n",
    "    else:\n",
    "        GPA.append(0)\n",
    "        print(marks, \".You got F grade\")\n",
    "        \n",
    "print(\"GPA_of_all_subjects: \" + str(GPA))\n",
    "\n",
    "\n",
    "Subject_Grade_Points = []\n",
    "# Third Loop to find the Subject Grade Points\n",
    "for credit,gpa in zip(Credit_hours, GPA):\n",
    "    grade_point = round((credit * gpa),2)\n",
    "    Subject_Grade_Points.append(grade_point)\n",
    "\n",
    "print(\"Subject_Grade_Points: \", Subject_Grade_Points)\n",
    "\n",
    "# take sum \n",
    "Grade_point_of_all_Subjects = sum (Subject_Grade_Points)\n",
    "Total_Credit_Hours = sum (Credit_hours)\n",
    "\n",
    "# Semester GPA Calculation\n",
    "# round command will round off the semester gpa upto 2 decimal points\n",
    "Semester_GPA = Grade_point_of_all_Subjects / Total_Credit_Hours\n",
    "Semester_GPA = round(Semester_GPA, 2)\n",
    "print(\"Semester_GPA: \" + str(Semester_GPA))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}