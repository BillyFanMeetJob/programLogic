def correct_scores(wrong_scores):
    def reverse_digits(n):
        return (n % 10) * 10 + (n // 10)
    
    corrected = [reverse_digits(score) for score in wrong_scores]
    return corrected

# 測試資料
wrong_scores = [35, 46, 57, 91, 29]
print(correct_scores(wrong_scores))  # 輸出應為 [53, 64, 75, 19, 92]