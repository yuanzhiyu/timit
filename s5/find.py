import sys

filename = "exp/ivector_gauss512_dim200/scores/plda_scores"
user = {}

# 从命令行获取参数
if len(sys.argv) > 2:
    label_to_search = sys.argv[1]
    plda_threshold = float(sys.argv[2])
else:
    print("请提供要搜索的用户和PLDA得分阈值")
    sys.exit(1)

# 读取文件
with open(filename, "r") as file:
    lines = file.readlines()
    
# 解析文件内容
for line in lines:
    item = line.strip().split(" ")
    if item[0] not in user:
        user[item[0]] = {}
        user[item[0]][item[1]] = float(item[2])
    else:
        user[item[0]][item[1]] = float(item[2])

if label_to_search not in user:
    print(f"未找到指定人 {label_to_search}。")
    sys.exit(1)

if len(user) == 1:
    suc_flag = False
    max_score_suc = float("-inf")
    max_score_fail = float("-inf")
    for wav_file in user[label_to_search]:
        score = float(user[label_to_search][wav_file])
        if score >= plda_threshold:
            #print(f"在用户 {label_to_search} 下, 音频 {wav_file} 识别成功，得分 {score}")
            if score > max_score_suc:
                max_score_suc = score
                suc_flag = True
        else:
            #print(f"在用户 {label_to_search} 下, 音频 {wav_file} 识别失败，得分 {score}")
            if score > max_score_fail:
                max_score_fail = score
    if suc_flag:
        print(f"在用户 {label_to_search} 下, PLDA阈值为 {plda_threshold}, 识别出用户 {label_to_search}, 最高得分为 {max_score_suc}")
    else:
        print(f"在用户 {label_to_search} 下, PLDA阈值为 {plda_threshold}, 没有识别出用户 {label_to_search}, 最高得分为 {max_score_fail}")
else:
    max_score = float("-inf")
    label_with_max_score = None
    for wav_file in user[label_to_search]:
        score = user[label_to_search][wav_file]
        if score > max_score:
            max_score = score
            label_with_max_score = wav_file[0:6]
    if max_score > plda_threshold:
        print(f"在用户 {label_to_search} 下, PLDA阈值为 {plda_threshold}, 识别出用户 {label_with_max_score}, 得分为 {max_score}")
    else:
        print(f"在用户 {label_to_search} 下, PLDA阈值为 {plda_threshold}, 没有识别出相似的音频, 最高得分为 {max_score}")

