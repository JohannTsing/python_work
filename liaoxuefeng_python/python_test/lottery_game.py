import random

def lottery_game():
    """
    抽奖小游戏
    功能：
    1. 从300名员工中分三次抽奖
    2. 第一次抽三等奖20名，第二次抽二等奖10名，第三次抽一等奖5名
    3. 已中奖员工不会在后续抽奖中再次中奖
    """
    
    # 初始化员工池，用1-300的编号表示300名员工
    employees = set(range(1, 301))
    
    print("=== 欢迎参加公司年度抽奖活动 ===")
    print(f"当前员工池人数: {len(employees)}人")
    
    # 第一次抽奖 - 三等奖20名
    if len(employees) >= 20:
        third_prize = random.sample(sorted(employees), 20)
        employees -= set(third_prize)  # 从员工池中移除已中奖员工
        print("\n=== 三等奖中奖名单 ===")
        for i, emp in enumerate(sorted(third_prize), 1):
            print(f"{i}. 员工{emp:03d}")
    else:
        print("\n员工人数不足，无法抽取三等奖")
    
    # 第二次抽奖 - 二等奖10名
    if len(employees) >= 10:
        second_prize = random.sample(sorted(employees), 10)
        employees -= set(second_prize)  # 从员工池中移除已中奖员工
        print("\n=== 二等奖中奖名单 ===")
        for i, emp in enumerate(sorted(second_prize), 1):
            print(f"{i}. 员工{emp:03d}")
    else:
        print("\n员工人数不足，无法抽取二等奖")
    
    # 第三次抽奖 - 一等奖5名
    if len(employees) >= 5:
        first_prize = random.sample(sorted(employees), 5)
        employees -= set(first_prize)  # 从员工池中移除已中奖员工
        print("\n=== 一等奖中奖名单 ===")
        for i, emp in enumerate(sorted(first_prize), 1):
            print(f"{i}. 员工{emp:03d}")
    else:
        print("\n员工人数不足，无法抽取一等奖")
    
    print("\n=== 抽奖活动结束 ===")
    print(f"剩余未中奖员工: {len(employees)}人")

if __name__ == "__main__":
    lottery_game()