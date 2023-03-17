import os
import glob
from pydub import AudioSegment

# 指定要遍历的目录
base_directory = "timit_sre/wav/test"

# 获取目录下所有文件夹
folders = [d for d in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, d))]

# 遍历所有文件夹并处理子文件夹中的音频文件
for folder in folders:
    folder_path = os.path.join(base_directory, folder)

    # 获取子文件夹中的所有音频文件
    audio_files = glob.glob(os.path.join(folder_path, "*"))

    # 转换音频文件
    for file in audio_files:
        file_extension = os.path.splitext(file)[1].lower()
        if file_extension in [".mp3", ".m4a", ".aac"]:
            # 加载音频文件
            audio = AudioSegment.from_file(file, file_extension[1:])

            # 转换采样率
            converted_audio = audio.set_frame_rate(16000)

            # 保存转换后的音频文件
            converted_file = os.path.splitext(file)[0] + ".wav"
            converted_audio.export(converted_file, format="wav")

            # 删除原始音频文件
            os.remove(file)

    print(f"已处理文件夹: {folder}")

