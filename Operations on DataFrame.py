#!/usr/bin/env python
# coding: utf-8

# # Accessing Columns Of DataFrame

# In[123]:


import pandas as pd

d = {'Name':['Sachin','Dhoni','Virat','Rohit','Shikhar','Sachin'],
     'Age':[26,25,25,24,31,33],
     'Score':[87,67,89,55,47,90]}

df = pd.DataFrame(d,index = ['A','B','C','D','E','F'])

df


# # Accessing the Columns
# 
# 
# ## 1. DataFrame_Object [ Column_name ] 
# ## 2. DataFrame_Object.Column_name
# 
# ### Note : - In the dot notation make sure do not put any quotatino marks around column name.
# 

# ## 1. DataFrame_Object [ Column_name ]

# In[47]:


# Single Column
#returning single column in the type of Series
# df['Name']
# type(df['Name'])
#returning single column in the type of DataFrame
# df[['Name']]
# type(df[['Name']])
#accessing individual Value
#df['Name']['C']

# Accessing Multiple Columns
df[['Age','Name']]


# ## 2. DataFrame_Object.Column_name

# In[52]:


#singe Column using dot Operator in the form of Series
df.Age

#accessing individual value
#df.Name['A']


# # Accessing Slices of DataFrame
# 1. <font size=5>loc [start_row : End_row , start_col : End_col]</font>
# 
# 2. <font size=5>iloc [start_row_Pos : End_row_Pos , start_col_Pos : End_col_Pos]</font>

# In[59]:


#using loc
df.loc['B':,:'Age']
df.iloc[1:,:2]

#accessing perticular rows
df.loc[['C','E']]
df.loc[['C','E'],:]
df.iloc[[2,4]]
df.iloc[[2,4],:]


#accessing perticular rows and columns
df.loc[['C','E'],['Age']]
df.iloc[[2,4],[1]]


# # Adding a Column / Modifying Values of Existing Column

# In[107]:


# same vale in all columns
df['Strike_rate'] = 100
print(df)


# In[112]:


# different values in all columns 
df['Strike_rate'] = [100,90,86,74,75,90]
print(df)


# # Deleting Columns 

# In[109]:


del df['Strike_rate']
print(df)


# In[111]:


df.pop('Strike_rate')
print(df)


# In[113]:


# Only print the outpu on screen, to change we have to assign it to the same variable
df = df.drop('Strike_rate',axis = 1)
# df = df.drop('Strike_rate',axis = 'columns')

print(df)


# # Adding rows / Modifying value of existing rows

# In[114]:


# adding Values
df.loc['G'] = ['Rahul',35,98]
print(df)


# In[124]:


# changing Values
df.iloc[5] = ['Gambhir',32,82]
# df.loc['F'] = ['Gambhir',32,82]
df.iloc[[0,1,2]] = ['Tanmay',29,88]
print(df)


# # Deleting Rows

# In[121]:


# Only print the outpu on screen, to change we have to assign it to the same variable
df = df.drop('Age', axis= 0)
# df = df.drop('Age', axis='rows')
print(df)

