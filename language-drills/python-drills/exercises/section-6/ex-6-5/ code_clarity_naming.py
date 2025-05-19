
MAX_RETRIES = 3

def calculate_score(marks: list[int]) -> float:
    if not marks:
        return 0.0
    return sum(marks) / len(marks)

def is_eligible(score: float) -> bool:
    return score >= 50

def main():
    marks = [60, 70, 80]
    score = calculate_score(marks)
    if is_eligible(score):
        print("Eligible")
    else:
        print("Not eligible")

if __name__ == "__main__":
    main()