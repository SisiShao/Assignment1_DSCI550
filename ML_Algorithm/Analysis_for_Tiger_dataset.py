#!/usr/bin/env python
# coding: utf-8

# In[128]:


import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
import matplotlib as mpl


# In[38]:


df = pd.read_csv('tiger_final_dataset.csv')


# In[39]:


df


# In[40]:


df_train_label=df['Correction']


# In[42]:


df_train_label.fillna(0,inplace=True) 


# In[34]:


df_train_attribute=df_train[['GreenPct','NearBodyOfWater','Rank','Overall Score','Academic Reputation Score','Citations per Faculty','Faculty Student Ratio','tavg','tmin','tmax','prcp','snow','wdir','wspd','wpgt','pres','tsun']]


# In[7]:


df_train.fillna(0,inplace=True) 


# In[17]:


df_train


# In[51]:


df_train_attribute = df_train_attribute.apply(pd.to_numeric, errors='coerce').fillna(0)


# In[ ]:


#split the dataset for training and testing 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df_train_attribute, df_train_label, test_size=0.4, random_state=42)


# In[201]:


#Kmean
from sklearn.cluster import KMeans
mykmeans= KMeans(n_clusters=3, random_state=123) 
#random_state will comtrol the initialization of the cluster centers
#if we fix ramdom state then the result from K-means are always consistent
y_pred=mykmeans.fit(df_train_attribute)


# In[ ]:





# In[112]:


#KNN
#find the best option for n value
#tuned_parameters={'n_neighbors': [3, 5, 10],
                 #'metric' : ['euclidean', 'chebyshev']} #dictionary format
tuned_parameters={'n_neighbors': [19,21,23,25,27 ],
                  'metric' : ['manhattan']} #dictionary format

#括号里的为尝试的k值，metric里面的为distance的方法

from sklearn.model_selection import GridSearchCV
#GridSearchCV will carry out a procedure to select the bestparameters
#among tuned_parameters based on the machine learning CV performances
from sklearn.neighbors import KNeighborsClassifier
#cv; number pf folds, n_jobs: # of cpus
_mykNN = KNeighborsClassifier()
mykNN = GridSearchCV(_mykNN, tuned_parameters, cv=3, 
                    scoring='roc_auc',
                    verbose=10,
                    n_jobs=2)
mykNN.fit(df_train_attribute, df_train_label)


# In[113]:


mykNN.best_params_


# In[118]:


# KNN
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

#try different distance method
metrics = ["euclidean","manhattan","chebyshev","minkowski"]
#cv; number pf folds, n_jobs: # of cpus
for i in metrics:b
    mykNN = KNeighborsClassifier(n_neighbors=23, metric=i)
    mykNN.fit(X_train,  y_train)
    y_pred = mykNN.predict(X_test)
    print(accuracy_score(y_test, y_pred))


# In[194]:


mykNN = KNeighborsClassifier(n_neighbors=23, metric='manhattan')
mykNN.fit(X_train,  y_train)
y_pred = mykNN.predict(X_test)


# In[186]:


# SVM with linear
mySVM = SVC(kernel='linear', C=0.5)
mySVM.fit(X_train, y_train)
y_pred = mySVM.predict(X_test)


# In[122]:


from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)


# In[190]:


# SVM with rbf
mySVM = SVC(kernel='rbf', C=0.5, gamma=1.0)
mySVM.fit(X_train, y_train)
y_pred = mySVM.predict(X_test)
accuracy_score(y_test, y_pred)


# In[191]:


# SVM with sigmoid
mySVM = SVC(kernel='sigmoid', C=0.5, gamma=1.0, coef0=1)
mySVM.fit(X_train, y_train)
y_pred = mySVM.predict(X_test)
accuracy_score(y_test, y_pred)


# In[ ]:





# In[ ]:





# In[ ]:


#Random Forest


# In[141]:


#find the best option for n
my_n_estimators = [50, 100, 200, 300]
my_oob_scores = []
from sklearn.ensemble import RandomForestClassifier
for n_estimators in my_n_estimators:
    myRF = RandomForestClassifier(n_estimators=n_estimators, 
                                  max_features=None,  random_state=123, 
                                  oob_score=True,
                                 n_jobs=1)
    myRF.fit(X_train, y_train)
    my_oob_scores.append([n_estimators, myRF.oob_score_])


# In[142]:


# check and select  n_estimators give the best oob_score
my_oob_scores


# In[143]:


#find the best option for # of features
n_estimatores_best = 200
my_max_features = [1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14,15,16,17] #range(1, 8); 
#range(1, X_train.shape[1])
my_oob_scores = []
for max_features in my_max_features:
    myRF = RandomForestClassifier(n_estimators=n_estimatores_best,
                                  max_features=max_features,  
                                  random_state=123, oob_score=True)
    myRF.fit(X_train, y_train)
    my_oob_scores.append([max_features, myRF.oob_score_])


# In[144]:


my_oob_scores


# In[203]:


#Run Random Forest with feature of 17  and n of 200
max_features_best = 17
myRF = RandomForestClassifier(n_estimators=n_estimatores_best,
                              max_features=max_features_best,  
                              random_state=123, oob_score=True)
myRF.fit(X_train, y_train)


# In[204]:


y_pred = myRF.predict(X_test)


# In[160]:


accuracy_score(y_test, y_pred)


# In[ ]:





# In[ ]:


# Feature importance graph


# In[161]:


importances = myRF.feature_importances_


# In[162]:


importances


# In[164]:


indices = np.argsort(importances)[::-1]
indices


# In[172]:


feature_names = list(X_train)


# In[173]:


feature_names


# In[175]:


ordered_feature_names = [feature_names[i] for i in indices]
ordered_feature_names


# In[181]:


sns.set()
plt.figure(figsize=(35,10))
plt.title("Feature importances")
plt.bar(range(X_train.shape[1]), importances[indices], color="r", align="center")
plt.xticks(range(X_train.shape[1]), ordered_feature_names)
plt.xlim([-1, X_train.shape[1]])
plt.show()


# In[187]:


sns.set()
plt.figure(figsize=(15,15))
sns.heatmap(df_train_attribute.corr(), annot=True,  cmap='coolwarm')
plt.title("Feature Correlations", fontsize = 25)


# In[182]:


# for jaccard_similarity_score
import numpy as np
from sklearn.metrics import jaccard_similarity_score
jaccard_similarity_score(y_test, y_pred)


# In[185]:


jaccard_similarity_score(y_test, y_pred, normalize=False)


# In[ ]:


#result for jaccard_simmilarity_score


# In[ ]:


#jaccard_similarity_score for SVM with rbf :0.6046511627906976
#jaccard_similarity_score for KNN with manhattan and n of 23 :0.627906976744186
#jaccard_similarity_score for  Random Forest: 0.627906976744186

