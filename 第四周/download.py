import requests
import zipfile
import os

# 下载文件
url = "https://bj.bcebos.com/apollo-air/v2-2022-01-08/cooperative-vehicle-infrastructure-example_15998115871600640.zip?authorization=bce-auth-v1%2F62ff93831d5840338d0fcc9585430b3a%2F2024-06-11T15%3A54%3A12Z%2F604800%2F%2F6473e3d1dceb55ae3542df9156e28cbc679cde6cb7ec783c60b12873361c5831"
local_filename = "example.zip"

print("开始下载文件...")

response = requests.get(url)
if response.status_code == 200:
    with open(local_filename, 'wb') as f:
        f.write(response.content)
    print("文件下载完成:", local_filename)

    # 解压文件
    print("开始解压文件...")
    with zipfile.ZipFile(local_filename, 'r') as zip_ref:
        zip_ref.extractall(r"E:\Desktop\复习\小米实习\第四周\downloads")
    print("解压完成，文件保存到：E:\Desktop\复习\小米实习\第四周\downloads")
else:
    print("下载失败，状态码为：", response.status_code)
