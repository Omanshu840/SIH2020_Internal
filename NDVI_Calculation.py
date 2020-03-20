import cv2
import matplotlib.pyplot as plt

x = -1.9
x1 = -1.9
x2 = -1.9


per_y = [0] * 24
per_g = [0] * 24



size = 2118*2135



# def Calulate():

#     k = 0

#     for i in range(2017, 2019):
#         for j in range(1,13):
#                 if(j <= 9):
#                     x = str('Dataset/awifs_ndvi_'+ str(i) +'0'+ str(j) +'_15_'+ str(1) +'_clipped.tif')
#                     y = str('Dataset/awifs_ndvi_'+ str(i) +'0'+ str(j) +'_15_'+ str(2) +'_clipped.tif')
#                 else:
#                     x = str('Dataset/awifs_ndvi_'+ str(i) +''+ str(j) +'_15_'+ str(1) +'_clipped.tif')
#                     y = str('Dataset/awifs_ndvi_'+ str(i) +''+ str(j) +'_15_'+ str(2) +'_clipped.tif')

#                 img1 = cv2.imread(x, 0)
#                 img2 = cv2.imread(y, 0)

#                 img_h1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2RGB)

#                 for l in range(0,2135):
#                     for m in range(0,2118):
#                         # NDVI = (NRI - RED)/(NRI + RED)
#                         x1 = int(img1[l][m]) - int(img2[l][m])
#                         x2 = int(img1[l][m]) + int(img2[l][m])

#                         if x2==0:
#                             z = 0
#                         else:
#                             z = x1/x2

#                         if(z < -0.2 and z >= -1.0):
#                             img_h1[l][m] = (0,0,0)
#                         elif(z < -0.1 and z >= -0.2):
#                             img_h1[l][m] = (255,0,0)
#                         elif(z < 0 and z >= 0.1):
#                             img_h1[l][m] = (191,0,0)
#                         elif(z < 0.1 and z >= 0):
#                             img_h1[l][m] = (127,0,0)
#                         elif(z < 0.2 and z >= 0.1):
#                             img_h1[l][m] = (255,255,0)
#                         elif(z < 0.3 and z >= 0.2):
#                             img_h1[l][m] = (191,191,0)
#                         elif(z < 0.4 and z >= 0.3):
#                             img_h1[l][m] = (127,127,0)
#                         elif(z < 0.5 and z >= 0.4):
#                             img_h1[l][m] = (0,255,255)
#                         elif(z < 0.6 and z >= 0.5):
#                             img_h1[l][m] = (0,191,191)
#                         elif(z < 0.7 and z >= 0.6):
#                             img_h1[l][m] = (0,127,127)
#                         elif(z < 0.8 and z >= 0.7):
#                             img_h1[l][m] = (0,255,0)
#                         elif(z < 0.9 and z >= 0.8):
#                             img_h1[l][m] = (0,191,0)
#                         elif(z < 1.0 and z >= 0.9):
#                             img_h1[l][m] = (0,127,0)

#                         if(img_h1[l][m][2] == 0):
#                             if(img_h1[l][m][0] != 0 and img_h1[l][m][1] != 0):
#                                 per_y[k] = per_y[k] + 1
#                         if(img_h1[l][m][0] == 0 and img_h1[l][m][2] == 0):
#                             if(img_h1[l][m][1] != 0):
#                                 per_g[k] = per_g[k] + 1
                        
                
#                 per_y[k] = (per_y[k] / size) * 100
#                 per_g[k] = (per_g[k] / size) * 100
#                 print('Percentage of Yellow @' + str(j) +'-'+ str(i) + ' : '+ str(per_y[k]))
#                 print('Percentage of Green  @' + str(j) +'-'+ str(i) + ' : '+ str(per_g[k]))
#                 k = k + 1

#                 n = str('ProcessedImages/'+str(i)+'-'+str(j)+'-'+str(0)+'15.tif')
#                 cv2.imwrite(n, img_h1)

