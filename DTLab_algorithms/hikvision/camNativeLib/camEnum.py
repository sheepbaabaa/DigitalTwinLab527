# **宏定义***/
# 常量
MAX_NAMELEN = 16  # DVR本地登陆名
MAX_RIGHT = 32  # 设备支持的权限（1-12表示本地权限，13-32表示远程权限）
NAME_LEN = 32  # 用户名长度
PASSWD_LEN = 16  # 密码长度
SERIALNO_LEN = 48  # 序列号长度
MACADDR_LEN = 6  # mac地址长度
MAX_ETHERNET = 2  # 设备可配以太网络
PATHNAME_LEN = 128  # 路径长度
MAX_TIMESEGMENT_V30 = 8  # 9000设备最大时间段数
MAX_TIMESEGMENT = 4  # 8000设备最大时间段数
MAX_SHELTERNUM = 4  # 8000设备最大遮挡区域数
MAX_DAYS = 7  # 每周天数
PHONENUMBER_LEN = 32  # pppoe拨号号码最大长度
MAX_DISKNUM_V30 = 33  # 9000设备最大硬盘数# 最多33个硬盘(包括16个内置SATA硬盘、1个eSATA硬盘和16个NFS盘) */
MAX_DISKNUM = 16  # 8000设备最大硬盘数
MAX_DISKNUM_V10 = 8  # 1.2版本之前版本
MAX_WINDOW_V30 = 32  # 9000设备本地显示最大播放窗口数
MAX_WINDOW = 16  # 8000设备最大硬盘数
MAX_VGA_V30 = 4  # 9000设备最大可接VGA数
MAX_VGA = 1  # 8000设备最大可接VGA数
MAX_USERNUM_V30 = 32  # 9000设备最大用户数
MAX_USERNUM = 16  # 8000设备最大用户数
MAX_EXCEPTIONNUM_V30 = 32  # 9000设备最大异常处理数
MAX_EXCEPTIONNUM = 16  # 8000设备最大异常处理数
MAX_LINK = 6  # 8000设备单通道最大视频流连接数
MAX_DECPOOLNUM = 4  # 单路解码器每个解码通道最大可循环解码数
MAX_DECNUM = 4  # 单路解码器的最大解码通道数（实际只有一个，其他三个保留）
MAX_TRANSPARENTNUM = 2  # 单路解码器可配置最大透明通道数
MAX_CYCLE_CHAN = 16  # 单路解码器最大轮循通道数
MAX_DIRNAME_LENGTH = 80  # 最大目录长度
MAX_STRINGNUM_V30 = 8  # 9000设备最大OSD字符行数数
MAX_STRINGNUM = 4  # 8000设备最大OSD字符行数数
MAX_STRINGNUM_EX = 8  # 8000定制扩展
MAX_AUXOUT_V30 = 16  # 9000设备最大辅助输出数
MAX_AUXOUT = 4  # 8000设备最大辅助输出数
MAX_HD_GROUP = 16  # 9000设备最大硬盘组数
MAX_NFS_DISK = 8  # 8000设备最大NFS硬盘数
IW_ESSID_MAX_SIZE = 32  # WIFI的SSID号长度
IW_ENCODING_TOKEN_MAX = 32  # WIFI密锁最大字节数
MAX_SERIAL_NUM = 64  # 最多支持的透明通道路数
MAX_DDNS_NUMS = 10  # 9000设备最大可配ddns数
MAX_DOMAIN_NAME = 64  # 最大域名长度 */

MAX_EMAIL_ADDR_LEN = 48  # 最大email地址长度
MAX_EMAIL_PWD_LEN = 32  # 最大email密码长度
MAXPROGRESS = 100  # 回放时的最大百分率
MAX_SERIALNUM = 2  # 8000设备支持的串口数 1-232， 2-485
CARDNUM_LEN = 20  # 卡号长度
MAX_VIDEOOUT_V30 = 4  # 9000设备的视频输出数
MAX_VIDEOOUT = 2  # 8000设备的视频输出数
MAX_PRESET_V30 = 256  # 9000设备支持的云台预置点数 */
MAX_TRACK_V30 = 256  # 9000设备支持的云台轨迹数 */
MAX_CRUISE_V30 = 256  # 9000设备支持的云台巡航数 */
MAX_PRESET = 128  # 8000设备支持的云台预置点数 */
MAX_TRACK = 128  # 8000设备支持的云台轨迹数 */
MAX_CRUISE = 128  # 8000设备支持的云台巡航数 */
CRUISE_MAX_PRESET_NUMS = 32  # 一条巡航最多的巡航点 */
MAX_SERIAL_PORT = 8  # 9000设备支持232串口数
MAX_PREVIEW_MODE = 8  # 设备支持最大预览模式数目 1画面,4画面,9画面,16画面.... */
MAX_MATRIXOUT = 16  # 最大模拟矩阵输出个数 */
LOG_INFO_LEN = 11840  # 日志附加信息 */
DESC_LEN = 16  # 云台描述字符串长度 */
PTZ_PROTOCOL_NUM = 200  # 9000最大支持的云台协议数 */
MAX_AUDIO = 1  # 8000语音对讲通道数
MAX_AUDIO_V30 = 2  # 9000语音对讲通道数
MAX_CHANNUM = 16  # 8000设备最大通道数
MAX_ALARMIN = 16  # 8000设备最大报警输入数
MAX_ALARMOUT = 4  # 8000设备最大报警输出数
# 9000 IPC接入
MAX_ANALOG_CHANNUM = 32  # 最大32个模拟通道
MAX_ANALOG_ALARMOUT = 32  # 最大32路模拟报警输出
MAX_ANALOG_ALARMIN = 32  # 最大32路模拟报警输入
MAX_IP_DEVICE = 32  # 允许接入的最大IP设备数
MAX_IP_CHANNEL = 32  # 允许加入的最多IP通道数
MAX_IP_ALARMIN = 128  # 允许加入的最多报警输入数
MAX_IP_ALARMOUT = 64  # 允许加入的最多报警输出数

# 最大支持的通道数 最大模拟加上最大IP支持 */
MAX_CHANNUM_V30 = (MAX_ANALOG_CHANNUM + MAX_IP_CHANNEL)  # 64
MAX_ALARMOUT_V30 = (MAX_ANALOG_ALARMOUT + MAX_IP_ALARMOUT)  # 96
MAX_ALARMIN_V30 = (MAX_ANALOG_ALARMIN + MAX_IP_ALARMIN)  # 160

