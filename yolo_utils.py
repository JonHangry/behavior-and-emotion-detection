import subprocess

def run_yolo_detection(weights_path='bestcrowd.pt', source_path='data/images'):
    """
    运行 YOLO 模型进行图像检测

    :param weights_path: 模型权重文件路径
    :param source_path: 图像来源路径
    """
    command = [
        'python3', 'detect.py',  # 指定 Python 和脚本文件
        '--weights', weights_path,  # 权重路径
        '--source', source_path  # 源图像路径
    ]

    try:
        # 执行命令
        subprocess.run(command, check=True)
        print("YOLO detection completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# 示例调用
if __name__ == "__main__":
    run_yolo_detection('bestcrowd.pt', 'data/images')
