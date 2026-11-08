from quiz import Quiz
from quiz_data import get_default_quizzes
from quiz_game import QuizGame


def show_menu():
    print("\n================================")
    print("     Python & Git 퀴즈 게임")
    print("================================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("================================")


def main():
    game = QuizGame()

    while True:
        show_menu()

        try:
            choice = input("메뉴 번호를 선택하세요: ").strip()

            if choice == "":
                print("입력값이 없습니다. 1~5 중에서 선택하세요.")
                continue

            if choice == "1":
                game.play_quiz()

            elif choice == "2":
                print("퀴즈 추가 기능을 준비 중입니다.")

            elif choice == "3":
                print("퀴즈 목록 기능을 준비 중입니다.")

            elif choice == "4":
                print("점수 확인 기능을 준비 중입니다.")

            elif choice == "5":
                print("퀴즈 게임을 종료합니다.")
                break

            else:
                print("잘못된 입력입니다. 1~5 중에서 선택하세요.")

        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되었습니다. 안전하게 종료합니다.")
            break


if __name__ == "__main__":
    main()