# ******************全局错误码 begin**********************/
NET_DVR_NOERROR = 0  # 没有错误
NET_DVR_PASSWORD_ERROR = 1  # 用户名密码错误
NET_DVR_NOENOUGHPRI = 2  # 权限不足
NET_DVR_NOINIT = 3  # 没有初始化
NET_DVR_CHANNEL_ERROR = 4  # 通道号错误
NET_DVR_OVER_MAXLINK = 5  # 连接到DVR的客户端个数超过最大
NET_DVR_VERSIONNOMATCH = 6  # 版本不匹配
NET_DVR_NETWORK_FAIL_CONNECT = 7  # 连接服务器失败
NET_DVR_NETWORK_SEND_ERROR = 8  # 向服务器发送失败
NET_DVR_NETWORK_RECV_ERROR = 9  # 从服务器接收数据失败
NET_DVR_NETWORK_RECV_TIMEOUT = 10  # 从服务器接收数据超时
NET_DVR_NETWORK_ERRORDATA = 11  # 传送的数据有误
NET_DVR_ORDER_ERROR = 12  # 调用次序错误
NET_DVR_OPERNOPERMIT = 13  # 无此权限
NET_DVR_COMMANDTIMEOUT = 14  # DVR命令执行超时
NET_DVR_ERRORSERIALPORT = 15  # 串口号错误
NET_DVR_ERRORALARMPORT = 16  # 报警端口错误
NET_DVR_PARAMETER_ERROR = 17  # 参数错误
NET_DVR_CHAN_EXCEPTION = 18  # 服务器通道处于错误状态
NET_DVR_NODISK = 19  # 没有硬盘
NET_DVR_ERRORDISKNUM = 20  # 硬盘号错误
NET_DVR_DISK_FULL = 21  # 服务器硬盘满
NET_DVR_DISK_ERROR = 22  # 服务器硬盘出错
NET_DVR_NOSUPPORT = 23  # 服务器不支持
NET_DVR_BUSY = 24  # 服务器忙
NET_DVR_MODIFY_FAIL = 25  # 服务器修改不成功
NET_DVR_PASSWORD_FORMAT_ERROR = 26  # 密码输入格式不正确
NET_DVR_DISK_FORMATING = 27  # 硬盘正在格式化，不能启动操作
NET_DVR_DVRNORESOURCE = 28  # DVR资源不足
NET_DVR_DVROPRATEFAILED = 29  # DVR操作失败
NET_DVR_OPENHOSTSOUND_FAIL = 30  # 打开PC声音失败
NET_DVR_DVRVOICEOPENED = 31  # 服务器语音对讲被占用
NET_DVR_TIMEINPUTERROR = 32  # 时间输入不正确
NET_DVR_NOSPECFILE = 33  # 回放时服务器没有指定的文件
NET_DVR_CREATEFILE_ERROR = 34  # 创建文件出错
NET_DVR_FILEOPENFAIL = 35  # 打开文件出错
NET_DVR_OPERNOTFINISH = 36  # 上次的操作还没有完成
NET_DVR_GETPLAYTIMEFAIL = 37  # 获取当前播放的时间出错
NET_DVR_PLAYFAIL = 38  # 播放出错
NET_DVR_FILEFORMAT_ERROR = 39  # 文件格式不正确
NET_DVR_DIR_ERROR = 40  # 路径错误
NET_DVR_ALLOC_RESOURCE_ERROR = 41  # 资源分配错误
NET_DVR_AUDIO_MODE_ERROR = 42  # 声卡模式错误
NET_DVR_NOENOUGH_BUF = 43  # 缓冲区太小
NET_DVR_CREATESOCKET_ERROR = 44  # 创建SOCKET出错
NET_DVR_SETSOCKET_ERROR = 45  # 设置SOCKET出错
NET_DVR_MAX_NUM = 46  # 个数达到最大
NET_DVR_USERNOTEXIST = 47  # 用户不存在
NET_DVR_WRITEFLASHERROR = 48  # 写FLASH出错
NET_DVR_UPGRADEFAIL = 49  # DVR升级失败
NET_DVR_CARDHAVEINIT = 50  # 解码卡已经初始化过
NET_DVR_PLAYERFAILED = 51  # 调用播放库中某个函数失败
NET_DVR_MAX_USERNUM = 52  # 设备端用户数达到最大
NET_DVR_GETLOCALIPANDMACFAIL = 53  # 获得客户端的IP地址或物理地址失败
NET_DVR_NOENCODEING = 54  # 该通道没有编码
NET_DVR_IPMISMATCH = 55  # IP地址不匹配
NET_DVR_MACMISMATCH = 56  # MAC地址不匹配
NET_DVR_UPGRADELANGMISMATCH = 57  # 升级文件语言不匹配
NET_DVR_MAX_PLAYERPORT = 58  # 播放器路数达到最大
NET_DVR_NOSPACEBACKUP = 59  # 备份设备中没有足够空间进行备份
NET_DVR_NODEVICEBACKUP = 60  # 没有找到指定的备份设备
NET_DVR_PICTURE_BITS_ERROR = 61  # 图像素位数不符，限24色
NET_DVR_PICTURE_DIMENSION_ERROR = 62  # 图片高*宽超限， 限128*256
NET_DVR_PICTURE_SIZ_ERROR = 63  # 图片大小超限，限100K
NET_DVR_LOADPLAYERSDKFAILED = 64  # 载入当前目录下Player Sdk出错
NET_DVR_LOADPLAYERSDKPROC_ERROR = 65  # 找不到Player Sdk中某个函数入口
NET_DVR_LOADDSSDKFAILED = 66  # 载入当前目录下DSsdk出错
NET_DVR_LOADDSSDKPROC_ERROR = 67  # 找不到DsSdk中某个函数入口
NET_DVR_DSSDK_ERROR = 68  # 调用硬解码库DsSdk中某个函数失败
NET_DVR_VOICEMONOPOLIZE = 69  # 声卡被独占
NET_DVR_JOINMULTICASTFAILED = 70  # 加入多播组失败
NET_DVR_CREATEDIR_ERROR = 71  # 建立日志文件目录失败
NET_DVR_BINDSOCKET_ERROR = 72  # 绑定套接字失败
NET_DVR_SOCKETCLOSE_ERROR = 73  # socket连接中断，此错误通常是由于连接中断或目的地不可达
NET_DVR_USERID_ISUSING = 74  # 注销时用户ID正在进行某操作
NET_DVR_SOCKETLISTEN_ERROR = 75  # 监听失败
NET_DVR_PROGRAM_EXCEPTION = 76  # 程序异常
NET_DVR_WRITEFILE_FAILED = 77  # 写文件失败
NET_DVR_FORMAT_READONLY = 78  # 禁止格式化只读硬盘
NET_DVR_WITHSAMEUSERNAME = 79  # 用户配置结构中存在相同的用户名
NET_DVR_DEVICETYPE_ERROR = 80  # 导入参数时设备型号不匹配*/
NET_DVR_LANGUAGE_ERROR = 81  # 导入参数时语言不匹配*/
NET_DVR_PARAVERSION_ERROR = 82  # 导入参数时软件版本不匹配*/
NET_DVR_IPCHAN_NOTALIVE = 83  # 预览时外接IP通道不在线*/
NET_DVR_RTSP_SDK_ERROR = 84  # 加载高清IPC通讯库StreamTransClient.dll失败*/
NET_DVR_CONVERT_SDK_ERROR = 85  # 加载转码库失败*/
NET_DVR_IPC_COUNT_OVERFLOW = 86  # 超出最大的ip接入通道数*/
NET_PLAYM4_NOERROR = 500  # no error
NET_PLAYM4_PARA_OVER = 501  # input parameter is invalid
NET_PLAYM4_ORDER_ERROR = 502  # The order of the function to be called is error.
NET_PLAYM4_TIMER_ERROR = 503  # Create multimedia clock failed
NET_PLAYM4_DEC_VIDEO_ERROR = 504  # Decode video data failed.
NET_PLAYM4_DEC_AUDIO_ERROR = 505  # Decode audio data failed.
NET_PLAYM4_ALLOC_MEMORY_ERROR = 506  # Allocate memory failed.
NET_PLAYM4_OPEN_FILE_ERROR = 507  # Open the file failed.
NET_PLAYM4_CREATE_OBJ_ERROR = 508  # Create thread or event failed
NET_PLAYM4_CREATE_DDRAW_ERROR = 509  # Create DirectDraw object failed.
NET_PLAYM4_CREATE_OFFSCREEN_ERROR = 510  # failed when creating off-screen surface.
NET_PLAYM4_BUF_OVER = 511  # buffer is overflow
NET_PLAYM4_CREATE_SOUND_ERROR = 512  # failed when creating audio device.
NET_PLAYM4_SET_VOLUME_ERROR = 513  # Set volume failed
NET_PLAYM4_SUPPORT_FILE_ONLY = 514  # The function only support play file.
NET_PLAYM4_SUPPORT_STREAM_ONLY = 515  # The function only support play stream.
NET_PLAYM4_SYS_NOT_SUPPORT = 516  # System not support.
NET_PLAYM4_FILEHEADER_UNKNOWN = 517  # No file header.
NET_PLAYM4_VERSION_INCORRECT = 518  # The version of decoder and encoder is not adapted.
NET_PALYM4_INIT_DECODER_ERROR = 519  # Initialize decoder failed.
NET_PLAYM4_CHECK_FILE_ERROR = 520  # The file data is unknown.
NET_PLAYM4_INIT_TIMER_ERROR = 521  # Initialize multimedia clock failed.
NET_PLAYM4_BLT_ERROR = 522  # Blt failed.
NET_PLAYM4_UPDATE_ERROR = 523  # Update failed.
NET_PLAYM4_OPEN_FILE_ERROR_MULTI = 524  # openfile error, streamtype is multi
NET_PLAYM4_OPEN_FILE_ERROR_VIDEO = 525  # openfile error, streamtype is video
NET_PLAYM4_JPEG_COMPRESS_ERROR = 526  # JPEG compress error
NET_PLAYM4_EXTRACT_NOT_SUPPORT = 527  # Don't support the version of this file.
NET_PLAYM4_EXTRACT_DATA_ERROR = 528  # extract video data failed.
# ******************全局错误码 end**********************/
# ************************************************
#  NET_DVR_IsSupport()返回值
#  1－9位分别表示以下信息（位与是TRUE)表示支持；
# **************************************************/
NET_DVR_SUPPORT_DDRAW = 0x01  # 支持DIRECTDRAW，如果不支持，则播放器不能工作；
NET_DVR_SUPPORT_BLT = 0x02  # 显卡支持BLT操作，如果不支持，则播放器不能工作；
NET_DVR_SUPPORT_BLTFOURCC = 0x04  # 显卡BLT支持颜色转换，如果不支持，播放器会用软件方法作RGB转换；
NET_DVR_SUPPORT_BLTSHRINKX = 0x08  # 显卡BLT支持X轴缩小；如果不支持，系统会用软件方法转换；
NET_DVR_SUPPORT_BLTSHRINKY = 0x10  # 显卡BLT支持Y轴缩小；如果不支持，系统会用软件方法转换；
NET_DVR_SUPPORT_BLTSTRETCHX = 0x20  # 显卡BLT支持X轴放大；如果不支持，系统会用软件方法转换；
NET_DVR_SUPPORT_BLTSTRETCHY = 0x40  # 显卡BLT支持Y轴放大；如果不支持，系统会用软件方法转换；
NET_DVR_SUPPORT_SSE = 0x80  # CPU支持SSE指令，Intel Pentium3以上支持SSE指令；
NET_DVR_SUPPORT_MMX = 0x100  # CPU支持MMX指令集，Intel Pentium3以上支持SSE指令；
# *********************云台控制命令 begin*************************/
PTZ_CONTROL_START = 0
PTZ_CONTROL_STOP = 1
LIGHT_PWRON = 2  # 接通灯光电源 */
WIPER_PWRON = 3  # 接通雨刷开关 */
FAN_PWRON = 4  # 接通风扇开关 */
HEATER_PWRON = 5  # 接通加热器开关 */
AUX_PWRON1 = 6  # 接通辅助设备开关 */
AUX_PWRON2 = 7  # 接通辅助设备开关 */
SET_PRESET = 8  # 设置预置点 */
CLE_PRESET = 9  # 清除预置点 */
ZOOM_IN = 11  # 焦距以速度SS变大(倍率变大) */
ZOOM_OUT = 12  # 焦距以速度SS变小(倍率变小) */
FOCUS_NEAR = 13  # 焦点以速度SS前调 */
FOCUS_FAR = 14  # 焦点以速度SS后调 */
IRIS_OPEN = 15  # 光圈以速度SS扩大 */
IRIS_CLOSE = 16  # 光圈以速度SS缩小 */
TILT_UP = 21  # 云台以SS的速度上仰 */
TILT_DOWN = 22  # 云台以SS的速度下俯 */
PAN_LEFT = 23  # 云台以SS的速度左转 */
PAN_RIGHT = 24  # 云台以SS的速度右转 */
UP_LEFT = 25  # 云台以SS的速度上仰和左转 */
UP_RIGHT = 26  # 云台以SS的速度上仰和右转 */
DOWN_LEFT = 27  # 云台以SS的速度下俯和左转 */
DOWN_RIGHT = 28  # 云台以SS的速度下俯和右转 */
PAN_AUTO = 29  # 云台以SS的速度左右自动扫描 */
FILL_PRE_SEQ = 30  # 将预置点加入巡航序列 */
SET_SEQ_DWELL = 31  # 设置巡航点停顿时间 */
SET_SEQ_SPEED = 32  # 设置巡航速度 */
CLE_PRE_SEQ = 33  # 将预置点从巡航序列中删除 */
STA_MEM_CRUISE = 34  # 开始记录轨迹 */
STO_MEM_CRUISE = 35  # 停止记录轨迹 */
RUN_CRUISE = 36  # 开始轨迹 */
RUN_SEQ = 37  # 开始巡航 */
STOP_SEQ = 38  # 停止巡航 */
GOTO_PRESET = 39  # 快球转到预置点 */
DEL_SEQ = 43  # 删除巡航路径
STOP_CRUISE = 44  # 停止运行轨迹*/
DELETE_CRUISE = 45  # 删除单条轨迹 */
DELETE_ALL_CRUISE = 46  # 删除所有轨迹*/
NET_DVR_CONTROL_PTZ_PATTERN = 3313  # 快球云台花样扫描*/