#     per_total = per_y + per_g
#     print('Percentage of Total:')
#     print(per_total)

#     return per_g



def Calulate():
    
    k = 0

    for i in range(2017, 2018):
        for j in range(6,8):
                if(j <= 9):
                    x = str('Dataset/awifs_ndvi_'+ str(i) +'0'+ str(j) +'_15_'+ str(1) +'_clipped.tif')
                    y = str('Dataset/awifs_ndvi_'+ str(i) +'0'+ str(j) +'_15_'+ str(2) +'_clipped.tif')
                else:
                    x = str('Dataset/awifs_ndvi_'+ str(i) +''+ str(j) +'_15_'+ str(1) +'_clipped.tif')
                    y = str('Dataset/awifs_ndvi_'+ str(i) +''+ str(j) +'_15_'+ str(2) +'_clipped.tif')

                img1 = cv2.imread(x, 0)
                img2 = cv2.imread(y, 0)

                img_h1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2RGB)

                for l in range(0,2135):
                    for m in range(0,2118):
                        # NDVI = (NRI - RED)/(NRI + RED)
                        x1 = int(img1[l][m]) - int(img2[l][m])
                        x2 = int(img1[l][m]) + int(img2[l][m])

                        if x2==0:
                            z = 0
                        else:
                            z = x1/x2

                        if(z < -0.2 and z >= -1.0):
                            img_h1[l][m] = (0,0,0)
                        elif(z < -0.1 and z >= -0.2):
                            img_h1[l][m] = (255,0,0)
                        elif(z < 0 and z >= 0.1):
                            img_h1[l][m] = (191,0,0)
                        elif(z < 0.1 and z >= 0):
                            img_h1[l][m] = (127,0,0)
                        elif(z < 0.2 and z >= 0.1):
                            img_h1[l][m] = (255,255,0)
                        elif(z < 0.3 and z >= 0.2):
                            img_h1[l][m] = (191,191,0)
                        elif(z < 0.4 and z >= 0.3):
                            img_h1[l][m] = (127,127,0)
                        elif(z < 0.5 and z >= 0.4):
                            img_h1[l][m] = (0,255,255)
                        elif(z < 0.6 and z >= 0.5):
                            img_h1[l][m] = (0,191,191)
                        elif(z < 0.7 and z >= 0.6):
                            img_h1[l][m] = (0,127,127)
                        elif(z < 0.8 and z >= 0.7):
                            img_h1[l][m] = (0,255,0)
                        elif(z < 0.9 and z >= 0.8):
                            img_h1[l][m] = (0,191,0)
                        elif(z < 1.0 and z >= 0.9):
                            img_h1[l][m] = (0,127,0)

                        if(img_h1[l][m][2] == 0):
                            if(img_h1[l][m][0] != 0 and img_h1[l][m][1] != 0):
                                per_y[k] = per_y[k] + 1
                        if(img_h1[l][m][0] == 0 and img_h1[l][m][2] == 0):
                            if(img_h1[l][m][1] != 0):
                                per_g[k] = per_g[k] + 1
                        
                
                per_y[k] = (per_y[k] / size) * 100
                per_g[k] = (per_g[k] / size) * 100
                print('Percentage of Yellow @' + str(j) +'-'+ str(i) + ' : '+ str(per_y[k]))
                print('Percentage of Green  @' + str(j) +'-'+ str(i) + ' : '+ str(per_g[k]))
                k = k + 1

                n = str('ProcessedImages/'+str(i)+'-'+str(j)+'-'+str(0)+'15.tif')
                cv2.imwrite(n, img_h1)

    per_total = per_y + per_g
    print('Percentage of Total:')
    print(per_total)
    
    return per_g




def GenerateGraph():
    kt = -1
    k = [0]*24

    for i in range (1,25):
        kt = kt+1
        k[kt] = kt
    plt.plot(k, per_g)
    plt.xlabel('No of Months')
    plt.ylabel('Percentage area')

    plt.title('Green Area Graph') 
    plt.savefig('/static/img/green.jpg')
    


