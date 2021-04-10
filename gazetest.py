import socket
import xml.etree.ElementTree as ET
import pygetwindow as pgw
import keyboard
#Run this file after running the gazepointer application
alt_pressed = False
w_pressed = False
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",43333)) #connect to the socket

s.send("xml\n".encode("utf-8"))#Send data format
print(s.send('AppKeyDemo\n'.encode("utf-8"))) #Send AppKey
#s.settimeout(1.0)


def onaltpres(key):
    global alt_pressed
    alt_pressed = True

def onwpres(key):
    global w_pressed
    w_pressed = True

def onaltrel(key):
    global alt_pressed
    alt_pressed = False

def onwrel(key):
    global w_pressed
    w_pressed = False

keyboard.on_press_key('alt',onaltpres)
keyboard.on_press_key('w',onwpres)
keyboard.on_release_key('alt',onaltrel)
keyboard.on_release_key('w',onwrel)


while True:
    data = s.recv(4096)
    try:
        data = data.decode("utf-8")
    except:
        # print(repr(data))
        #print("-------------------------------------------------------------------------------")
        continue
    
    try:
    	root=ET.fromstring(data[1:])
    except:
    	continue
    print(root)	
    X = float(root[0].text)
    Y = float(root[1].text)
    active_window = pgw.getActiveWindow()
    if alt_pressed and w_pressed:
        try:
            print(active_window.title)
            active_window.moveTo(int(X),int(Y))
        except Exception as e:
            print(e)
            print("oopss")
            continue
        #active window follow the coordinate of gaze
    print("{}: {}".format(root[0].tag, root[0].text))
    print("{}: {}".format(root[1].tag, root[1].text))
    print("heymama-------------------------------------------------------------------------------")
