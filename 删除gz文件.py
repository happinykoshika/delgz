import os
import time
# 设置目标文件夹路径
target_folder = './'
current_time = time.time()
three_days_ago = current_time - (3 * 24 * 60 * 60)
for root, dirs, files in os.walk(target_folder):
    for file in files:
        # 检查文件是否以.gz结尾
        if file.endswith('.gz') and file.startswith('PM'):
            # 获取文件的完整路径
            file_path = os.path.join(root, file)
            # 获取文件的修改时间
            file_mod_time = os.path.getmtime(file_path)
            # 如果文件修改时间早于三天前
            if file_mod_time < three_days_ago:
                try:
                    os.remove(file_path)
                    print(f'Deleted: {file_path}')
                except Exception as e:
                    print('移除文件错误！%s' %e)