# *********************云台控制命令 end*************************/
# ************************************************
#  回放时播放控制命令宏定义
#  NET_DVR_PlayBackControl
#  NET_DVR_PlayControlLocDisplay
#  NET_DVR_DecPlayBackCtrl的宏定义
#  具体支持查看函数说明和代码
#  **************************************************/
NET_DVR_PLAYSTART = 1  # 开始播放
NET_DVR_PLAYSTOP = 2  # 停止播放
NET_DVR_PLAYPAUSE = 3  # 暂停播放
NET_DVR_PLAYRESTART = 4  # 恢复播放
NET_DVR_PLAYFAST = 5  # 快放
NET_DVR_PLAYSLOW = 6  # 慢放
NET_DVR_PLAYNORMAL = 7  # 正常速度
NET_DVR_PLAYFRAME = 8  # 单帧放
NET_DVR_PLAYSTARTAUDIO = 9  # 打开声音
NET_DVR_PLAYSTOPAUDIO = 10  # 关闭声音
NET_DVR_PLAYAUDIOVOLUME = 11  # 调节音量
NET_DVR_PLAYSETPOS = 12  # 改变文件回放的进度
NET_DVR_PLAYGETPOS = 13  # 获取文件回放的进度
NET_DVR_PLAYGETTIME = 14  # 获取当前已经播放的时间(按文件回放的时候有效)
NET_DVR_PLAYGETFRAME = 15  # 获取当前已经播放的帧数(按文件回放的时候有效)
NET_DVR_GETTOTALFRAMES = 16  # 获取当前播放文件总的帧数(按文件回放的时候有效)
NET_DVR_GETTOTALTIME = 17  # 获取当前播放文件总的时间(按文件回放的时候有效)
NET_DVR_THROWBFRAME = 20  # 丢B帧
NET_DVR_SETSPEED = 24  # 设置码流速度
NET_DVR_KEEPALIVE = 25  # 保持与设备的心跳(如果回调阻塞，建议2秒发送一次)
# 远程按键定义如下：
# key value send to CONFIG program */
KEY_CODE_1 = 1
KEY_CODE_2 = 2
KEY_CODE_3 = 3
KEY_CODE_4 = 4
KEY_CODE_5 = 5
KEY_CODE_6 = 6
KEY_CODE_7 = 7
KEY_CODE_8 = 8
KEY_CODE_9 = 9
KEY_CODE_0 = 10
KEY_CODE_POWER = 11
KEY_CODE_MENU = 12
KEY_CODE_ENTER = 13
KEY_CODE_CANCEL = 14
KEY_CODE_UP = 15
KEY_CODE_DOWN = 16
KEY_CODE_LEFT = 17
KEY_CODE_RIGHT = 18
KEY_CODE_EDIT = 19
KEY_CODE_ADD = 20
KEY_CODE_MINUS = 21
KEY_CODE_PLAY = 22
KEY_CODE_REC = 23
KEY_CODE_PAN = 24
KEY_CODE_M = 25
KEY_CODE_A = 26
KEY_CODE_F1 = 27
KEY_CODE_F2 = 28

# for PTZ control */
KEY_PTZ_UP_START = KEY_CODE_UP
KEY_PTZ_UP_STO = 32
KEY_PTZ_DOWN_START = KEY_CODE_DOWN
KEY_PTZ_DOWN_STOP = 33
KEY_PTZ_LEFT_START = KEY_CODE_LEFT
KEY_PTZ_LEFT_STOP = 34
KEY_PTZ_RIGHT_START = KEY_CODE_RIGHT
KEY_PTZ_RIGHT_STOP = 35
KEY_PTZ_AP1_START = KEY_CODE_EDIT  # 光圈+ */
KEY_PTZ_AP1_STOP = 36
KEY_PTZ_AP2_START = KEY_CODE_PAN  # 光圈- */
KEY_PTZ_AP2_STOP = 37
KEY_PTZ_FOCUS1_START = KEY_CODE_A  # 聚焦+ */
KEY_PTZ_FOCUS1_STOP = 38
KEY_PTZ_FOCUS2_START = KEY_CODE_M  # 聚焦- */
KEY_PTZ_FOCUS2_STOP = 39
KEY_PTZ_B1_START = 40  # 变倍+ */
KEY_PTZ_B1_STOP = 41
KEY_PTZ_B2_START = 42  # 变倍- */
KEY_PTZ_B2_STOP = 43
# 9000新增
KEY_CODE_11 = 44
KEY_CODE_12 = 45
KEY_CODE_13 = 46
KEY_CODE_14 = 47
KEY_CODE_15 = 48
KEY_CODE_16 = 49
# ************************参数配置命令 begin*******************************/
# 用于NET_DVR_SetDVRConfig和NET_DVR_GetDVRConfig,注意其对应的配置结构
NET_DVR_GET_DEVICECFG = 100  # 获取设备参数
NET_DVR_SET_DEVICECFG = 101  # 设置设备参数
NET_DVR_GET_NETCFG = 102  # 获取网络参数
NET_DVR_SET_NETCFG = 103  # 设置网络参数
NET_DVR_GET_PICCFG = 104  # 获取图象参数
NET_DVR_SET_PICCFG = 105  # 设置图象参数
NET_DVR_GET_COMPRESSCFG = 106  # 获取压缩参数
NET_DVR_SET_COMPRESSCFG = 107  # 设置压缩参数
NET_DVR_GET_RECORDCFG = 108  # 获取录像时间参数
NET_DVR_SET_RECORDCFG = 109  # 设置录像时间参数
NET_DVR_GET_DECODERCFG = 110  # 获取解码器参数
NET_DVR_SET_DECODERCFG = 111  # 设置解码器参数
NET_DVR_GET_RS232CFG = 112  # 获取232串口参数
NET_DVR_SET_RS232CFG = 113  # 设置232串口参数
NET_DVR_GET_ALARMINCFG = 114  # 获取报警输入参数
NET_DVR_SET_ALARMINCFG = 115  # 设置报警输入参数
NET_DVR_GET_ALARMOUTCFG = 116  # 获取报警输出参数
NET_DVR_SET_ALARMOUTCFG = 117  # 设置报警输出参数
NET_DVR_GET_TIMECFG = 118  # 获取DVR时间
NET_DVR_SET_TIMECFG = 119  # 设置DVR时间
NET_DVR_GET_PREVIEWCFG = 120  # 获取预览参数
NET_DVR_SET_PREVIEWCFG = 121  # 设置预览参数
NET_DVR_GET_VIDEOOUTCFG = 122  # 获取视频输出参数
NET_DVR_SET_VIDEOOUTCFG = 123  # 设置视频输出参数
NET_DVR_GET_USERCFG = 124  # 获取用户参数
NET_DVR_SET_USERCFG = 125  # 设置用户参数
NET_DVR_GET_EXCEPTIONCFG = 126  # 获取异常参数
NET_DVR_SET_EXCEPTIONCFG = 127  # 设置异常参数
NET_DVR_GET_ZONEANDDST = 128  # 获取时区和夏时制参数
NET_DVR_SET_ZONEANDDST = 129  # 设置时区和夏时制参数
NET_DVR_GET_SHOWSTRING = 130  # 获取叠加字符参数
NET_DVR_SET_SHOWSTRING = 131  # 设置叠加字符参数
NET_DVR_GET_EVENTCOMPCFG = 132  # 获取事件触发录像参数
NET_DVR_SET_EVENTCOMPCFG = 133  # 设置事件触发录像参数
NET_DVR_GET_AUXOUTCFG = 140  # 获取报警触发辅助输出设置(HS设备辅助输出2006-02-28)
NET_DVR_SET_AUXOUTCFG = 141  # 设置报警触发辅助输出设置(HS设备辅助输出2006-02-28)
NET_DVR_GET_PREVIEWCFG_AUX = 142  # 获取-s系列双输出预览参数(-s系列双输出2006-04-13)
NET_DVR_SET_PREVIEWCFG_AUX = 143  # 设置-s系列双输出预览参数(-s系列双输出2006-04-13)
NET_DVR_GET_PICCFG_EX = 200  # 获取图象参数(SDK_V14扩展命令)
NET_DVR_SET_PICCFG_EX = 201  # 设置图象参数(SDK_V14扩展命令)
NET_DVR_GET_USERCFG_EX = 202  # 获取用户参数(SDK_V15扩展命令)
NET_DVR_SET_USERCFG_EX = 203  # 设置用户参数(SDK_V15扩展命令)
NET_DVR_GET_COMPRESSCFG_EX = 204  # 获取压缩参数(SDK_V15扩展命令2006-05-15)
NET_DVR_SET_COMPRESSCFG_EX = 205  # 设置压缩参数(SDK_V15扩展命令2006-05-15)
NET_DVR_GET_NETAPPCFG = 222  # 获取网络应用参数 NTP/DDNS/EMAIL
NET_DVR_SET_NETAPPCFG = 223  # 设置网络应用参数 NTP/DDNS/EMAIL
NET_DVR_GET_NTPCFG = 224  # 获取网络应用参数 NTP
NET_DVR_SET_NTPCFG = 225  # 设置网络应用参数 NTP
NET_DVR_GET_DDNSCFG = 226  # 获取网络应用参数 DDNS
NET_DVR_SET_DDNSCFG = 227  # 设置网络应用参数 DDNS
NET_DVR_GET_DEVICECFG_V40 = 1100  # 获取设备参数(扩展)
NET_DVR_GET_AUDIO_INPUT = 3201  # 获取音频输入参数
NET_DVR_SET_AUDIO_INPUT = 3202  # 设置音频输入参数
# 对应NET_DVR_EMAILPARA
NET_DVR_GET_EMAILCFG = 228  # 获取网络应用参数 EMAIL
NET_DVR_SET_EMAILCFG = 229  # 设置网络应用参数 EMAIL
NET_DVR_GET_NFSCFG = 230  # NFS disk config */
NET_DVR_SET_NFSCFG = 231  # NFS disk config */
NET_DVR_GET_SHOWSTRING_EX = 238  # 获取叠加字符参数扩展(支持8条字符)
NET_DVR_SET_SHOWSTRING_EX = 239  # 设置叠加字符参数扩展(支持8条字符)
NET_DVR_GET_NETCFG_OTHER = 244  # 获取网络参数
NET_DVR_SET_NETCFG_OTHER = 245  # 设置网络参数
# 对应NET_DVR_EMAILCFG结构
NET_DVR_GET_EMAILPARACFG = 250  # Get EMAIL parameters
NET_DVR_SET_EMAILPARACFG = 251  # Setup EMAIL parameters
NET_DVR_GET_DDNSCFG_EX = 274  # 获取扩展DDNS参数
NET_DVR_SET_DDNSCFG_EX = 275  # 设置扩展DDNS参数
NET_DVR_SET_PTZPOS = 292  # 云台设置PTZ位置
NET_DVR_GET_PTZPOS = 293  # 云台获取PTZ位置
NET_DVR_GET_PTZSCOPE = 294  # 云台获取PTZ范围
# 用于NET_DVR_GetDeviceConfig和NET_DVR_SetDeviceConfig批量获取设备配置信息
NET_DVR_GET_MULTI_STREAM_COMPRESSIONCFG = 3216  # 远程获取多码流压缩参数
NET_DVR_SET_MULTI_STREAM_COMPRESSIONCFG = 3217  # 远程设置多码流压缩参数
# **************************DS9000新增命令(_V30) begin *****************************/
# 网络(NET_DVR_NETCFG_V30结构)
NET_DVR_GET_NETCFG_V30 = 1000  # 获取网络参数
NET_DVR_SET_NETCFG_V30 = 1001  # 设置网络参数
# 图象(NET_DVR_PICCFG_V30结构)
NET_DVR_GET_PICCFG_V30 = 1002  # 获取图象参数
NET_DVR_SET_PICCFG_V30 = 1003  # 设置图象参数
# 录像时间(NET_DVR_RECORD_V30结构)
NET_DVR_GET_RECORDCFG_V30 = 1004  # 获取录像参数
NET_DVR_SET_RECORDCFG_V30 = 1005  # 设置录像参数
# 用户(NET_DVR_USER_V30结构)
NET_DVR_GET_USERCFG_V30 = 1006  # 获取用户参数
NET_DVR_SET_USERCFG_V30 = 1007  # 设置用户参数
# 9000DDNS参数配置(NET_DVR_DDNSPARA_V30结构)
NET_DVR_GET_DDNSCFG_V30 = 1010  # 获取DDNS(9000扩展)
NET_DVR_SET_DDNSCFG_V30 = 1011  # 设置DDNS(9000扩展)
# EMAIL功能(NET_DVR_EMAILCFG_V30结构)
NET_DVR_GET_EMAILCFG_V30 = 1012  # 获取EMAIL参数
NET_DVR_SET_EMAILCFG_V30 = 1013  # 设置EMAIL参数
# 巡航参数 (NET_DVR_CRUISE_PARA结构)
NET_DVR_GET_CRUISE = 1020
NET_DVR_SET_CRUISE = 1021
# 报警输入结构参数 (NET_DVR_ALARMINCFG_V30结构)
NET_DVR_GET_ALARMINCFG_V30 = 1024
NET_DVR_SET_ALARMINCFG_V30 = 1025
# 报警输出结构参数 (NET_DVR_ALARMOUTCFG_V30结构)
NET_DVR_GET_ALARMOUTCFG_V30 = 1026
NET_DVR_SET_ALARMOUTCFG_V30 = 1027
# 视频输出结构参数 (NET_DVR_VIDEOOUT_V30结构)
NET_DVR_GET_VIDEOOUTCFG_V30 = 1028
NET_DVR_SET_VIDEOOUTCFG_V30 = 1029
# 叠加字符结构参数 (NET_DVR_SHOWSTRING_V30结构)
NET_DVR_GET_SHOWSTRING_V30 = 1030
NET_DVR_SET_SHOWSTRING_V30 = 1031
# 异常结构参数 (NET_DVR_EXCEPTION_V30结构)
NET_DVR_GET_EXCEPTIONCFG_V30 = 1034
NET_DVR_SET_EXCEPTIONCFG_V30 = 1035
# 串口232结构参数 (NET_DVR_RS232CFG_V30结构)
NET_DVR_GET_RS232CFG_V30 = 1036
NET_DVR_SET_RS232CFG_V30 = 1037
# 压缩参数 (NET_DVR_COMPRESSIONCFG_V30结构)
NET_DVR_GET_COMPRESSCFG_V30 = 1040
NET_DVR_SET_COMPRESSCFG_V30 = 1041
# 获取485解码器参数 (NET_DVR_DECODERCFG_V30结构)
NET_DVR_GET_DECODERCFG_V30 = 1042  # 获取解码器参数
NET_DVR_SET_DECODERCFG_V30 = 1043  # 设置解码器参数
# 获取预览参数 (NET_DVR_PREVIEWCFG_V30结构)
NET_DVR_GET_PREVIEWCFG_V30 = 1044  # 获取预览参数
NET_DVR_SET_PREVIEWCFG_V30 = 1045  # 设置预览参数
# 辅助预览参数 (NET_DVR_PREVIEWCFG_AUX_V30结构)
NET_DVR_GET_PREVIEWCFG_AUX_V30 = 1046  # 获取辅助预览参数
NET_DVR_SET_PREVIEWCFG_AUX_V30 = 1047  # 设置辅助预览参数
# IP接入配置参数 （NET_DVR_IPPARACFG结构）
NET_DVR_GET_IPPARACFG = 1048  # 获取IP接入配置信息
NET_DVR_SET_IPPARACFG = 1049  # 设置IP接入配置信息
# IP报警输入接入配置参数 （NET_DVR_IPALARMINCFG结构）
NET_DVR_GET_IPALARMINCFG = 1050  # 获取IP报警输入接入配置信息
NET_DVR_SET_IPALARMINCFG = 1051  # 设置IP报警输入接入配置信息
# IP报警输出接入配置参数 （NET_DVR_IPALARMOUTCFG结构）
NET_DVR_GET_IPALARMOUTCFG = 1052  # 获取IP报警输出接入配置信息
NET_DVR_SET_IPALARMOUTCFG = 1053  # 设置IP报警输出接入配置信息
# 硬盘管理的参数获取 (NET_DVR_HDCFG结构)
NET_DVR_GET_HDCFG = 1054  # 获取硬盘管理配置参数
NET_DVR_SET_HDCFG = 1055  # 设置硬盘管理配置参数
# 盘组管理的参数获取 (NET_DVR_HDGROUP_CFG结构)
NET_DVR_GET_HDGROUP_CFG = 1056  # 获取盘组管理配置参数
NET_DVR_SET_HDGROUP_CFG = 1057  # 设置盘组管理配置参数
# 设备编码类型配置(NET_DVR_COMPRESSION_AUDIO结构)
NET_DVR_GET_COMPRESSCFG_AUD = 1058  # 获取设备语音对讲编码参数
NET_DVR_SET_COMPRESSCFG_AUD = 1059  # 设置设备语音对讲编码参数
# 设备的配置信息配置
NET_DVR_GET_ISP_CAMERAPARAMCFG = 3255  # 获取设备的配置信息
NET_DVR_SET_ISP_CAMERAPARAMCFG = 3256  # 设置设备的配置信息
# **************************DS9000新增命令(_V30) end *****************************/
# ************************参数配置命令 end*******************************/
# ******************查找文件和日志函数返回值*************************/
NET_DVR_FILE_SUCCESS = 1000  # 获得文件信息
NET_DVR_FILE_NOFIND = 1001  # 没有文件
NET_DVR_ISFINDING = 1002  # 正在查找文件
NET_DVR_NOMOREFILE = 1003  # 查找文件时没有更多的文件
NET_DVR_FILE_EXCEPTION = 1004  # 查找文件时异常
# ********************回调函数类型 begin************************/
COMM_ALARM = 0x1100  # 8000报警信息主动上传
COMM_TRADEINFO = 0x1500  # ATMDVR主动上传交易信息
COMM_ALARM_V30 = 0x4000  # 9000报警信息主动上传
COMM_ALARM_V40 = 0x4007
COMM_IPCCFG = 0x4001  # 9000设备IPC接入配置改变报警信息主动上传
COMM_ALARM_PDC = 0x1103  # 客流量统计报警上传
COMM_UPLOAD_PLATE_RESULT = 0x2800  # 交通抓拍结果(车辆、车牌识别及抓拍图片)上传
# ************操作异常类型(消息方式, 回调方式(保留))****************/
EXCEPTION_EXCHANGE = 0x8000  # 用户交互时异常
EXCEPTION_AUDIOEXCHANGE = 0x8001  # 语音对讲异常
EXCEPTION_ALARM = 0x8002  # 报警异常
EXCEPTION_PREVIEW = 0x8003  # 网络预览异常
EXCEPTION_SERIAL = 0x8004  # 透明通道异常
EXCEPTION_RECONNECT = 0x8005  # 预览时重连
EXCEPTION_ALARMRECONNECT = 0x8006  # 报警时重连
EXCEPTION_SERIALRECONNECT = 0x8007  # 透明通道重连
EXCEPTION_PLAYBACK = 0x8010  # 回放异常
EXCEPTION_DISKFMT = 0x8011  # 硬盘格式化
# *******************预览回调函数*********************/
NET_DVR_SYSHEAD = 1  # 系统头数据
NET_DVR_STREAMDATA = 2  # 视频流数据（包括复合流和音视频分开的视频流数据）
NET_DVR_AUDIOSTREAMDATA = 3  # 音频流数据
NET_DVR_STD_VIDEODATA = 4  # 标准视频流数据
NET_DVR_STD_AUDIODATA = 5  # 标准音频流数据
# 回调预览中的状态和消息
NET_DVR_REALPLAYEXCEPTION = 111  # 预览异常
NET_DVR_REALPLAYNETCLOSE = 112  # 预览时连接断开
NET_DVR_REALPLAY5SNODATA = 113  # 预览5s没有收到数据
NET_DVR_REALPLAYRECONNECT = 114  # 预览重连
# *******************回放回调函数*********************/
NET_DVR_PLAYBACKOVER = 101  # 回放数据播放完毕
NET_DVR_PLAYBACKEXCEPTION = 102  # 回放异常
NET_DVR_PLAYBACKNETCLOSE = 103  # 回放时候连接断开
NET_DVR_PLAYBACK5SNODATA = 104  # 回放5s没有收到数据
# ********************回调函数类型 end************************/
# 设备型号(DVR类型)
# 设备类型 */
DVR = 1  # 对尚未定义的dvr类型返回NETRET_DVR*/
ATMDVR = 2  # atm dvr*/
DVS = 3  # DVS*/
DEC = 4  # 6001D */
ENC_DEC = 5  # 6001F */
DVR_HC = 6  # 8000HC*/
DVR_HT = 7  # 8000HT*/
DVR_HF = 8  # 8000HF*/
DVR_HS = 9  # 8000HS DVR(no audio) */
DVR_HTS = 10  # 8016HTS DVR(no audio) */
DVR_HB = 11  # HB DVR(SATA HD) */
DVR_HCS = 12  # 8000HCS DVR */
DVS_A = 13  # 带ATA硬盘的DVS */
DVR_HC_S = 14  # 8000HC-S */
DVR_HT_S = 15  # 8000HT-S */
DVR_HF_S = 16  # 8000HF-S */
DVR_HS_S = 17  # 8000HS-S */
ATMDVR_S = 18  # ATM-S */
LOWCOST_DVR = 19  # 7000H系列*/
DEC_MAT = 20  # 多路解码器*/
DVR_MOBILE = 21  # mobile DVR */
DVR_HD_S = 22  # 8000HD-S */
DVR_HD_SL = 23  # 8000HD-SL */
DVR_HC_SL = 24  # 8000HC-SL */
DVR_HS_ST = 25  # 8000HS_ST */
DVS_HW = 26  # 6000HW */
IPCAM = 30  # IP 摄像机*/
MEGA_IPCAM = 31  # X52MF系列,752MF,852MF*/
IPCAM_X62MF = 32  # X62MF系列可接入9000设备,762MF,862MF*/
IPDOME = 40  # IP标清快球*/
MEGA_IPDOME = 41  # IP高清快球*/
IPMOD = 50  # IP 模块*/
DS71XX_H = 71  # DS71XXH_S */
DS72XX_H_S = 72  # DS72XXH_S */
DS73XX_H_S = 73  # DS73XXH_S */
DS81XX_HS_S = 81  # DS81XX_HS_S */
DS81XX_HL_S = 82  # DS81XX_HL_S */
DS81XX_HC_S = 83  # DS81XX_HC_S */
DS81XX_HD_S = 84  # DS81XX_HD_S */
DS81XX_HE_S = 85  # DS81XX_HE_S */
DS81XX_HF_S = 86  # DS81XX_HF_S */
DS81XX_AH_S = 87  # DS81XX_AH_S */
DS81XX_AHF_S = 88  # DS81XX_AHF_S */
DS90XX_HF_S = 90  # DS90XX_HF_S*/
DS91XX_HF_S = 91  # DS91XX_HF_S*/
DS91XX_HD_S = 92  # 91XXHD-S(MD)*/

# 操作 */
# 主类型

MAJOR_OPERATION = 0x3
MAJOR_EVENT = 0x5

# 次类型
MINOR_START_DVR = 0x41  # 开机 */
MINOR_STOP_DVR = 0x42  # 关机 */
MINOR_STOP_ABNORMAL = 0x43  # 异常关机 */
MINOR_REBOOT_DVR = 0x44  # 本地重启设备*/
MINOR_LOCAL_LOGIN = 0x50  # 本地登陆 */
MINOR_LOCAL_LOGOUT = 0x51  # 本地注销登陆 */
MINOR_LOCAL_CFG_PARM = 0x52  # 本地配置参数 */
MINOR_LOCAL_PLAYBYFILE = 0x53  # 本地按文件回放或下载 */
MINOR_LOCAL_PLAYBYTIME = 0x54  # 本地按时间回放或下载*/
MINOR_LOCAL_START_REC = 0x55  # 本地开始录像 */
MINOR_LOCAL_STOP_REC = 0x56  # 本地停止录像 */
MINOR_LOCAL_PTZCTRL = 0x57  # 本地云台控制 */
MINOR_LOCAL_PREVIEW = 0x58  # 本地预览 (保留不使用)*/
MINOR_LOCAL_MODIFY_TIME = 0x59  # 本地修改时间(保留不使用) */
MINOR_LOCAL_UPGRADE = 0x5a  # 本地升级 */
MINOR_LOCAL_RECFILE_OUTPUT = 0x5b  # 本地备份录象文件 */
MINOR_LOCAL_FORMAT_HDD = 0x5c  # 本地初始化硬盘 */
MINOR_LOCAL_CFGFILE_OUTPUT = 0x5d  # 导出本地配置文件 */
MINOR_LOCAL_CFGFILE_INPUT = 0x5e  # 导入本地配置文件 */
MINOR_LOCAL_COPYFILE = 0x5f  # 本地备份文件 */
MINOR_LOCAL_LOCKFILE = 0x60  # 本地锁定录像文件 */
MINOR_LOCAL_UNLOCKFILE = 0x61  # 本地解锁录像文件 */
MINOR_LOCAL_DVR_ALARM = 0x62  # 本地手动清除和触发报警*/
MINOR_IPC_ADD = 0x63  # 本地添加IPC */
MINOR_IPC_DEL = 0x64  # 本地删除IPC */
MINOR_IPC_SET = 0x65  # 本地设置IPC */
MINOR_LOCAL_START_BACKUP = 0x66  # 本地开始备份 */
MINOR_LOCAL_STOP_BACKUP = 0x67  # 本地停止备份*/
MINOR_LOCAL_COPYFILE_START_TIME = 0x68  # 本地备份开始时间*/
MINOR_LOCAL_COPYFILE_END_TIME = 0x69  # 本地备份结束时间*/
MINOR_REMOTE_LOGIN = 0x70  # 远程登录 */
MINOR_REMOTE_LOGOUT = 0x71  # 远程注销登陆 */
MINOR_REMOTE_START_REC = 0x72  # 远程开始录像 */
MINOR_REMOTE_STOP_REC = 0x73  # 远程停止录像 */
MINOR_START_TRANS_CHAN = 0x74  # 开始透明传输 */
MINOR_STOP_TRANS_CHAN = 0x75  # 停止透明传输 */
MINOR_REMOTE_GET_PARM = 0x76  # 远程获取参数 */
MINOR_REMOTE_CFG_PARM = 0x77  # 远程配置参数 */
MINOR_REMOTE_GET_STATUS = 0x78  # 远程获取状态 */
MINOR_REMOTE_ARM = 0x79  # 远程布防 */
MINOR_REMOTE_DISARM = 0x7a  # 远程撤防 */
MINOR_REMOTE_REBOOT = 0x7b  # 远程重启 */
MINOR_START_VT = 0x7c  # 开始语音对讲 */
MINOR_STOP_VT = 0x7d  # 停止语音对讲 */
MINOR_REMOTE_UPGRADE = 0x7e  # 远程升级 */
MINOR_REMOTE_PLAYBYFILE = 0x7f  # 远程按文件回放 */
MINOR_REMOTE_PLAYBYTIME = 0x80  # 远程按时间回放 */
MINOR_REMOTE_PTZCTRL = 0x81  # 远程云台控制 */
MINOR_REMOTE_FORMAT_HDD = 0x82  # 远程格式化硬盘 */
MINOR_REMOTE_STOP = 0x83  # 远程关机 */
MINOR_REMOTE_LOCKFILE = 0x84  # 远程锁定文件 */
MINOR_REMOTE_UNLOCKFILE = 0x85  # 远程解锁文件 */
MINOR_REMOTE_CFGFILE_OUTPUT = 0x86  # 远程导出配置文件 */
MINOR_REMOTE_CFGFILE_INTPUT = 0x87  # 远程导入配置文件 */
MINOR_REMOTE_RECFILE_OUTPUT = 0x88  # 远程导出录象文件 */
MINOR_REMOTE_DVR_ALARM = 0x89  # 远程手动清除和触发报警*/
MINOR_REMOTE_IPC_ADD = 0x8a  # 远程添加IPC */
MINOR_REMOTE_IPC_DEL = 0x8b  # 远程删除IPC */
MINOR_REMOTE_IPC_SET = 0x8c  # 远程设置IPC */
MINOR_REBOOT_VCA_LIB = 0x8d  # 重启智能库*/

# 日志附加信息*/
# 主类型
MAJOR_INFORMATION = 0x4  # 附加信息*/
# 次类型
MINOR_HDD_INFO = 0xa1  # 硬盘信息*/
MINOR_SMART_INFO = 0xa2  # SMART信息*/
MINOR_REC_START = 0xa3  # 开始录像*/
MINOR_REC_STOP = 0xa4  # 停止录像*/
MINOR_REC_OVERDUE = 0xa5  # 过期录像删除*/
MINOR_LINK_START = 0xa6  # ivms，多路解码器等连接前端设备
MINOR_LINK_STOP = 0xa7  # ivms，多路解码器等断开前端设备　
MINOR_NET_DISK_INFO = 0xa8
MINOR_RAID_INFO = 0xa9
MINOR_RUN_STATUS_INFO = 0xaa
# 当日志的主类型为MAJOR_OPERATION=03，次类型为MINOR_LOCAL_CFG_PARM=0x52或者MINOR_REMOTE_GET_PARM=0x76或者MINOR_REMOTE_CFG_PARM=0x77时，dwParaType:参数类型有效，其含义如下：
PARA_VIDEOOUT = 0x1
PARA_IMAGE = 0x2
PARA_ENCODE = 0x4
PARA_NETWORK = 0x8
PARA_ALARM = 0x10
PARA_EXCEPTION = 0x20
PARA_DECODER = 0x40  # 解码器*/
PARA_RS232 = 0x80
PARA_PREVIEW = 0x100
PARA_SECURITY = 0x200
PARA_DATETIME = 0x400
PARA_FRAMETYPE = 0x800  # 帧格式*/
PARA_VCA_RULE = 0x1000  # 行为规则

# 主类型
MAJOR_EXCEPTION = 0x2
# 次类型
MINOR_RAID_ERROR = 0x20  # 阵列异常 */
MINOR_VI_LOST = 0x21  # 视频信号丢失 */
MINOR_ILLEGAL_ACCESS = 0x22  # 非法访问 */
MINOR_HD_FULL = 0x23  # 硬盘满 */
MINOR_HD_ERROR = 0x24  # 硬盘错误 */
MINOR_DCD_LOST = 0x25  # MODEM 掉线(保留不使用) */
MINOR_IP_CONFLICT = 0x26  # IP地址冲突 */
MINOR_NET_BROKEN = 0x27  # 网络断开 */
MINOR_REC_ERROR = 0x28  # 录像出错 */
MINOR_IPC_NO_LINK = 0x29  # IPC连接异常 */
MINOR_VI_EXCEPTION = 0x2a  # 视频输入异常(只针对模拟通道) */
MINOR_IPC_IP_CONFLICT = 0x2b  # ipc ip 地址 冲突 */
MINOR_SENCE_EXCEPTION = 0x2c  # 场景异常

# 主类型
MAJOR_ALARM = 0x1
# 次类型
MINOR_ALARM_IN = 0x1  # 报警输入 */
MINOR_ALARM_OUT = 0x2  # 报警输出 */
MINOR_MOTDET_START = 0x3  # 移动侦测报警开始 */
MINOR_MOTDET_STOP = 0x4  # 移动侦测报警结束 */
MINOR_HIDE_ALARM_START = 0x5  # 遮挡报警开始 */
MINOR_HIDE_ALARM_STOP = 0x6  # 遮挡报警结束 */
MINOR_VCA_ALARM_START = 0x7  # 智能报警开始 */
MINOR_VCA_ALARM_STOP = 0x8  # 智能报警停止 */
MINOR_ITS_ALARM_START = 0x09  # 交通事件报警开始
MINOR_ITS_ALARM_STOP = 0x0A  # 交通事件报警结束
# 2010-11-10 网络报警日志
MINOR_NETALARM_START = 0x0b  # 网络报警开始 */
MINOR_NETALARM_STOP = 0x0c  # 网络报警结束 */
# 2010-12-16 报警板日志，与"MINOR_ALARM_IN"配对使用
MINOR_NETALARM_RESUME = 0x0d  # 网络报警恢复 */
# 2012-4-5 IPC PIR、无线、呼救报警
MINOR_WIRELESS_ALARM_START = 0x0e  # 无线报警开始 */
MINOR_WIRELESS_ALARM_STOP = 0x0f  # 无线报警结束 */
MINOR_PIR_ALARM_START = 0x10  # 人体感应报警开始 */
MINOR_PIR_ALARM_STOP = 0x11  # 人体感应报警结束 */
MINOR_CALLHELP_ALARM_START = 0x12  # 呼救报警开始 */
MINOR_CALLHELP_ALARM_STOP = 0x13  # 呼救报警结束 */
MINOR_IPCHANNEL_ALARMIN_START = 0x14  # 数字通道报警输入开始：PCNVR在接收到数字通道的MINOR_ALARM_IN产生“数字通道报警输入开始”，10s，再收不到MINOR_ALARM_IN，产生“数字通道报警输入结束”
MINOR_IPCHANNEL_ALARMIN_STOP = 0x15  # 数字通道报警输入开始：同上
MINOR_DETECTFACE_ALARM_START = 0x16  # 人脸侦测报警开始 */
MINOR_DETECTFACE_ALARM_STOP = 0x17  # 人脸侦测报警结束 */
MINOR_VQD_ALARM_START = 0x18  # VQD报警
MINOR_VQD_ALARM_STOP = 0x19  # VQD报警结束
MINOR_VCA_SECNECHANGE_DETECTION = 0x1a  # 场景侦测报警
# 2013-07-16

MINOR_SMART_REGION_EXITING_BEGIN = 0x1b  # 离开区域侦测开始
MINOR_SMART_REGION_EXITING_END = 0x1c  # 离开区域侦测结束
MINOR_SMART_LOITERING_BEGIN = 0x1d  # 徘徊侦测开始
MINOR_SMART_LOITERING_END = 0x1e  # 徘徊侦测结束

MINOR_VCA_ALARM_LINE_DETECTION_BEGIN = 0x20
MINOR_VCA_ALARM_LINE_DETECTION_END = 0x21
MINOR_VCA_ALARM_INTRUDE_BEGIN = 0x22  # 区域侦测开始
MINOR_VCA_ALARM_INTRUDE_END = 0x23  # 区域侦测结束
MINOR_VCA_ALARM_AUDIOINPUT = 0x24  # 音频异常输入
MINOR_VCA_ALARM_AUDIOABNORMAL = 0x25  # 声强突变
MINOR_VCA_DEFOCUS_DETECTION_BEGIN = 0x26  # 虚焦侦测开始
MINOR_VCA_DEFOCUS_DETECTION_END = 0x27  # 虚焦侦测结束

# 民用NVR
MINOR_EXT_ALARM = 0x28  # IPC外部报警 */
MINOR_VCA_FACE_ALARM_BEGIN = 0x29  # 人脸侦测开始 */
MINOR_SMART_REGION_ENTRANCE_BEGIN = 0x2a  # 进入区域侦测开始
MINOR_SMART_REGION_ENTRANCE_END = 0x2b  # 进入区域侦测结束
MINOR_SMART_PEOPLE_GATHERING_BEGIN = 0x2c  # 人员聚集侦测开始
MINOR_SMART_PEOPLE_GATHERING_END = 0x2d  # 人员聚集侦测结束
MINOR_SMART_FAST_MOVING_BEGIN = 0x2e  # 快速运动侦测开始
MINOR_SMART_FAST_MOVING_END = 0x2f  # 快速运动侦测结束

MINOR_VCA_FACE_ALARM_END = 0x30  # 人脸侦测结束 */
MINOR_VCA_SCENE_CHANGE_ALARM_BEGIN = 0x31  # 场景变更侦测开始 */
MINOR_VCA_SCENE_CHANGE_ALARM_END = 0x32  # 场景变更侦测结束 */
MINOR_VCA_ALARM_AUDIOINPUT_BEGIN = 0x33  # 音频异常输入开始 */
MINOR_VCA_ALARM_AUDIOINPUT_END = 0x34  # 音频异常输入结束 */
MINOR_VCA_ALARM_AUDIOABNORMAL_BEGIN = 0x35  # 声强突变侦测开始 */
MINOR_VCA_ALARM_AUDIOABNORMAL_END = 0x36  # 声强突变侦测结束 */

