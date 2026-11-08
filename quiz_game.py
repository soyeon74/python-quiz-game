from quiz import Quiz
from quiz_data import get_default_quizzes


class QuizGame:
    def __init__(self):
        self.quizzes = get_default_quizzes()
        self.best_score = None

    def get_number_input(self, prompt, min_value, max_value):
        """정해진 범위의 숫자를 안전하게 입력받습니다."""
        while True:
            try:
                value = input(prompt).strip()

                if value == "":
                    print("빈 값은 입력할 수 없습니다.")
                    continue

                number = int(value)

                if number < min_value or number > max_value:
                    print(f"{min_value}~{max_value} 사이의 숫자를 입력하세요.")
                    continue

                return number

            except ValueError:
                print("숫자만 입력하세요.")

            except (KeyboardInterrupt, EOFError):
                print("\n입력이 중단되었습니다.")
                return None

    def play_quiz(self):
        """저장된 퀴즈를 순서대로 출제합니다."""
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0

        print("\n=== 퀴즈 시작 ===")

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{number}/{len(self.quizzes)}]")
            quiz.display()

            answer = self.get_number_input(
                "정답 번호를 입력하세요 (1~4): ",
                1,
                4,
            )

            if answer is None:
                print("퀴즈를 중단합니다.")
                return

            if quiz.check_answer(answer):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print("\n=== 퀴즈 결과 ===")
        print(f"총 문제 수: {len(self.quizzes)}")
        print(f"정답 수: {score}")
        print(f"점수: {score}/{len(self.quizzes)}")

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")

    def add_quiz(self):
        """새로운 퀴즈를 추가합니다."""
        print("\n=== 퀴즈 추가 ===")

        try:
            while True:
                question = input("문제를 입력하세요: ").strip()

                if question:
                    break

                print("문제는 비워둘 수 없습니다.")

            choices = []

            for number in range(1, 5):
                while True:
                    choice = input(
                        f"{number}번 선택지를 입력하세요: "
                    ).strip()

                    if choice:
                        choices.append(choice)
                        break

                    print("선택지는 비워둘 수 없습니다.")

            answer = self.get_number_input(
                "정답 번호를 입력하세요 (1~4): ",
                1,
                4,
            )

            if answer is None:
                print("퀴즈 추가를 취소합니다.")
                return

            new_quiz = Quiz(question, choices, answer)
            self.quizzes.append(new_quiz)

            print("퀴즈가 추가되었습니다.")

        except (KeyboardInterrupt, EOFError):
            print("\n퀴즈 추가를 취소합니다.")

    def list_quizzes(self):
        """등록된 모든 퀴즈를 목록으로 보여줍니다."""
        print("\n=== 퀴즈 목록 ===")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n{number}. {quiz.question}")

            for index, choice in enumerate(quiz.choices, start=1):
                print(f"   {index}) {choice}")

        print(
            f"\n총 {len(self.quizzes)}개의 퀴즈가 등록되어 있습니다."
        )