import sys


filename = "exp/ivector_gauss512_dim200/scores/plda_scores"

# 从命令行获取参数
if len(sys.argv) > 1:
    plda_threshold = float(sys.argv[1])
else:
    print("请提供一个PLDA得分阈值作为输入。")
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
    if score >= plda_threshold:
        print(f"音频 {label2} 识别成功，得分 {score}")
    else:
        print(f"音频 {label2} 识别失败，得分 {score}")

