import json
from pathlib import Path

from quiz import Quiz
from quiz_data import get_default_quizzes


class QuizGame:
    def __init__(self):
        self.state_file = Path(__file__).resolve().parent / "state.json"
        self.quizzes = []
        self.best_score = None
        self.load_state()

    def load_state(self):
        """state.json에서 퀴즈와 최고 점수를 불러옵니다."""
        if not self.state_file.exists():
            print("저장 파일이 없어 기본 퀴즈를 사용합니다.")
            self.quizzes = get_default_quizzes()
            self.best_score = None
            self.save_state()
            return

        try:
            with open(self.state_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            quiz_data = data.get("quizzes", [])
            loaded_quizzes = []

            for item in quiz_data:
                quiz = Quiz.from_dict(item)

                if len(quiz.choices) != 4:
                    raise ValueError("선택지는 반드시 4개여야 합니다.")

                if quiz.answer < 1 or quiz.answer > 4:
                    raise ValueError("정답 번호는 1~4여야 합니다.")

                loaded_quizzes.append(quiz)

            if not loaded_quizzes:
                loaded_quizzes = get_default_quizzes()

            self.quizzes = loaded_quizzes
            self.best_score = data.get("best_score")

        except (
            json.JSONDecodeError,
            OSError,
            KeyError,
            TypeError,
            ValueError,
        ) as error:
            print(f"저장 파일을 읽는 중 문제가 발생했습니다: {error}")
            print("기본 퀴즈로 복구합니다.")

            self.quizzes = get_default_quizzes()
            self.best_score = None
            self.save_state()

    def save_state(self):
        """현재 퀴즈와 최고 점수를 state.json에 저장합니다."""
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
        }

        try:
            with open(self.state_file, "w", encoding="utf-8") as file:
                json.dump(
                    data,
                    file,
                    ensure_ascii=False,
                    indent=2,
                )

        except OSError as error:
            print(f"저장 중 오류가 발생했습니다: {error}")

    def get_number_input(self, prompt, min_value, max_value):
        """지정한 범위의 숫자를 안전하게 입력받습니다."""
        while True:
            try:
                value = input(prompt).strip()

                if value == "":
                    print("빈 값은 입력할 수 없습니다.")
                    continue

                number = int(value)

                if number < min_value or number > max_value:
                    print(
                        f"{min_value}~{max_value} 사이의 "
                        "숫자를 입력하세요."
                    )
                    continue

                return number

            except ValueError:
                print("숫자만 입력하세요.")

            except (KeyboardInterrupt, EOFError):
                print("\n입력이 중단되었습니다.")
                return None

    def play_quiz(self):
        """등록된 퀴즈를 풀고 점수를 계산합니다."""
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
                print(
                    f"오답입니다. 정답은 "
                    f"{quiz.answer}번입니다."
                )

        print("\n=== 퀴즈 결과 ===")
        print(f"총 문제 수: {len(self.quizzes)}")
        print(f"정답 수: {score}")
        print(f"점수: {score}/{len(self.quizzes)}")

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            self.save_state()
            print("새로운 최고 점수입니다!")

    def add_quiz(self):
        """새로운 퀴즈를 추가하고 저장합니다."""
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

            self.save_state()

            print("퀴즈가 추가되고 저장되었습니다.")

        except (KeyboardInterrupt, EOFError):
            print("\n퀴즈 추가를 취소합니다.")

    def list_quizzes(self):
        """등록된 모든 퀴즈를 출력합니다."""
        print("\n=== 퀴즈 목록 ===")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n{number}. {quiz.question}")

            for index, choice in enumerate(
                quiz.choices,
                start=1,
            ):
                print(f"   {index}) {choice}")

        print(
            f"\n총 {len(self.quizzes)}개의 "
            "퀴즈가 등록되어 있습니다."
        )

    def show_best_score(self):
        """현재 저장된 최고 점수를 출력합니다."""
        print("\n=== 최고 점수 ===")

        if self.best_score is None:
            print("아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"최고 정답 수: {self.best_score}개")

        def show_menu(self):
         """메인 메뉴를 화면에 출력합니다."""
        print("\n================================")
        print("     Python & Git 퀴즈 게임")
        print("================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("================================")

    def run(self):
        """퀴즈 게임의 메인 메뉴를 실행합니다."""
        try:
            while True:
                self.show_menu()

                choice = input(
                    "메뉴 번호를 선택하세요: "
                ).strip()

                if choice == "":
                    print(
                        "입력값이 없습니다. "
                        "1~5 중에서 선택하세요."
                    )
                    continue

                if choice == "1":
                    self.play_quiz()

                elif choice == "2":
                    self.add_quiz()

                elif choice == "3":
                    self.list_quizzes()

                elif choice == "4":
                    self.show_best_score()

                elif choice == "5":
                    print("\n퀴즈 게임을 종료합니다.")
                    break

                else:
                    print(
                        "잘못된 입력입니다. "
                        "1~5 중에서 선택하세요."
                    )

        except (KeyboardInterrupt, EOFError):
            print(
                "\n입력이 중단되었습니다. "
                "안전하게 종료합니다."
            )

        finally:
            self.save_state()        