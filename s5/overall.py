import sys

filename = "exp/ivector_gauss512_dim200/scores/plda_scores"

if len(sys.argv) > 1:
    plda_threshold = float(sys.argv[1])
else:
    print("请提供PLDA得分阈值")
    sys.exit(1)

user = {}

# 读取文件
with open(filename, "r") as file:
    lines = file.readlines()

# 收集所有label
for line in lines:
    item = line.strip().split(" ")
    if item[0] not in user:
        user[item[0]] = {}
        user[item[0]][item[1]] = float(item[2])
    else:
        user[item[0]][item[1]] = float(item[2])

correct = 0
wrong = 0

# 查找指定label的最高score及对应的第一列label
for label_to_search in user:
    max_score = float("-inf")
    label_with_max_score = None
    for wav_file in user[label_to_search]:
        score = user[label_to_search][wav_file]
        if score > max_score:
            max_score = score
            label_with_max_score = wav_file[0:6]
    if max_score < plda_threshold:
        print(f'{label_to_search} 没有找到相似的音频')
        wrong += 1
    elif label_to_search != label_with_max_score:
        print(f'{label_to_search} 识别错误, 识别成了 {label_with_max_score}, 得分为 {max_score}')
        wrong += 1
    else:
        print(f'{label_to_search} 识别成功, 得分为 {max_score}')
        correct += 1

print(f"{correct+wrong}个人的识别准确率是{str(correct/(correct+wrong)*100)+'%'}")
