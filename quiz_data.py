from quiz import Quiz


def get_default_quizzes():
    return [
        Quiz(
            "Python에서 화면에 내용을 출력할 때 사용하는 함수는?",
            ["input()", "print()", "len()", "type()"],
            2,
        ),
        Quiz(
            "Python에서 사용자에게 값을 입력받을 때 사용하는 함수는?",
            ["print()", "input()", "open()", "range()"],
            2,
        ),
        Quiz(
            "여러 값을 순서대로 저장할 수 있는 Python 자료형은?",
            ["list", "bool", "int", "str"],
            1,
        ),
        Quiz(
            "Git에서 변경된 파일을 스테이징 영역에 추가하는 명령어는?",
            ["git push", "git add", "git clone", "git pull"],
            2,
        ),
        Quiz(
            "Git에서 변경 이력을 하나의 기록으로 저장하는 명령어는?",
            ["git commit", "git checkout", "git status", "git branch"],
            1,
        ),
    ]