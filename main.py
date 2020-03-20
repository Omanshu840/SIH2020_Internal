from flask import Flask, render_template, request, redirect
import cv2
import NDVI_Calculation
import matplotlib.pyplot as plt
size = 2118*2135

app = Flask(__name__)



@app.route("/")
def home():
    return render_template('index.html')


@app.route("/page2")
def page2():

    per_g = NDVI_Calculation.Calulate()
    
    kt = -1
    k = [0]*24

    for i in range (1,25):
        kt = kt+1
        k[kt] = kt
    plt.plot(k, per_g)
    plt.xlabel('No of Months')
    plt.ylabel('Percentage area')

    plt.title('Green Area Graph') 
    plt.savefig('static/img/green.jpg')

    return render_template('page2.html', per_g=per_g)


@app.route("/test")
def test():

    return render_template('test..html')


if __name__=='__main__':
    app.run(debug=True)

