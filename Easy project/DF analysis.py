#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib as mt
import numpy as np


# In[3]:


df = pd.read_csv('D:\student_exam_data.csv')


# In[6]:


df.head(8)


# In[29]:


#Calculating how many hours on ave, min & max two groups of students studied
study_hours = df.groupby('Pass/Fail', as_index=False)    .agg({'Study Hours': ['mean', 'min', 'max']}).round(0)

study_hours.columns = ['Pass/Fail', 'mean_study_hours', 'min_study_hours', 'max_study_hours']


# In[30]:


study_hours


# In[32]:


#Calculating what ave, min & max scores on previous exams did students receive
previous_exam_score = df.groupby('Pass/Fail', as_index = False)    .agg({'Previous Exam Score' : ['mean', 'min', 'max']}).round(0)

previous_exam_score.columns = ['Pass/Fail', 'mean_previous_exam_score', 'min_previous_exam_score', 'max_previous_exam_score']


# In[33]:


previous_exam_score


# In[43]:


#merging results of two dataframes to have an overview
merged_data = study_hours     .merge(previous_exam_score, on = 'Pass/Fail')


# In[44]:


merged_data


# In[45]:


#reversing columns & rows for better visibility
merged_data.transpose()


# In[47]:


#Assessing how much students of each type (1 = passed exam, 0 = failed exam) are in the dataframe
students = df["Pass/Fail"].value_counts()

print('# of students who passed: ', students[1])
print('# of students who failed: ', students[0])


# In[48]:


#Showing what percentage of students who failed the exam spent more than average time to study

average_study_hours = df['Study Hours'].mean()

# Filtering the DataFrame for students who failed the exam
failed_students = df[df['Pass/Fail'] == 0]

# Checking the number of failed students who spent more than the average time studying
failed_students_above_average = failed_students[failed_students['Study Hours'] > average_study_hours]
num_failed_above_average = len(failed_students_above_average)

percentage_failed_above_average = (num_failed_above_average / len(failed_students)) * 100

# Displpaying results
print(f"Percentage of students who failed and spent more than average time studying: {percentage_failed_above_average:.2f}%")


# In[49]:


#Showing what percentage of students who passed the exam spent more than average time to study

average_study_hours = df['Study Hours'].mean()

# Filtering the DataFrame for students who passed the exam
passed_students = df[df['Pass/Fail'] == 1]

# Checking the number of students who passed test and spent more than the average time studying
passed_students_above_average = passed_students[passed_students['Study Hours'] > average_study_hours]
num_passed_above_average = len(passed_students_above_average)

percentage_passed_above_average = (num_passed_above_average / len(passed_students)) * 100

# Showing results
print(f"Percentage of students who passed and spent more than average time studying: {percentage_passed_above_average:.2f}%")

