from __future__ import print_function
from multiprocessing.spawn import import_main_path
import roslibpy
from time import sleep
from bhaptics import haptic_player
import matplotlib.pyplot as plt

def vest():
    player = haptic_player.HapticPlayer()
    sleep(0.4)
    return player

#The host address needs to be replaced with the name or IP address of the ROS bridge host
client = roslibpy.Ros(host='10.204.94.55', port=9090)
client.run()

listener = roslibpy.Topic(client, '/chatter', 'std_msgs/Float64MultiArray')

NEW_DICT = {'message_var': None}

player=vest()
y_region0_distance = []
y_region0_intensity = []

def callback(message):
    NEW_DICT['message_var'] = message['data']
    print(NEW_DICT['message_var'])
    y_region0_distance.append(NEW_DICT['message_var'][0])
    
    for i in range(0,8):    
        durationMillis = 1
        d = NEW_DICT['message_var'][i]
        

        if(d>0):
            intensity = int(10/d)
            if(d<0.1):
                d = 0.1
            if i==0:
                print(0)
                y_region0_intensity.append(intensity)
                player.submit_dot("frontFrame", "VestFront", [{"index": 5, "intensity": intensity}], durationMillis)
                player.submit_dot("frontFrame", "VestFront", [{"index": 6, "intensity": intensity}], durationMillis)
            if i==1:
                print(1)
                player.submit_dot("frontFrame", "VestFront", [{"index": 1, "intensity": intensity}], durationMillis)
                player.submit_dot("frontFrame", "VestFront", [{"index": 4, "intensity": intensity}], durationMillis)
            if i==2:
                print(2)
                player.submit_dot("frontFrame", "VestFront", [{"index": 8, "intensity": intensity}], durationMillis)
                player.submit_dot("backFrame", "VestBack", [{"index": 8, "intensity": intensity}], durationMillis)
            if i==3:
                print(3)
                player.submit_dot("backFrame", "VestBack", [{"index": 1, "intensity": intensity}], durationMillis)
                player.submit_dot("backFrame", "VestBack", [{"index": 4, "intensity": intensity}], durationMillis)
            if i==4:
                print(4)
                player.submit_dot("backFrame", "VestBack", [{"index": 5, "intensity": intensity}], durationMillis)
                player.submit_dot("backFrame", "VestBack", [{"index": 6, "intensity": intensity}], durationMillis)
            if i==5:
                print(5)
                player.submit_dot("backFrame", "VestBack", [{"index": 3, "intensity": intensity}], durationMillis)
                player.submit_dot("backFrame", "VestBack", [{"index": 7, "intensity": intensity}], durationMillis)
            if i==6:
                print(6)
                player.submit_dot("frontFrame", "VestFront", [{"index": 11, "intensity": intensity}], durationMillis)
                player.submit_dot("backFrame", "VestBack", [{"index": 11, "intensity": intensity}], durationMillis)
            if i==7:
                print(7)
                player.submit_dot("frontFrame", "VestFront", [{"index": 3, "intensity": intensity}], durationMillis)
                player.submit_dot("frontFrame", "VestFront", [{"index": 7, "intensity": intensity}], durationMillis)
        else:
            if(i==0):
                y_region0_intensity.append(0)

listener.subscribe(callback)

try:
    while True:
        pass

except KeyboardInterrupt:

'''
    Show the function graph of time/distance, time/intensity and distance/intensity
    ax1=plt.subplot(3,1,1)

    x = []
    y_distance = y_region0_distance

    y_intensity = y_region0_intensity

    for i in range(len(y_distance)):
        x.append(i)

    plt.plot(x,y_distance)
    ax2=plt.subplot(3,1,2)
    plt.plot(x,y_intensity)
    ax3=plt.subplot(3,1,3)
    plt.plot(y_distance,y_intensity)
    plt.show()
'''
    client.terminate()
