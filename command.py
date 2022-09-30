
from time import sleep
from win32 import win32api

# lparam define
# https://docs.microsoft.com/zh-cn/windows/win32/inputdev/wm-syskeydown
# scan code
# https://www.win.tue.nl/~aeb/linux/kbd/scancodes-1.html

def sendAltedKey(hwmd, keyCode, scanCode, extendKeyFlag = 0):
  win32api.PostMessage(hwmd, 0x0104, 0x12, 0x00380001)
  win32api.PostMessage(hwmd, 0x0104, keyCode, 0x20000001 + (scanCode<<16) + (extendKeyFlag<<24)) # 29
  sleep(0.1)
  win32api.PostMessage(hwmd, 0x0105, keyCode, 0xe0000001 + (scanCode<<16) + (extendKeyFlag<<24)) # 31 30 29
  win32api.PostMessage(hwmd, 0x0105, 0x12, 0xc0380001) # 31 30

def sendShiftAltedKey(hwmd, keyCode, scanCode, extendKeyFlag = 0):
  win32api.PostMessage(hwmd, 0x0104, 0x12, 0x00380001)
  win32api.PostMessage(hwmd, 0x0104, 0xA0, 0x202a0001) # 29
  win32api.PostMessage(hwmd, 0x0104, keyCode, 0x20000001 + (scanCode<<16) + (extendKeyFlag<<24)) # 29
  sleep(0.1)
  win32api.PostMessage(hwmd, 0x0105, keyCode, 0xe0000001 + (scanCode<<16) + (extendKeyFlag<<24)) # 31 30 29
  win32api.PostMessage(hwmd, 0x0105, 0xA0, 0xe02a0001) # 31 30 29
  win32api.PostMessage(hwmd, 0x0105, 0x12, 0xc0380001) # 31 30

def sendAltF(hwmd):
  keyCode = 0x46
  scanCode = 0x21
  sendAltedKey(hwmd, keyCode, scanCode)

def sendAltLeft(hwmd):
  keyCode = 0x25
  scanCode = 0x4b
  sendAltedKey(hwmd, keyCode, scanCode, 1)


def sendAltRight(hwmd):
  keyCode = 0x27
  scanCode = 0x4d
  sendAltedKey(hwmd, keyCode, scanCode, 1)

def sendAltUp(hwmd):
  keyCode = 0x26
  scanCode = 0x48
  sendAltedKey(hwmd, keyCode, scanCode, 1)

def sendAltDown(hwmd):
  keyCode = 0x28
  scanCode = 0x50 
  sendAltedKey(hwmd, keyCode, scanCode, 1)  

def sendAltG(hwmd):
  keyCode = 0x47
  scanCode = 0x22 
  sendAltedKey(hwmd, keyCode, scanCode) 

def sendAltW(hwmd):
  keyCode = 0x58
  scanCode = 0x11 
  sendAltedKey(hwmd, keyCode, scanCode) 

def sendAltB(hwmd):
  keyCode = 0x42
  scanCode = 0x30 
  sendAltedKey(hwmd, keyCode, scanCode) 

def sendAltS(hwmd):
  keyCode = 0x53
  scanCode = 0x1f 
  sendAltedKey(hwmd, keyCode, scanCode) 

def sendAltM(hwmd):
  keyCode = 0x4D
  scanCode = 0x32 
  sendAltedKey(hwmd, keyCode, scanCode) 

def sendAltP(hwmd):
  keyCode = 0x50
  scanCode = 0x19
  sendAltedKey(hwmd, keyCode, scanCode) 

def sendAltO(hwmd):
  keyCode = 0x4F
  scanCode = 0x18
  sendAltedKey(hwmd, keyCode, scanCode) 

def sendShiftAltO(hwmd):
  keyCode = 0x4F
  scanCode = 0x18
  sendShiftAltedKey(hwmd, keyCode, scanCode)

def sendAltR(hwmd):
  keyCode = 0x52
  scanCode = 0x13
  sendAltedKey(hwmd, keyCode, scanCode) 

def sendAltN(hwmd):
  keyCode = 0x4E
  scanCode = 0x31
  sendAltedKey(hwmd, keyCode, scanCode) 

def sendShiftAltN(hwmd):
  keyCode = 0x4E
  scanCode = 0x31
  sendShiftAltedKey(hwmd, keyCode, scanCode) 

def sendAltH(hwmd):
  keyCode = 0x48
  scanCode = 0x23
  sendAltedKey(hwmd, keyCode, scanCode) 

commandDict = {
  'toggle_fullscreen': sendAltF,
  'rotate_left': sendAltLeft,
  'rotate_right': sendAltRight,
  'volume_up': sendAltUp,
  'volume_down': sendAltDown,
  'resize_to_1': sendAltG,
  'resize_to_fit': sendAltW,
  'back': sendAltB,
  'app_switch': sendAltS,
  'menu': sendAltM,
  'turn_off_screen': sendAltO,
  'turn_on_screen': sendShiftAltO,
  'rotate_device_screen': sendAltR,
  'expand_notification': sendAltN,
  'collapse_notification': sendShiftAltN,
  'power': sendAltP,
  'home': sendAltH,
}

def getCommandFunction(commandId):
  return commandDict.get(commandId)

def getCommandIdList():
  return [ commandId for commandId in commandDict.keys()]


# # Expand settings panel	MOD+n+n | Double-5th-click³

# sendShiftAltN(0x04D08F4)

