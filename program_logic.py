# -*- coding: utf-8 -*-


def modify_score(original_score):
    """
    將學生分數根據以下規則調整後, 依序輸出新的分數:
    規則 1: 如果原分數的下一個最接近的 5 的倍數跟原分數的差在 3 以下，新分數則為下一個最接近的 5 的倍數
    規則 2: 如果新分數小於 40 分，不予加分 (保持原分數)。
    """
    for name, score in original_score.items():
        new_score = score + (5 - score % 5) if (score % 5 >= 2) else score  # 規則 1
        new_score = score if (new_score < 40) else new_score  # 規則 2
        print(f'{name}: {score} -> {new_score}')


def calculate_falling_distance(initial_high, n):
    """
    建立 generator, 迭代並 return 每次的回彈值
    """
    for i in range(1, n+1):
        yield initial_high*(1/2)**i


def record_falling_distance(initial_high, n):
    """
    根據每次回彈值, 總結每次回彈後的 total 距離 & 各次的回彈值
    """
    total = initial_high

    print(f'Start falling: initial_hight = {initial_high}; obeservate for {n} time(s)')
    falling_distance = calculate_falling_distance(initial_high, n)
    for idx, i in enumerate(falling_distance):
        print(f'#{idx+1}: total = {total}; rebound = {i}')
        total += 2*i


if __name__ == '__main__':

    print('Q1 ---')
    original_score = {'德瑞克': 33, '尚恩': 73, '傑夫': 63, '馬基': 39}
    modify_score(original_score)

    print('\nQ2 ---')
    record_falling_distance(100, 10)

