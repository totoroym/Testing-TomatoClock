import time
import subprocess

def focus_timer(work_minutes, break_minutes):
    print(f"专注开始，工作时间 {work_minutes} 分钟")

    # 计时工作时间
    time.sleep(work_minutes * 60)

    # 提醒休息
    subprocess.run(["notify-send", "专注时间结束", f"休息 {break_minutes} 分钟"])

    print(f"休息 {break_minutes} 分钟")

    # 计时休息时间
    time.sleep(break_minutes * 60)

if __name__ == "__main__":
    # 设置工作时间和休息时间（单位：分钟）
    work_time = 25
    break_time = 5

    # 运行专注时钟
    focus_timer(work_time, break_time)
