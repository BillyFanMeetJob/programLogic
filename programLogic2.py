from collections import Counter

def count_letters_and_digits(text):
    # 先把所有字母转成大写，过滤出字母和数字
    filtered = [ch.upper() for ch in text if ch.isalpha() or ch.isdigit()]
    return dict(Counter(filtered))

# 示例输入
message = "Hello welcome to Cathay 60th year anniversary"
result = count_letters_and_digits(message)

# 输出排序后的结果
for ch in sorted(result):
    print(f"{ch} {result[ch]}")
