import sys


filename = "exp/ivector_gauss512_dim200/scores/plda_scores"

# 读取文件
with open(filename, "r") as file:
    lines = file.readlines()

# 解析文件内容
data = [line.strip().split(" ") for line in lines]

# 收集所有label
test_list = []
for item in data:
    if item[1] not in test_list:
        test_list.append(item[1])

correct = 0
wrong = 0
# 查找指定label的最高score及对应的第一列label
for label_to_search in test_list:
    max_score = float("-inf")
    label_with_max_score = None
    for item in data:
        label1, label2, score = item[0], item[1], float(item[2])
        if label2 == label_to_search and score > max_score:
            max_score = score
            label_with_max_score = label1

    if label_with_max_score == label_to_search[0:6]:
        correct += 1
        print(f'{label_with_max_score} 识别正确, 得分为 {max_score}')
    else:
        wrong += 1
        print(f'{label_to_search[0:6]} 识别错误，识别成了 {label_with_max_score}')

print(f"{correct+wrong}个人的识别准确率是{correct/(correct+wrong)}")
