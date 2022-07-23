# Import matplotlib, numpy and math
import matplotlib.pyplot as plt
import numpy as np
import math

"""x = np.linspace(-10, 10, 100)
z = 1 / (1 + np.exp(-x))


plt.plot(x, z)
plt.xlabel("x")
plt.ylabel("Sigmoid(X)")
plt.title("Sigmoid function")
plt.grid()
plt.show()"""

"""x = np.array([-10, 0, 10])
y = np.array([0, 0, 1])

plt.step(x, y, where='pre')
plt.xlabel("x")
plt.ylabel("step(X)")
plt.title("Step function")
plt.grid()
plt.show()"""

"""x = np.linspace(-10, 10, 1000)
y = np.maximum(0, x)
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("relu(X)")
plt.title("The Rectifier Function")
plt.grid()
plt.show()"""

times = np.array([0.0053,8.56,0.18,4.86, 0.069,0.075
])
AR1 = np.array([0.41,0.27,0.26,0.41,0.43,0.22
]) #pascall map
n = ["edge- en contourdetectie","Frcnn+InceptionResnet","SSD+MobileNet","MaskRcnn","eigen CNN", "eigen CNN+PreProcessing"]
markers = ["^" , "," , "o" , "v", ">", "<"]


plt.title("average Recall x gemiddelde uitvoeringstijd modellen")
plt.xlabel("AR1")
plt.ylabel("tijd [s]")
plt.xlim( [ 0, 1 ] )          # Plot from x=0 to x=80.
plt.yscale( 'log' )

for i in range(0, len(n)):
    plt.scatter(AR1[i], times[i], marker=markers[i], color='k')
    if n[i] == "eigen CNN+PreProcessing":
        plt.annotate(n[i], (AR1[i] + 0.01, times[i]+0.02))
    elif n[i] == "preprocessing model":
        plt.annotate(n[i], (AR1[i] + 0.01, times[i]+0.014))
    else: plt.annotate(n[i], (AR1[i]+0.01, times[i]))
plt.show()

"""times = np.array([0.0053,8.56,0.18,4.86, 0.069,0.075
])
AR1 = np.array([0.41,0.27,0.26,0.41,0.43,0.22
]) #pascall map
n = ["edge- en contourdetectie","Frcnn+InceptionResnet","SSD+MobileNet","MaskRcnn","eigen CNN", "eigen CNN+PreProcessing"]
markers = ["^" , "," , "o" , "v", ">", "<"]


plt.title("average Recall en gemiddelde uitvoeringstijd modellen")
plt.xlabel("AR1")
plt.ylabel("log(tijd) [s]")
plt.xlim( [ 0, 1 ] )          # Plot from x=0 to x=80.
plt.yscale( 'log' )

for i in range(0, len(n)):
    plt.scatter(AR1[i], times[i], marker=markers[i], color='k')
    if n[i] == "eigen CNN+PreProcessing":
        plt.annotate(n[i], (AR1[i] + 0.01, times[i]+0.02))
    elif n[i] == "preprocessing model":
        plt.annotate(n[i], (AR1[i] + 0.01, times[i]+0.014))
    else: plt.annotate(n[i], (AR1[i]+0.01, times[i]))


plt.show()"""

"""AP50 = np.array([0.323,0.494,0.466,0.771,0.580,0.220
])
AP75 = np.array([0.171,0.123,0.133,0.232,0.230,0.053
]) #pascall map
n = ["edge- en contourdetectie","Frcnn+InceptionResnet","SSD+MobileNet","MaskRcnn","eigen CNN", "eigen CNN+PreProcessing"]
markers = ["^" , "," , "o" , "v", ">", "<"]


plt.title("average Recall en gemiddelde uitvoeringstijd modellen")
plt.xlabel("AP50")
plt.ylabel("AP75")
plt.xlim( [ 0, 1 ] )          # Plot from x=0 to x=80.
plt.ylim( [ 0, 1 ] )

for i in range(0, len(n)):
    plt.scatter(AP50[i], AP75[i], marker=markers[i], color='k')
    if n[i] =='Frcnn+InceptionResnet':
        plt.annotate(n[i], (AP50[i]+0.01, AP75[i]-0.03))
    else:
        plt.annotate(n[i], (AP50[i]+0.01, AP75[i]))

plt.show()
AP = np.array([0.346, 0.292,0.299,0.521,0.484,0.23
])
AR1 = np.array([0.533,0.370,0.350,0.562,0.596,0.27
]) #pascall map
n = ["edge- en contourdetectie","Frcnn+InceptionResnet","SSD+MobileNet","MaskRcnn","eigen CNN", "eigen CNN+PreProcessing"]
markers = ["^" , "," , "o" , "v", ">", "<"]


plt.title("AP x AR1")
plt.ylabel("AP")
plt.xlabel("AR1")
plt.xlim( [ 0, 1 ] )          # Plot from x=0 to x=80.
plt.ylim( [ 0, 1 ] )

for i in range(0, len(n)):
    plt.scatter(AR1[i], AP[i], marker=markers[i], color='k')

    if n[i] =='Frcnn+InceptionResnet':
        plt.annotate(n[i], (AR1[i]+0.01, AP[i]-0.03))
    elif n[i] == 'SSD+MobileNet':
        plt.annotate(n[i], (AR1[i] + 0.01, AP[i] ))
    else:
        plt.annotate(n[i], (AR1[i]+0.01, AP[i]))

plt.show()
AP50 = np.array([0.489,0.710,0.640,0.910,0.923,0.3
])
AP75 = np.array([0.353,0.192,0.231,0.515,0.564,0.09
]) #pascall map
n = ["edge- en contourdetectie","Frcnn+InceptionResnet","SSD+MobileNet","MaskRcnn","eigen CNN", "eigen CNN+PreProcessing"]
markers = ["^" , "," , "o" , "v", ">", "<"]


plt.title("AP75 x AP50")
plt.xlabel("AP50")
plt.ylabel("AP75")
plt.xlim( [ 0, 1 ] )          # Plot from x=0 to x=80.
plt.ylim( [ 0, 1 ] )

for i in range(0, len(n)):
    plt.scatter(AP50[i], AP75[i], marker=markers[i], color='k')
    if n[i] =='Frcnn+InceptionResnet':
        plt.annotate(n[i], (AP50[i]+0.01, AP75[i]-0.03))
    else:
        plt.annotate(n[i], (AP50[i]+0.01, AP75[i]))

plt.show()"""