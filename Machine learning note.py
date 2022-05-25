#!/usr/bin/env python
# coding: utf-8

# # <h1 style="front-size:10rem;color:orange;"> Machine Learning note (Andrew Ng)

# # What is Machine Learning?

# ## Two defination 

# * **Arthur Samuel (older, informal version):**\
# "the field of study that gives computers the ability to learn without being explicitly programmed."

# * **Tom mitchell (more modern version):**\
# "A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E."    
# 
# Example:`playing checkers`
# 
# **E** = the experience of playing many games of checkers
# 
# **T** = the task of playing checkers.
# 
# **P** = the probability that the program will win the next game.
# 
# 
# 

# ## Two broad classifications

# * **Supervised learning**
# * `given a data set( training set) and already know what our correct output should look like`
#  * _Regression Problems_ : map input variables to some continuous function
#         eg: Given a picture of a person, predict their age on the basis of the given picture
#  * _Classification Problems_ : map input variables into discrete categories
#         eg: Given a patient with a tumor, predict whether the tumor is malignant or benign.
# 
#   
# * **Unsupervised learning**
# * `approach problems with little or no idea what our results should look like`
# * `derive data's structure by clustering the data based on relationships among the variables in the data`
#  * _Clustering_ :
#         eg: Take a collection of 1,000,000 different genes, and find a way to automatically group these genes into groups that are somehow similar or related by different variables, such as lifespan, location, roles, and so on.
#  * _Non-Clustering_ :
#         eg: The "Cocktail Party Algorithm", allows you to find structure in a chaotic environment. (i.e. identifying individual voices and music from a mesh of sounds at a cocktail party).

# ## Model Representation 

# ### Notation:
# m = Number of training examples(crossponse "input" and "output" variable)\
# x's = "input" variable/features\
# y's = "output" variable/"target" variable\
# (x,y) = one training example\
# ($x^{i}$, $y^{i}$) = ith training example

# Data set= a list of m training examples ($x^{i}$, $y^{i}$), i = 1, 2, ....m

# ### supervised learning problem (more formal)
# * given a training set, learn a function (hypothesis),
#   so that h(x) is a "good" predictot for the corressponding value of y
# 
#   $h_{\theta}$ : $X_{\theta}$ -> $Y_{\theta}$ 
#   
#   
# * if the target variable y is continuous-> `refression problem
# * if y can take on only a small number of discrete values -> `classification problem

# $x^{2}$     $x_{2}$

# ## Cost Function
# measure the accuracy of hypothesis function \
# $$J(\theta_{0},\theta_{1})=\frac{1}{2m}\sum_{i=1}^m(\hat{y}_{i}-y_{i})^2 = \frac{1}{2m}\sum_{i=1}^m(h_{\theta}(x_{i})-y_{i})^2$$

# $\hat{x}$, $\tilde{x}$, $\vec{x}$

# In[ ]:




