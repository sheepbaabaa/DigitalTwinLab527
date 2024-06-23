import numpy as np
import math


# Psize:图片尺寸[宽, 高]; point:目标点[x, y]; Cposition:相机三维坐标[x, y, z]; Rx:绕x轴旋转角度; Ry:绕x轴旋转角度; Rz:绕x轴旋转角度;
# vision:摄像头视场角[水平角度, 竖直角度]; 初始时摄像头中心线对应z轴，x和y与世界坐标相同; 旋转以逆时针为正方向
def to3d(Psize, point, Cposition, Rx, Ry, Rz, vision):
    pc_x = 2 * point[1] / Psize[1] * math.tan(vision[1] / 2)
    pc_y = 2 * point[0] / Psize[0] * math.tan(vision[0] / 2)
    # pw2 = xyz_transform(Cposition, Rx, Ry, Rz, np.array([pc_x, pc_y, 1]))
    pw1 = coordinate_transform(Cposition, [pc_x, pc_y, 1], [Rx, Ry, Rz])
    p_w1 = get_point_byZ(Cposition, pw1, 0)
    return p_w1


# 根据z坐标的值和两个直线上的点求x坐标和y坐标
def get_point_byZ(p1, p2, z):
    x = p1[0]+(p2[0]-p1[0])*(z-p1[2])/(p2[2]-p1[2])
    y = p1[1]+(p2[1]-p1[1])*(z-p1[2])/(p2[2]-p1[2])
    x = round(x, 2)
    y = round(y, 2)
    z = round(z, 2)
    return [str(x), str(y), str(z)]


# 三维坐标系的点坐标转换; o_new:相对坐标系的原点在绝对坐标系的坐标; Rx:相对坐标系绕x轴旋转角; Ry:相对坐标系绕y轴旋转角; Rz:相对坐标系绕z轴旋转角
# point:相对坐标系中的坐标
def xyz_transform(o_new, Rx, Ry, Rz, point):
    R_x = np.array([[1, 0, 0], [0, math.cos(Rx), -math.sin(Rx)], [0, math.sin(Rx), math.cos(Rx)]])
    R_y = np.array([[math.cos(Ry), 0, math.sin(Ry)], [0, 1, 0], [-math.sin(Ry), 0, math.cos(Ry)]])
    R_z = np.array([[math.cos(Rz), -math.sin(Rz), 0], [math.sin(Rz), math.cos(Rz), 0], [0, 0, 1]])
    point_new = np.dot(np.dot(np.dot(R_z, R_y), R_x), point.T) + o_new.T
    return point_new.T


def coordinate_transform(origin, point, angles):

    # 构造平移矩阵 T
    T = np.eye(4)
    T[:3, 3] = origin
    print(T)
    # 构造旋转矩阵 R
    Rx = np.array([[1, 0, 0, 0],
                   [0, np.cos(angles[0]), -np.sin(angles[0]), 0],
                   [0, np.sin(angles[0]), np.cos(angles[0]), 0],
                   [0, 0, 0, 1]])
    Ry = np.array([[np.cos(angles[1]), 0, np.sin(angles[1]), 0],
                   [0, 1, 0, 0],
                   [-np.sin(angles[1]), 0, np.cos(angles[1]), 0],
                   [0, 0, 0, 1]])
    Rz = np.array([[np.cos(angles[2]), -np.sin(angles[2]), 0, 0],
                   [np.sin(angles[2]), np.cos(angles[2]), 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    R = np.dot(np.dot(Rz, Ry), Rx)

    # 构造待转换坐标系中某点的齐次坐标
    point_homogeneous = np.array([point[0], point[1], point[2], 1])

    # 坐标转换
    transformed_point_homogeneous = np.dot(np.dot(T, R), point_homogeneous)

    # 转换后的坐标
    transformed_point = transformed_point_homogeneous[:3]

    return transformed_point


def coordinate_transform1(origin, point, angles_rad):
    # 构建旋转矩阵
    Rx = np.array([[1, 0, 0],
                   [0, math.cos(angles_rad[0]), -math.sin(angles_rad[0])],
                   [0, math.sin(angles_rad[0]), math.cos(angles_rad[0])]])

    Ry = np.array([[math.cos(angles_rad[1]), 0, math.sin(angles_rad[1])],
                   [0, 1, 0],
                   [-math.sin(angles_rad[1]), 0, math.cos(angles_rad[1])]])

    Rz = np.array([[math.cos(angles_rad[2]), -math.sin(angles_rad[2]), 0],
                   [math.sin(angles_rad[2]), math.cos(angles_rad[2]), 0],
                   [0, 0, 1]])

    # 计算旋转矩阵的乘积
    R = np.dot(Rz, np.dot(Ry, Rx))

    # 进行坐标转换
    transformed_point = np.dot(R, point) + origin

    return transformed_point


if __name__ == '__main__':
    pw = to3d(np.array([1280, 720]), np.array([-60, -78]), np.array([0.60, 2.00, 1.90]), math.pi*1/3, math.pi*2/3, 0, [math.pi*110/180, math.pi*75/180])
    print(pw)
