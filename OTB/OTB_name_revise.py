import os

# 定义两个文件夹的路径
folder1_path = "E:/OTB_results/MixFormer"
folder2_path = "E:/OTB_results/Ours"

# 获取两个文件夹中的txt文件列表
folder1_files = [file for file in os.listdir(folder1_path) if file.endswith(".txt")]
folder2_files = [file for file in os.listdir(folder2_path) if file.endswith(".txt")]

# 遍历同名文件并比较行数
for file_name in folder1_files:
    if file_name in folder2_files:
        file1_path = os.path.join(folder1_path, file_name)
        file2_path = os.path.join(folder2_path, file_name)

        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()

            if len(lines1) == len(lines2):
                pass
            else:
                print(f"文件 {file_name} 行数不同")
    else:
        print(f"文件 {file_name} 在文件夹2中不存在")
