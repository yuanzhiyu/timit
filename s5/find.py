import sys


filename = "exp/ivector_gauss512_dim200/scores/plda_scores"

# 从命令行获取参数
if len(sys.argv) > 1:
    label_to_search = sys.argv[1]
else:
    print("请提供要搜索的第二列label作为命令行参数。")
    sys.exit(1)

# 读取文件
with open(filename, "r") as file:
    lines = file.readlines()

# 解析文件内容
data = [line.strip().split(" ") for line in lines]

# 查找指定label的最高score及对应的第一列label
max_score = float("-inf")
label_with_max_score = None
for item in data:
    label1, label2, score = item[0], item[1], float(item[2])
    if label_to_search in label2 and score > max_score:
        max_score = score
        label_with_max_score = label1

# 打印结果
if label_with_max_score is not None and label_to_search == label_with_max_score:
    print(f"在指定人 {label_to_search} 下，识别出 {label_with_max_score}。得分是 {max_score}, 识别正确")
elif label_with_max_score is not None and label_to_search != label_with_max_score:
    print(f"在指定人 {label_to_search} 下，识别出 {label_with_max_score}。得分是 {max_score}, 识别错误")
else:
    print(f"未找到指定人 {label_to_search}。")

