import os
import glob

# 指定要遍历的目录
base_directory = "timit_sre/wav/test"

# 获取目录下所有文件夹
folders = [d for d in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, d))]

# 遍历所有文件夹并重命名子文件夹中的文件
for folder in folders:
    folder_path = os.path.join(base_directory, folder)

    # 获取子文件夹中的所有文件
    files = glob.glob(os.path.join(folder_path, "*"))

    # 按照指定规则重命名文件
    for index, file in enumerate(files):
        file_extension = os.path.splitext(file)[1]
        new_name = f"{folder}W{index:02}{file_extension}"
        new_path = os.path.join(folder_path, new_name)
        os.rename(file, new_path)

    print(f"已处理文件夹: {folder}")

