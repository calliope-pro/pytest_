from datetime import datetime

time_info = datetime.utcnow().strftime('%Y年%m月%d日%H時%M分')
with open('./time-info.txt', 'w') as f:
    f.write(time_info)