import time

def focus_timer(duration):
    print("开始专注计时...")
    time.sleep(duration * 60)  # 将分钟转换为秒并暂停程序执行
    print("专注时间已结束！")

if __name__ == "__main__":
    focus_duration = int(input("请输入专注时长（分钟）："))
    focus_timer(focus_duration)
