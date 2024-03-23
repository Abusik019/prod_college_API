from .models import Question


def calculate_exam_score(answers_data):
    """
    Функция для расчета баллов за экзамен.
    Принимает данные ответов на вопросы.
    """
    total_questions = len(answers_data)
    if total_questions == 0:
        return None

    correct_answers = 0

    for answer_data in answers_data:
        question_id = answer_data.get('question_id')
        selected_answer_id = answer_data.get('selected_answer_id')

        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            return None

        correct_answer = question.answers.filter(is_correct=True, id=selected_answer_id).exists()

        if correct_answer:
            correct_answers += 1
    percentage_correct = (correct_answers / total_questions) * 100

    if percentage_correct < 30:
        return 2
    elif 40 <= percentage_correct < 70:
        return 3
    elif 70 <= percentage_correct < 90:
        return 4
    elif 90 <= percentage_correct <= 100:
        return 5
    else:
        return None
