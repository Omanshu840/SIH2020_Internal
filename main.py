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

    num_cycle = 0

    date_sowing = [0]*24
    ds = -1

    date_harvest = [0]*24
    dh = -1

    for i in range(0,24):
        if(per_g[i]>5):
            num_cycle = num_cycle+1
        
            l = i - 1
            while(1):
                if(per_g[l]<1):
                    ds+=1
                    y = 2017
                    if(l>13):
                        l = l-12
                        y +=1
                    
                    l = l-1
                    s = "15 - "+str(l)+" - "+str(y)+""
                    date_sowing[ds] = s
                    break;
                l+=-1
                if(l<0):
                    break;
                    
            l = i+1
            while(1):
                if(per_g[l]<1):
                    dh+=1
                    y = 2017
                    if(l>13):
                        l = l-12
                        y +=1
                    l = l-1
                    s = "15 - "+str(l)+" - "+str(y)+""
                    date_harvest[dh] = s;
                    break;
                l+=1
                if(l>24):
                    break;


                            



    return render_template('page2.html', per_g=per_g, num_cycle=num_cycle, date_sowing=date_sowing, ds=ds, date_harvest=date_harvest, dh=dh)


@app.route("/test")
def test():

    return render_template('test..html')


if __name__=='__main__':
    app.run(debug=True)

