from quiz import Quiz


def get_default_quizzes():
    return [
        Quiz(
            "Python에서 화면에 내용을 출력할 때 사용하는 함수는?",
            ["input()", "print()", "len()", "type()"],
            2,
            "화면에 결과를 보여 주는 출력 함수를 떠올려 보세요.",
        ),
        Quiz(
            "Python에서 사용자에게 값을 입력받을 때 사용하는 함수는?",
            ["print()", "input()", "open()", "range()"],
            2,
            "키보드로 값을 받아오는 입력 함수를 떠올려 보세요.",
        ),
        Quiz(
            "여러 값을 순서대로 저장할 수 있는 Python 자료형은?",
            ["list", "bool", "int", "str"],
            1,
            "대괄호 []로 여러 값을 저장하는 자료형입니다.",
        ),
        Quiz(
            "Git에서 변경된 파일을 스테이징 영역에 추가하는 명령어는?",
            ["git push", "git add", "git clone", "git pull"],
            2,
            "commit 전에 변경 파일을 준비하는 명령어입니다.",
        ),
        Quiz(
            "Git에서 변경 이력을 하나의 기록으로 저장하는 명령어는?",
            ["git commit", "git checkout", "git status", "git branch"],
            1,
            "스테이징한 변경 내용을 하나의 버전 기록으로 남깁니다.",
        ),
    ]
