%matplotlib inline
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display
from PIL import Image



tdata = pd.read_csv('appendix.csv')

tdata.head()
tdata_drop = tdata.copy()
tdata_drop.drop('Course Number', axis=1, inplace=True)
tdata_drop.drop('Instructors', axis=1, inplace=True)
tdata_drop.drop('Honor Code Certificates', axis=1, inplace=True)
tdata_drop.drop('Participants (Course Content Accessed)', axis=1, inplace=True)
tdata_drop.drop('Audited (> 50% Course Content Accessed)', axis=1, inplace=True)
tdata_drop.drop('% Certified of > 50% Course Content Accessed', axis=1, inplace=True)
tdata_drop.drop('% Played Video', axis=1, inplace=True)
tdata_drop.drop('% Posted in Forum', axis=1, inplace=True)
tdata_drop.drop('% Grade Higher Than Zero', axis=1, inplace=True)
tdata_drop.drop('Median Age', axis=1, inplace=True)
tdata_drop.drop('% Male', axis=1, inplace=True)
tdata_drop.drop('% Female', axis=1, inplace=True)
tdata_drop.drop("% Bachelor's Degree or Higher", axis=1, inplace=True)
tdata_drop.drop('% Audited', axis=1, inplace=True)
tdata_drop.drop('Certified', axis=1, inplace=True)
tdata_drop.drop('% Certified', axis=1, inplace=True)


tdata2 = tdata_drop.copy()

labels = tdata2['Median Hours for Certification']

tdata3.drop('Median Hours for Certification', axis=1, inplace=True)
tdata3.drop('Total Course Hours (Thousands)', axis=1, inplace=True)

tdata4.head()
tdata5 = tdata4.copy()
y = tdata4['Median Hours for Certification']

tdata5.head()
tdata5.drop('Median Hours for Certification', axis=1, inplace=True)

from sklearn.model_selection import train_test_split
X = tdata5
ctitles = X['Course Title']
csubject = X['Course Subject']
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit(ctitles)
ctitles2 = le.fit_transform(ctitles)
le.fit(csubject)
csubject2 = le.fit_transform(csubject)
Xtry = X.copy()

Xtry['Course Title'] = ctitles2

Xtry['Course Subject'] = csubject2
le.fit(Xtry['Course Number'])
cnumber2= le.fit_transform(Xtry['Course Number'])
Xtry['Course Number'] = cnumber2

from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.preprocessing import StandardScaler
from sql_query import data1
ss = StandardScaler()
ss.fit(X_train2)

X_final = ss.fit_transform(X_train2)

import tensorflow as tf


m, n = X_final.shape

X = tf.placeholder(tf.float32, shape=(None, n), name="X")
y = tf.placeholder(tf.float32, shape=(None, 1), name="y")

w = tf.Variable(tf.random_uniform([n, 1], -1.0, 1.0), name="theta")
b = tf.Variable(tf.random_uniform([1,n] , -1.0 , 1.0), name="b")

y_ = (tf.matmul(X, w) + b)

error = (y_ - y)

mse = tf.reduce_mean(tf.square(error), name="mse")



optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
training_op = optimizer.minimize(mse)

def fetch_batch(epoch, batch_index, batch_size):
    for i in range(len(X_final)):
        i = int(i*100)
        X_batch = X_final[i: i +100]
        y_batch = y_train2[i: i + 100]
    return X_batch, y_batch


batch_size = 100
n_batches = int(np.ceil(m/batch_size))
n_batches
y_train2 = y_train2.reshape(-1,1)

n_epochs = 1000
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for epoch in range(n_epochs):
        for batch_index in range(n_batches):
            X_batch, y_batch = fetch_batch(epoch, batch_index, batch_size)
           ## if batch_index % 9 == 0:
             ##   summary_str = mse_summary.eval(feed_dict={X:X_batch, y:y_batch})
               ## step = epoch * n_batches + batch_index
               ## file_writer.add_summary(summary_str, step)
               ## sess.run(training_op, feed_dict={X: X_batch, y: y_batch})
            best_theta = w.eval()
            best_mse = mse.eval(feed_dict={X:X_batch, y:y_batch})
print(best_theta)
y_train2.shape
