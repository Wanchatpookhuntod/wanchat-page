def get_score():
    while True:
        s = input("ใส่คะแนน: ").strip()
        try:
            score = float(s)
        except ValueError:
            print("กรุณาใส่ตัวเลขที่ถูกต้อง")
            continue
        if score < 0 or score > 100:
            print("กรุณาใส่คะแนนระหว่าง 0 ถึง 100")
            continue
        return score


def grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def main():
    score = get_score()
    g = grade(score)
    print("แสดงเกรด:", g)


if __name__ == "__main__":
    main()
