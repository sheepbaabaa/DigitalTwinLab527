import logging
from camNativeLib.camNativeSDK import *


sdk=HKSdkApi()
sdk.add_dll()
sdk.NET_DVR_Init()
sdk.NET_DVR_Login_V40()
# sdk.NET_DVR_Login_V30()
sdk.getStream()
# sdk.getPTZ()
# sdk.control(TILT_DOWN,PTZ_CONTROL_START,7)
# sdk.control(TILT_DOWN,PTZ_CONTROL_STOP,7)
sdk.NET_DVR_Logout()
