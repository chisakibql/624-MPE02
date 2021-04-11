import cv2
import matplotlib.pyplot as plt
import numpy as np

path = ""
pref = "SemImage20210401"
post = ".png"
name = ["051","053","055","058","061","063","066","068","070"]

ci = [400,450,500,550,600,650,700,750,800]
center = [274,230,250,241,234,187,226,185,183]
jumps = [[383,642],
[385,641],
[399,661],
[401,652],
[398,665],
[398,650],
[397,652],
[411,660],
[403,655]]

img = cv2.imread(path+pref+name[0]+post)
gl0 = [float(img[0,i,0])/255.0 for i in range(1024)]
xl0 = [j for j in range(1024)]
for i in range(9):
    img = cv2.imread(path+pref+name[i]+post)
    gl = [float(img[0,i,0])/255.0 for i in range(1024)]
    xl = [j-center[i]+center[0] for j in range(1024)]
    plt.plot(xl,gl,label="%d"%ci[i])
    plt.legend()
    plt.xlabel("pixel")
    plt.ylabel("grey level")
    plt.savefig("img%d.png"%(ci[i]))
    plt.clf()
for i in range(9):
    img = cv2.imread(path+pref+name[i]+post)
    gl = [float(img[0,i,0])/255.0 for i in range(1024)]
    plt.plot(xl0,gl,label="%d"%ci[i])
    plt.plot([center[i] for j in range(100)],[j*0.01 for j in range(100)],color="red",linestyle="--")
    plt.legend()
    plt.xlabel("pixel")
    plt.ylabel("grey level")
    plt.savefig("imgcentered%d.png"%(ci[i]))
    plt.clf()
for i in range(9):
    img = cv2.imread(path+pref+name[i]+post)
    gl = [float(img[0,i,0])/255.0 for i in range(1024)]
    xl = [j-center[i]+center[0] for j in range(1024)]
    plt.plot(xl,gl,label="%d"%ci[i])
    plt.plot(xl0,gl0,label="%d"%ci[0])
    plt.legend()
    plt.xlabel("pixel")
    plt.ylabel("grey level")
    plt.savefig("imgdx%d.png"%(ci[i]))
    plt.clf()
for i in range(9):
    img = cv2.imread(path+pref+name[i]+post)
    gl = [float(img[0,i,0])/255.0 for i in range(1024)]
    xl = [j-center[i]+center[0] for j in range(1024)]
    plt.plot(xl,gl,label="%d"%ci[i])
    plt.plot(xl0,gl0,label="%d"%ci[0])
    plt.plot([center[0] for j in range(100)],[j*0.01 for j in range(100)],color="red",linestyle="--")
    plt.legend()
    plt.xlabel("pixel")
    plt.ylabel("grey level")
    plt.savefig("imgcentereddx%d.png"%(ci[i]))
    plt.clf()

vrl = []
nvrl = []
for i in range(9):
    img = cv2.imread(path+pref+name[i]+post)
    gl = [float(img[0,j,0])/255.0 for j in range(1024)]
    xl = [j-center[i]+center[0] for j in range(1024)]
    y1 = gl[jumps[i][0]]
    y2 = gl[jumps[i][1]]
    dy = y1 - y2
    vr = np.var(gl[800:850])
    vrl.append(vr)
    nvrl.append(vr/dy/dy)
print(vrl)
print(nvrl)