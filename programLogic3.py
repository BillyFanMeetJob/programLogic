def last_person(n):
    people = list(range(1, n + 1))  # 初始化人員編號為1到n
    index = 0  # 報數起始位置是第一位同事

    while len(people) > 1:
        index = (index + 2) % len(people)  # 報到第3個人（index + 2）
        people.pop(index)  # 移除報到3的人

    return people[0]

# 範例
n = 100
print(f"第 {last_person(n)} 順位")