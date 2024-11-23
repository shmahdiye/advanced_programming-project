import math


def calculate_final_grade():
    number = get_number_of_scores()
    weight_scores = parse_weight_score(number)
    numeric_score = calculate_weighted_average(weight_scores)
    result = convert_score_to_grade(math.ceil(numeric_score))
    return result


def get_number_of_scores():
    number = int(input("Enter the number of exams:"))
    return number


def parse_weight_score(number):
    weight_scores = []
    for i in range(number):
        weight, score = input("Enter weight space grade :").split()
        weight = int(weight)
        weight_scores.append((weight, score))
    return weight_scores


def calculate_weighted_average(weight_scores):
    sum_ = 0
    total_weights = 0
    for weight, score in weight_scores:
        sum_ += weight * to_numeral(score)
        total_weights += weight
    numeric_score = sum_ / total_weights
    return numeric_score


def to_numeral(ch_score):
    scores = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
    return scores[ch_score]


def convert_score_to_grade(num_score):
    scores = {5: 'A', 4: 'B', 3: 'C', 2: 'D', 1: 'E', 0: 'F'}
    return scores[num_score]


if __name__ == '__main__':
    final_score = calculate_final_grade()
    print(final_score)

