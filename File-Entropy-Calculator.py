import math
import argparse

def calculate_entropy(file_path):
    # 打开文件并读取内容
    with open(file_path, 'rb') as file:
        data = file.read()

    # 统计每个字节的出现频率
    byte_frequency = {}
    total_bytes = len(data)
    for byte in data:
        if byte in byte_frequency:
            byte_frequency[byte] += 1
        else:
            byte_frequency[byte] = 1

    # 计算每个字节的概率和熵
    entropy = 0
    for byte in byte_frequency:
        probability = byte_frequency[byte] / total_bytes
        entropy -= probability * math.log2(probability)

    return entropy

# 创建命令行参数解析器
parser = argparse.ArgumentParser(description='File-Entropy-Calculator(文件熵计算器) author: 浪飒')
parser.add_argument('-r', '--file', type=str, required=True, help='path to the file')

# 解析命令行参数
args = parser.parse_args()
file_path = args.file

entropy = calculate_entropy(file_path)
print("文件熵:", entropy)

