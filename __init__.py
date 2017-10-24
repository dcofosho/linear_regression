from flask import Flask, render_template, request, redirect, jsonify, url_for, flash, send_file
import httplib2
import json
import random
from flask import make_response
import requests
import string
import StringIO
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import json
from sklearn.model_selection import ShuffleSplit
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import make_scorer
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
import matplotlib
matplotlib.use("Agg")
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from sklearn import linear_model
import matplotlib.pyplot as plt
app = Flask(__name__)

@app.route('/linreg', methods=['GET','POST'])
def linreg():
        if request.method=='POST':
                try:
                        if request.form['x_vals']:
                                x_vals=request.form['x_vals'].split(',')
                        if request.form['y_vals']:
                                y_vals = request.form['y_vals'].split(',')
                        #convert array vals to int and remove u character
                        for i in range(0, len(x_vals)):
                                x_vals[i] = [int(x_vals[i].replace('u',''))]
                        for i in range(0, len(y_vals)):
                                y_vals[i] = [int(y_vals[i].replace('u',''))]
                        print(str(x_vals)+str(y_vals))
                        fig = plt.figure()
                        fig.suptitle('test title', fontsize=20)
                        plt.scatter(x_vals, y_vals)
                        reg = linear_model.LinearRegression()
                        reg.fit(x_vals, y_vals)
                        plt.plot(x_vals, reg.predict(x_vals), color='blue', linewidth=3)
                        slope = str(reg.coef_).replace('[','').replace(']', '')
                        intercept = str(reg.intercept_).replace('[','').replace(']', '')
                        r_squared = str(reg.score(x_vals, y_vals))
                        fig.suptitle('y='+slope+'x'+'+'+intercept+"          "+'r-squared='+r_squared, fontsize=20)
                        plt.xlabel="X axis"
                        plt.ylabel="Y axis"
                        out_png = '/var/www/html/spamfilter/spamfilter/out_file.png'
                        plt.savefig(out_png, dpi=150)
                        return send_file(out_png, mimetype='image/png')
                except:
                        return "X and Y need to be same length!"+"<br>"+"length of x_vals: "+str(len(x_vals))+"<br>"+"<br>"+"length of y_vals: "+str(len(y_vals))+"<br>"+"<button onclick='history.back()'>Go back</button>"
        else:
                return render_template("linreg.html")



if __name__ == '__main__':
        app.secret_key='totally_secure_key'
        #app.debug = True
        app.run()