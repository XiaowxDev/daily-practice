import cv2
import numpy as np

def read_gray_image(img_path):
    """
    读取图片，转为灰度图
    :param img_path: 图片文件路径
    :return: 灰度图像二维矩阵 (高度H,宽度W)
    """
    # 读取原图，默认读取为BGR彩色图（OpenCV默认通道顺序）
    img = cv2.imread(img_path)
    # 彩色图转为单通道灰度图，降低计算量
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray


def convolve_2d(image, kernel):
    """
    实现滑动窗口卷积
    :param image: 输入灰度图像矩阵
    :param kernel: 卷积核矩阵
    :return: 卷积运算后的输出矩阵
    """
    # 获取图像高度、宽度
    img_h, img_w = image.shape
    # 获取卷积核高度、宽度（本项目是3*3）
    kernel_h, kernel_w = kernel.shape

    # Valid模式：不填充边界，计算输出图像尺寸
    out_h = img_h - kernel_h + 1
    out_w = img_w - kernel_w + 1

    # 创建空白输出矩阵，使用float存储，防止计算溢出、负数丢失
    output = np.zeros((out_h, out_w), dtype=np.float32)

    # 双层循环：卷积核从上到下滑动
    for i in range(out_h):
        # 卷积核从左到右滑动
        for j in range(out_w):
            # 截取当前位置对应的图像局部窗口
            window = image[i:i+kernel_h, j:j+kernel_w]
            # 窗口与卷积核对应位置相乘，全部求和，得到输出像素值
            output[i, j] = np.sum(window * kernel)
    return output


def sobel_edge_detect(gray_img):
    """
    Sobel边缘检测主逻辑
    :param gray_img: 输入灰度图像
    :return: 归一化后的边缘图
    """
    # 定义Sobel X卷积核，用于计算水平梯度，检测竖直边缘
    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])
    # 定义Sobel Y卷积核，用于计算竖直梯度，检测水平边缘
    sobel_y = np.array([[-1, -2, -1],
                        [0, 0, 0],
                        [1, 2, 1]])

    # 执行卷积运算，分别得到Gx、Gy梯度矩阵
    gx = convolve_2d(gray_img, sobel_x)
    gy = convolve_2d(gray_img, sobel_y)

    # 计算梯度幅值，融合两个方向的边缘信息
    magnitude = np.sqrt(gx ** 2 + gy ** 2)

    # 归一化：把计算结果缩放到0~255，转成图片可用uint8类型
    # 除以最大值，映射到0~1，再乘以255映射到像素范围
    magnitude = (magnitude / np.max(magnitude) * 255).astype(np.uint8)
    return magnitude


if __name__ == "__main__":
    # 1. 读取图片并转灰度
    gray_img = read_gray_image("test_img/test_01.png")
    # 2. 执行手写Sobel边缘检测
    edge_result = sobel_edge_detect(gray_img)

    # 3. 窗口展示原图与边缘结果图
    cv2.imshow("Original Gray Image", gray_img)
    cv2.imshow("Sobel Edge Result", edge_result)

    # 4. 将边缘图保存到output文件夹
    cv2.imwrite("output/edge_result.jpg", edge_result)

    # 等待按键，释放窗口资源
    cv2.waitKey(0)
    cv2.destroyAllWindows()