MINOR_VCA_LECTURE_DETECTION_BEGIN = 0x37  # 授课侦测开始报警
MINOR_VCA_LECTURE_DETECTION_END = 0x38  # 授课侦测结束报警
MINOR_VCA_ALARM_AUDIOSTEEPDROP = 0x39  # 声强陡降
# 2014-03-21
MINOR_VCA_ANSWER_DETECTION_BEGIN = 0x3a  # 回答问题侦测开始报警
MINOR_VCA_ANSWER_DETECTION_END = 0x3b  # 回答问题侦测结束报警

MINOR_SMART_PARKING_BEGIN = 0x3c  # 停车侦测开始
MINOR_SMART_PARKING_END = 0x3d  # 停车侦测结束
MINOR_SMART_UNATTENDED_BAGGAGE_BEGIN = 0x3e  # 物品遗留侦测开始
MINOR_SMART_UNATTENDED_BAGGAGE_END = 0x3f  # 物品遗留侦测结束
MINOR_SMART_OBJECT_REMOVAL_BEGIN = 0x40  # 物品拿取侦测开始
MINOR_SMART_OBJECT_REMOVAL_END = 0x41  # 物品拿取侦测结束
MINOR_SMART_VEHICLE_ALARM_START = 0x46  # 车牌检测开始
MINOR_SMART_VEHICLE_ALARM_STOP = 0x47  # 车牌检测结束
MINOR_THERMAL_FIREDETECTION = 0x48  # 热成像火点检测侦测开始
MINOR_THERMAL_FIREDETECTION_END = 0x49  # 热成像火点检测侦测结束
MINOR_SMART_VANDALPROOF_BEGIN = 0x50  # 防破坏检测开始
MINOR_SMART_VANDALPROOF_END = 0x51  # 防破坏检测结束

# 0x400-0x1000 门禁报警
MINOR_ALARMIN_SHORT_CIRCUIT = 0x400  # 防区短路报警
MINOR_ALARMIN_BROKEN_CIRCUIT = 0x401  # 防区断路报警
MINOR_ALARMIN_EXCEPTION = 0x402  # 防区异常报警
MINOR_ALARMIN_RESUME = 0x403  # 防区报警恢复
MINOR_HOST_DESMANTLE_ALARM = 0x404  # 防区防拆报警
MINOR_HOST_DESMANTLE_RESUME = 0x405  # 防区防拆恢复
MINOR_CARD_READER_DESMANTLE_ALARM = 0x406  # 读卡器防拆报警
MINOR_CARD_READER_DESMANTLE_RESUME = 0x407  # 读卡器防拆恢复
MINOR_CASE_SENSOR_ALARM = 0x408  # 事件输入报警
MINOR_CASE_SENSOR_RESUME = 0x409  # 事件输入恢复
MINOR_STRESS_ALARM = 0x40a  # 胁迫报警
MINOR_OFFLINE_ECENT_NEARLY_FULL = 0x40b  # 离线事件满90%报警
MINOR_CARD_MAX_AUTHENTICATE_FAIL = 0x40c  # 卡号认证失败超次报警
MINOR_SD_CARD_FULL = 0x40d  # SD卡存储满报警
MINOR_LINKAGE_CAPTURE_PIC = 0x40e  # 联动抓拍事件报警
# SDK_V222
# 智能设备类型
DS6001_HF_B = 60  # 行为分析：DS6001-HF/B
DS6001_HF_P = 61  # 车牌识别：DS6001-HF/P
DS6002_HF_B = 62  # 双机跟踪：DS6002-HF/B
DS6101_HF_B = 63  # 行为分析：DS6101-HF/B
IVMS_2000 = 64  # 智能分析仪
DS9000_IVS = 65  # 9000系列智能DVR
DS8004_AHL_A = 66  # 智能ATM, DS8004AHL-S/A
DS6101_HF_P = 67  # 车牌识别：DS6101-HF/P
# 能力获取命令
VCA_DEV_ABILITY = 0x100  # 设备智能分析的总能力
VCA_CHAN_ABILITY = 0x110  # 行为分析能力
# 获取/设置大接口参数配置命令
# 车牌识别（NET_VCA_PLATE_CFG）
NET_DVR_SET_PLATECFG = 150  # 设置车牌识别参数

NET_DVR_GET_PLATECFG = 151  # 获取车牌识别参数
# 行为对应（NET_VCA_RULECFG）
NET_DVR_SET_RULECFG = 152  # 设置行为分析规则
NET_DVR_GET_RULECFG = 153  # 获取行为分析规则,
# 双摄像机标定参数（NET_DVR_LF_CFG）
NET_DVR_SET_LF_CFG = 160  # 设置双摄像机的配置参数
NET_DVR_GET_LF_CFG = 161  # 获取双摄像机的配置参数
# 智能分析仪取流配置结构
NET_DVR_SET_IVMS_STREAMCFG = 162  # 设置智能分析仪取流参数
NET_DVR_GET_IVMS_STREAMCFG = 163  # 获取智能分析仪取流参数
# 智能控制参数结构
NET_DVR_SET_VCA_CTRLCFG = 164  # 设置智能控制参数
NET_DVR_GET_VCA_CTRLCFG = 165  # 获取智能控制参数
# 屏蔽区域NET_VCA_MASK_REGION_LIST
NET_DVR_SET_VCA_MASK_REGION = 166  # 设置屏蔽区域参数
NET_DVR_GET_VCA_MASK_REGION = 167  # 获取屏蔽区域参数
# ATM进入区域 NET_VCA_ENTER_REGION
NET_DVR_SET_VCA_ENTER_REGION = 168  # 设置进入区域参数
NET_DVR_GET_VCA_ENTER_REGION = 169  # 获取进入区域参数
# 标定线配置NET_VCA_LINE_SEGMENT_LIST
NET_DVR_SET_VCA_LINE_SEGMENT = 170  # 设置标定线
NET_DVR_GET_VCA_LINE_SEGMENT = 171  # 获取标定线
# ivms屏蔽区域NET_IVMS_MASK_REGION_LIST
NET_DVR_SET_IVMS_MASK_REGION = 172  # 设置IVMS屏蔽区域参数
NET_DVR_GET_IVMS_MASK_REGION = 173  # 获取IVMS屏蔽区域参数
# ivms进入检测区域NET_IVMS_ENTER_REGION
NET_DVR_SET_IVMS_ENTER_REGION = 174  # 设置IVMS进入区域参数
NET_DVR_GET_IVMS_ENTER_REGION = 175  # 获取IVMS进入区域参数
NET_DVR_SET_IVMS_BEHAVIORCFG = 176  # 设置智能分析仪行为规则参数
NET_DVR_GET_IVMS_BEHAVIORCFG = 177  # 获取智能分析仪行为规则参数

NET_ITC_GET_TRIGGERCFG = 3003  # 获取触发参数
NET_ITC_SET_TRIGGERCFG = 3004  # 设置触发参数

STREAM_ID_LEN = 32
NET_DVR_DEV_ADDRESS_MAX_LEN = 129
NET_DVR_LOGIN_USERNAME_MAX_LEN = 64
NET_DVR_LOGIN_PASSWD_MAX_LEN = 64
CARDNUM_LEN_OUT = 32
GUID_LEN = 16
MAX_IOSPEED_GROUP_NUM = 4
MAX_CHJC_NUM = 3
MAX_INTERVAL_NUM = 4
MAX_IOOUT_NUM = 4
MAX_LANEAREA_NUM = 2
ITC_MAX_POLYGON_POINT_NUM = 20
MAX_LICENSE_LEN = 16
MAX_AUDIO_V40 = 8
DEV_ID_LEN = 32
MAX_IP_DEVICE_V40 = 64
MAX_DEVICES = 512  # max device number
MAX_CHANNUM_V40 = 512

ALARM_INFO_T = 0
OPERATION_SUCC_T = 1
OPERATION_FAIL_T = 2
PLAY_SUCC_T = 3
PLAY_FAIL_T = 4
