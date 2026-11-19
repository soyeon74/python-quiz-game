# 컴퓨터에게 명령 내리는 말(파이썬) 처음 배우기
## Python & Git 퀴즈 게임

Python 기본 문법을 실제 프로그램으로 연결하고, 클래스·JSON 파일 저장·Git 버전 관리를 직접 경험하기 위해 만든 **터미널 기반 퀴즈 게임**입니다.

> **먼저 이렇게 구분하면 이해하기 쉽습니다.**
>
> - **실행 흐름:** `main.py` → `QuizGame` → 저장 데이터 확인 → 메뉴 실행
> - **문제 구조:** `Quiz` 클래스 = 문제 하나의 설계도
> - **기본 데이터:** `quiz_data.py` = `Quiz` 설계도로 만든 기본 문제 5개 제공
> - **현재 데이터 저장:** `state.json` = 사용 중인 퀴즈·최고 점수·점수 기록 저장
>
> 즉, `Quiz → quiz_data.py`가 순서대로 실행된다는 뜻이 아닙니다. `Quiz`는 **문제 하나의 구조를 정의**하고, `quiz_data.py`는 그 구조를 이용해 **기본 문제 여러 개를 준비**합니다.

---

## 1. 프로젝트 개요

이 미션의 목표는 Python 문법을 외우는 데서 끝나지 않고, **직접 동작하는 프로그램을 처음부터 끝까지 만들어 보면서 코드가 왜 그렇게 동작하는지 설명할 수 있게 되는 것**입니다.

구현한 프로그램에서는 다음을 경험했습니다.

- Python 입력·출력, 변수, 조건문, 반복문, 함수
- `Quiz`, `QuizGame` 두 클래스를 이용한 역할 분리
- JSON을 이용한 데이터 영속성
- 잘못된 입력과 파일 오류에 대한 예외 처리
- Git의 기능 단위 commit, branch, merge, clone, pull
- GitHub 원격 저장소를 이용한 버전 관리

### 퀴즈 주제와 선정 이유

- **주제:** Python과 Git 기초
- **기본 문제:** 5문제
- **선정 이유:** 이번 미션에서 배우는 Python과 Git 개념 자체를 문제로 만들면 프로그램을 구현하면서 동시에 학습 내용을 반복할 수 있고, 정답도 명확하게 확인할 수 있기 때문입니다.

`quiz_data.py`의 기본 문제 5개는 모두 `Quiz(...)`를 이용해 실제 객체로 생성됩니다.

---

## 2. 최종 구현 결과

| 구분 | 요구사항 | 현재 결과 |
|---|---|---|
| 필수 | 메뉴 선택 | ✅ 구현 |
| 필수 | 퀴즈 풀기 | ✅ 구현 |
| 필수 | 퀴즈 추가 | ✅ 구현 |
| 필수 | 퀴즈 목록 | ✅ 구현 |
| 필수 | 최고 점수 확인 | ✅ 구현 |
| 필수 | 종료 | ✅ 구현 |
| 필수 | 기본 퀴즈 5개 이상 | ✅ 5개 |
| 필수 | 클래스 2개 이상 | ✅ `Quiz`, `QuizGame` |
| 필수 | 입력 검증 | ✅ 빈 값·문자·범위 밖 값 |
| 필수 | Ctrl+C / EOF 안전 처리 | ✅ 구현 |
| 필수 | state.json 저장·불러오기 | ✅ 구현 |
| 필수 | 파일 미존재·손상 처리 | ✅ 구현 |
| 필수 | 의미 있는 commit 10개 이상 | ✅ 30개 이상 확인 |
| 필수 | branch 및 merge | ✅ 수행 |
| 필수 | clone / pull | ✅ 수행 기록 |
| 보너스 | 랜덤 출제 | ✅ |
| 보너스 | 문제 수 선택 | ✅ |
| 보너스 | 힌트 표시 | ✅ |
| 보너스 | 퀴즈 삭제 | ✅ |
| 보너스 | 점수 기록 목록 | ✅ |
| 보너스 | 힌트 사용 시 점수 차감 | ❌ 미구현 |
| 보너스 | 점수 기록 날짜·시간 | ❌ 미구현 |

보너스의 미구현 2개 항목은 선택사항이며 필수 미션 범위와 구분했습니다.

---

## 3. 프로그램 실행 방법

### 처음 GitHub에서 내려받는 경우

```powershell
git clone https://github.com/soyeon74/python-quiz-game.git
cd python-quiz-game
python main.py
```

`python` 명령이 동작하지 않는 환경에서는 다음과 같이 실행할 수 있습니다.

```powershell
py main.py
```

개발·검증 환경은 **Windows / PowerShell / VS Code / Python 3.12.10**입니다.

---

## 4. 프로그램 파일 구조

```text
python-quiz-game/
├─ main.py
├─ quiz.py
├─ quiz_data.py
├─ quiz_game.py
├─ state.json
├─ README.md
├─ .gitignore
└─ docs/
   └─ python_class_guide.pdf
```

| 파일 | 역할 |
|---|---|
| `main.py` | 프로그램 시작 |
| `quiz.py` | 문제 하나를 표현하는 `Quiz` 클래스 |
| `quiz_data.py` | 기본 Python·Git 퀴즈 5개 |
| `quiz_game.py` | 메뉴·입력·게임·점수·저장 등 전체 진행 |
| `state.json` | 퀴즈와 점수 데이터 저장 |
| `state.json.bak` | 실행 중 만들어지는 직전 정상 저장본 백업 |
| `README.md` | 과제 수행·구조·학습 내용·평가 증빙 정리 |

`state.json.bak`은 실행 과정에서 자동 생성되는 파일이므로 `.gitignore`에 등록했습니다.

---

## 5. 프로그램이 실행되는 순서

아래 화살표는 **실제로 프로그램이 실행되는 흐름**을 나타냅니다. `Quiz`, `quiz_data.py`, `state.json`의 역할 관계를 단순히 왼쪽에서 오른쪽으로 실행되는 순서로 이해하지 않도록 구분합니다.

```text
python main.py
     ↓
main.py
     ↓
game = QuizGame()
     ↓
QuizGame.__init__()
     ↓
load_state()
     ↓
state.json 확인
     ↓
메뉴 출력
     ↓
사용자가 기능 선택
     ↓
퀴즈 풀기 / 추가 / 목록 / 점수 / 삭제
     ↓
save_state()
     ↓
state.json 저장
```

`main.py`는 프로그램을 시작하는 역할만 하고 실제 게임 기능은 `QuizGame`에 맡깁니다.

### 실행 순서와 역할 관계는 다릅니다

```text
[실제 실행의 중심]
main.py
   ↓
QuizGame
   ↓
load_state()로 저장 데이터 확인
   ↓
메뉴와 게임 실행

[문제의 구조]
Quiz 클래스
   ↓
문제 하나의 question / choices / answer / hint를 관리

[기본 문제와 저장 데이터]
quiz_data.py ── Quiz 클래스를 이용해 기본 문제 5개 제공
state.json   ── 현재 퀴즈와 점수 데이터를 저장
```

- `Quiz`는 **문제 하나가 어떤 데이터를 가져야 하는지 정한 설계도**입니다.
- `quiz_data.py`는 그 `Quiz` 설계도를 이용해 **처음 사용할 기본 문제 여러 개를 준비**합니다.
- `state.json`은 프로그램을 사용하면서 추가·변경된 **현재 상태를 기억하는 저장 파일**입니다.
- 따라서 `Quiz → quiz_data.py → state.json`을 하나의 실행 순서로 외우지 않고, **실행 흐름과 각 파일의 역할을 나누어 이해**하는 것이 정확합니다.

```python
from quiz_game import QuizGame

def main():
    game = QuizGame()
    game.run()

if __name__ == "__main__":
    main()
```

---

## 6. 클래스 설계와 역할 분리

### Quiz 클래스 — 문제 한 문제 담당

```python
class Quiz:
    def __init__(self, question, choices, answer, hint=""):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint
```

| 메서드 | 책임 |
|---|---|
| `__init__()` | 문제·선택지·정답·힌트 초기화 |
| `display()` | 문제와 보기 출력 |
| `check_answer()` | 사용자의 답과 정답 비교 |
| `to_dict()` | Quiz 객체를 저장 가능한 dict로 변환 |
| `from_dict()` | dict를 Quiz 객체로 복원 |

### QuizGame 클래스 — 게임 전체 담당

| 메서드 | 책임 |
|---|---|
| `load_state()` | 저장 데이터 불러오기 |
| `restore_backup()` | 손상 시 백업 데이터 복구 |
| `save_state()` | 현재 데이터를 JSON으로 저장 |
| `get_number_input()` | 숫자 입력 검증 |
| `get_quiz_answer()` | 정답·힌트 입력 처리 |
| `play_quiz()` | 출제·채점·점수 갱신 |
| `add_quiz()` | 새 문제 등록 |
| `list_quizzes()` | 문제 목록 출력 |
| `delete_quiz()` | 문제 삭제 |
| `show_best_score()` | 최고 점수 출력 |
| `show_score_history()` | 점수 기록 출력 |
| `show_menu()` | 메뉴 출력 |
| `run()` | 메뉴 반복 및 전체 흐름 제어 |

**왜 두 클래스로 나눴는가?**

`Quiz`는 문제 하나의 데이터와 행동만 책임지고, `QuizGame`은 여러 문제와 게임 전체 흐름을 책임집니다. 이렇게 나누면 코드의 역할이 명확해지고 같은 `Quiz` 설계도로 여러 문제를 반복해서 만들 수 있어 **추상화·재사용성·유지보수성**이 좋아집니다.

---

## 7. 클래스·객체·__init__·self

- **클래스(Class):** 객체를 만들기 위한 설계도
- **인스턴스화:** 클래스를 이용해 실제 객체를 만드는 과정
- **인스턴스:** 클래스로부터 실제 만들어진 객체
- **`__init__`:** 객체가 생성될 때 자동 실행되어 초기값을 설정하는 메서드
- **`self`:** 현재 만들어진 객체 자기 자신

예를 들어:

```python
Quiz(
    "Python에서 화면에 내용을 출력할 때 사용하는 함수는?",
    ["input()", "print()", "len()", "type()"],
    2,
)
```

`Quiz`는 설계도이고 `Quiz(...)`를 실행하는 것은 실제 문제 객체를 만드는 **인스턴스화**입니다.

> 현재 프로젝트에는 클래스와 인스턴스화가 실제 적용되어 있습니다. 상속·다형성은 추가 학습자료에서 학습했지만 현재 프로그램의 구현 기능은 아닙니다.

추가 학습자료: [파이썬 클래스·인스턴스화·상속·다형성 PDF](docs/python_class_guide.pdf)

---

## 8. Python 기본 문법을 실제 코드에서 사용한 곳

| 개념 | 의미 | 실제 사용 |
|---|---|---|
| 변수 | 값을 이름으로 저장 | `score`, `question_count`, `choice` |
| `int` | 정수 | 정답 번호, 점수 |
| `str` | 문자열 | 문제, 보기, 힌트 |
| `bool` | 참/거짓 | `check_answer()` 결과 |
| `list` | 순서 있는 여러 값 | 퀴즈 목록, 선택지 |
| `dict` | key-value 데이터 | JSON 저장 구조 |
| `if/elif/else` | 조건에 따라 분기 | 메뉴·정답 판정 |
| `for` | 정해진 항목을 반복 | 문제·선택지 출력 |
| `while` | 조건이 만족될 때까지 반복 | 메뉴·입력 재시도 |
| 함수/메서드 | 기능을 묶어 재사용 | `play_quiz()`, `save_state()` 등 |
| 매개변수 | 함수가 받을 값 | `prompt`, `min_value`, `max_value` |
| `return` | 처리 결과를 호출한 곳에 반환 | 입력값·정답 판정 |

### for와 while의 차이

```python
for number, quiz in enumerate(selected_quizzes, start=1):
```

`for`는 선택된 퀴즈처럼 **반복할 대상이 정해져 있을 때** 사용합니다.

```python
while True:
```

`while`은 사용자가 올바른 값을 언제 입력할지 모르므로 **조건이 충족될 때까지 반복해야 할 때** 사용합니다.

---

## 9. 입력 검증과 예외 처리

과제에서 요구한 빈 값, 숫자가 아닌 값, 허용 범위를 벗어난 값을 처리합니다.

```python
value = input(prompt).strip()

if value == "":
    print("빈 값은 입력할 수 없습니다.")
    continue

number = int(value)

if number < min_value or number > max_value:
    print(f"{min_value}~{max_value} 사이의 숫자를 입력하세요.")
    continue
```

숫자로 변환할 수 없는 입력은 `ValueError`로 처리합니다.

```python
except ValueError:
    print("숫자만 입력하세요.")
```

### Ctrl+C / EOF 안전 처리

```python
except (KeyboardInterrupt, EOFError):
    print("\n입력이 중단되었습니다. 안전하게 종료합니다.")
finally:
    self.save_state()
```

- Ctrl+C → `KeyboardInterrupt`
- 입력 스트림 종료 → `EOFError`
- `finally` → 가능한 범위에서 `save_state()`를 실행

따라서 예외 때문에 Traceback만 남기고 끝나는 대신 안전한 종료 흐름을 갖도록 했습니다.

> 평가에서 언급된 SIGTERM은 운영체제 수준의 추가 종료 신호입니다. 원 과제의 필수 요구사항은 Ctrl+C와 EOF 처리이므로 현재 범위에서는 구현하지 않았으며, 서버·장기 실행 프로그램으로 확장할 경우 `signal` 모듈을 검토할 수 있습니다.

---

## 10. 데이터 파일 이해하기 — quiz_data.py, state.json, state.json.bak

이 프로그램에서는 데이터와 관련된 파일의 역할을 다음처럼 구분합니다.

| 파일 | 역할 | 언제 사용하는가? |
|---|---|---|
| `quiz_data.py` | 처음 사용할 **기본 퀴즈 5개**를 준비 | `state.json`이 없어서 처음 시작할 데이터가 필요할 때 |
| `state.json` | 현재 사용 중인 **퀴즈·최고 점수·점수 기록**을 저장 | 프로그램을 종료한 뒤에도 현재 데이터를 유지할 때 |
| `state.json.bak` | 직전의 정상 `state.json`을 보관하는 **백업 파일** | `state.json`이 손상되어 읽지 못할 때 복구용으로 사용 |

### 세 파일의 관계

```text
Quiz class
   │
   └── 문제 하나의 구조를 정의
       (question / choices / answer / hint)

quiz_data.py
   │
   └── Quiz 설계도를 이용해 기본 문제 5개를 준비
                 │
                 │ state.json이 없을 때 사용
                 ↓
QuizGame ── load_state() ──→ state.json에서 현재 데이터 불러오기
         └─ save_state() ──→ state.json에 현재 데이터 저장
                                  │
                                  └─ 저장 전 기존 정상본을
                                     state.json.bak으로 백업
```

중요한 점은 `Quiz → quiz_data.py → state.json`이 순서대로 실행된다는 뜻이 아니라는 것입니다.

- `Quiz`는 **문제 하나의 구조를 정하는 class**입니다.
- `quiz_data.py`는 그 구조를 이용해 **처음 사용할 기본 문제들을 제공**합니다.
- `state.json`은 프로그램을 사용하면서 바뀐 **현재 상태를 기억**합니다.
- `state.json.bak`은 현재 저장 파일에 문제가 생겼을 때 사용할 **이전 정상 상태의 백업**입니다.

### state.json과 데이터 영속성

프로그램 실행 중 변수에 들어 있는 값은 프로그램이 종료되면 사라집니다. 그래서 새로 추가한 문제와 점수 등을 `state.json`에 저장합니다. 이렇게 프로그램을 종료한 뒤 다시 실행해도 데이터를 다시 사용할 수 있게 하는 것을 **데이터 영속성**이라고 합니다.

```text
게임 데이터 변경
   ↓
save_state()
   ↓
state.json에 저장
   ↓
프로그램 종료
   ↓
다시 실행
   ↓
load_state()
   ↓
state.json에서 이전 데이터 불러오기
```

### 프로그램이 새로 저장하는 JSON 구조

```json
{
  "quizzes": [
    {
      "question": "문제",
      "choices": ["보기1", "보기2", "보기3", "보기4"],
      "answer": 2,
      "hint": "힌트"
    }
  ],
  "best_score": 3,
  "score_history": [
    {"score": 3, "total": 5}
  ]
}
```

| 필드 | 의미 |
|---|---|
| `quizzes` | 문제·선택지·정답·힌트 목록 |
| `best_score` | 최고 정답 수 |
| `score_history` | 게임별 정답 수와 출제 수 |

UTF-8로 읽고 쓰며, 한글을 그대로 저장하기 위해 `ensure_ascii=False`를 사용합니다.

### 현재 GitHub에 커밋된 state.json 상태

현재 저장소의 `state.json`은 이전 버전에서 생성된 파일이라 **기본 퀴즈 5개와 `best_score: null`을 포함하고 있으며 `hint`, `score_history` 필드는 아직 없습니다.**

현재 코드는 `data.get("score_history", [])`, `data.get("hint", "")` 방식으로 예전 파일도 읽을 수 있게 호환 처리합니다. 프로그램이 현재 코드로 저장되면 최신 구조가 반영됩니다.

### 왜 JSON인가?

JSON은 `list`와 `dict`처럼 중첩된 구조를 표현할 수 있어 한 문제의 **문제·보기 4개·정답·힌트**를 한 묶음으로 저장하기 쉽습니다. CSV는 단순한 표에는 편리하지만 선택지처럼 목록으로 된 데이터를 표현하려면 별도 변환이 필요합니다. 이 프로젝트에서는 사람이 읽기 쉽고 Python 표준 `json` 모듈만으로 처리할 수 있는 JSON을 선택했습니다.

---

## 11. 파일이 없거나 손상된 경우

### state.json이 없는 경우

```text
state.json 없음
   ↓
quiz_data.py의 get_default_quizzes()
   ↓
기본 문제 5개 사용
   ↓
새 state.json 저장
```

즉, `quiz_data.py`는 항상 현재 데이터를 저장하는 파일이 아니라 **저장된 데이터가 없을 때 시작할 기본값을 제공하는 역할**입니다.

### state.json이 손상된 경우

평가 피드백을 반영하여 백업 복구 기능을 추가했습니다.

```text
state.json 읽기 실패
   ↓
state.json.bak 확인
   ├── 정상 백업 있음 → 백업에서 복구
   └── 백업 없음/손상 → 기본 퀴즈 5개로 복구
```

정상 `state.json`이 존재하는 상태에서 저장할 때 기존 정상본을 `state.json.bak`으로 복사한 뒤 새 내용을 저장합니다.

쓰기 권한이 없는 경우에는 다음처럼 별도로 안내합니다.

```text
저장 권한이 없습니다. state.json 파일 또는 프로젝트 폴더의 쓰기 권한을 확인하세요.
```

---

## 12. 퀴즈 풀기와 점수 계산

```text
메뉴 1번
 ↓
문제 수 선택
 ↓
random.sample()로 무작위 문제 선택
 ↓
for 반복문으로 한 문제씩 출력
 ↓
답 입력
 ↓
check_answer()
 ↓
정답이면 score += 1
 ↓
최종 결과 표시
 ↓
최고 점수 비교
 ↓
state.json 저장
```

```python
score = 0

if quiz.check_answer(answer):
    score += 1
```

현재 최고 점수는 **최고 정답 수**를 기준으로 저장합니다.

---

## 13. 보너스 기능

현재 실제 구현된 보너스 기능은 다음과 같습니다.

- `random.sample()`을 이용한 랜덤 출제
- 풀 문제 수 선택
- `h` 입력으로 힌트 보기
- 등록된 퀴즈 삭제
- 게임별 `score/total` 기록

현재 **힌트 사용 시 점수 차감**과 **점수 기록 날짜·시간**은 구현하지 않았습니다. README에서도 구현된 것으로 표시하지 않습니다.

---

## 14. Git으로 개발 과정을 기록한 방법

Git은 단순히 최종 파일을 올리는 용도가 아니라 **기능을 하나씩 만들고 변경 과정을 기록하는 도구**로 사용했습니다.

### 주요 개발 커밋

```text
12a6353  Chore: 프로젝트 초기 구조 설정
42e30e3  Feat: 퀴즈 게임 메뉴 및 입력 예외 처리 구현
65ddda1  Feat: Quiz 클래스 및 정답 확인 기능 구현
3bdf3af  Feat: Python과 Git 기본 퀴즈 5문제 추가
985dac0  Feat: 퀴즈 출제 및 점수 계산 기능 구현
f773e6d  Merge: 퀴즈 플레이 기능 브랜치 병합
90e288c  Feat: 사용자 퀴즈 추가 기능 구현
342dc9b  Feat: 퀴즈 추가 및 목록 조회 기능 구현
9c0c21a  Feat: state.json 데이터 저장 및 최고 점수 유지 구현
f08f671  Refactor: QuizGame 중심으로 메뉴 실행 구조 정리
c1b7c4a  Fix: QuizGame 메뉴 실행 구조 오류 수정
1e9ce89  Docs: 프로젝트 실행 방법 및 데이터 구조 문서화
bd6b7c3  Docs: clone 환경에서 README 수정
27fbdf4  Feat: 퀴즈 힌트 데이터 구조 추가
2146b15  Feat: 기본 퀴즈 힌트 추가
b1df29a  Feat: 보너스 퀴즈 기능 5종 구현
ca7e7e9  Fix: 기존 state.json 힌트 호환 처리
58662fe  Merge: 보너스 과제 5종 구현
4ae8cbe  Feat: state.json 백업 복구 및 권한 오류 안내 추가
ac4b77d  Chore: 실행 백업 파일 Git 추적 제외
4b6eb69  Docs: 평가 피드백 보완사항과 증빙 계획 정리
```

GitHub에서 현재 **30개 이상의 커밋이 확인**됩니다.

### 브랜치

현재 저장소에서 확인되는 브랜치는 다음과 같습니다.

```text
main
feature/quiz-play
feature/bonus-features
```

퀴즈 플레이 기능은 별도 브랜치에서 작업한 뒤 `f773e6d Merge: 퀴즈 플레이 기능 브랜치 병합` 기록을 남겼고, 보너스 기능도 별도 브랜치 작업·병합 기록이 있습니다.

### clone과 pull 실습

과제 요구에 따라 완성된 저장소를 별도 디렉터리에 `clone`하고, 복제본에서 README를 변경하여 commit/push한 뒤 기존 작업 폴더에서 `pull`로 변경 내용을 가져오는 실습을 수행했습니다.

`bd6b7c3 Docs: clone 환경에서 README 수정` 커밋이 해당 실습 과정의 Git 기록으로 남아 있습니다.

> **clone과 pull 차이**  
> `clone`은 원격 저장소 전체를 처음 내 컴퓨터에 복제하는 명령이고, `pull`은 이미 복제된 로컬 저장소에 원격의 새로운 변경사항을 가져와 반영하는 명령입니다.

---

## 15. 커밋 규칙

기능 단위로 변경 목적이 드러나도록 다음 형식을 사용합니다.

```text
타입: 변경 내용 요약
```

| 타입 | 의미 | 예 |
|---|---|---|
| `Feat` | 기능 추가 | `Feat: 퀴즈 출제 기능 구현` |
| `Fix` | 오류 수정 | `Fix: 메뉴 실행 구조 오류 수정` |
| `Refactor` | 기능 변화 없이 구조 개선 | `Refactor: QuizGame 중심으로 구조 정리` |
| `Docs` | 문서 변경 | `Docs: README 실행 방법 추가` |
| `Chore` | 설정·관리 | `Chore: 프로젝트 초기 구조 설정` |
| `Merge` | 브랜치 병합 | `Merge: 퀴즈 플레이 기능 브랜치 병합` |

한 커밋에는 가능한 한 하나의 목적을 담아 변경 이유를 추적하기 쉽게 하는 것을 원칙으로 합니다.

---

## 16. 요구사항이 변경되면 어디를 수정하는가?

요구사항이 바뀌면 한 파일만 수정하는 것이 아니라 **그 기능과 연결된 입력·처리·저장 부분까지 함께 확인해야 합니다.** 한 부분만 바꾸면 화면에는 새 기능이 보이더라도 입력 검증이나 기존 저장 데이터에서 오류가 생길 수 있기 때문입니다.

| 변경 요구 | 주요 수정 위치 | 왜 함께 수정해야 하는가? | 같이 확인할 부분 |
|---|---|---|---|
| 4지선다 → 5지선다 | `Quiz`, `add_quiz()`, `get_quiz_answer()`, `load_state()` | 문제의 선택지 구조가 바뀌므로 새 문제 입력도 5개를 받아야 하고, 정답 입력 범위도 1~5로 바뀌어야 합니다. 불러올 때 선택지 개수를 검사하는 기준도 함께 바뀌어야 합니다. | 기존 4지선다 JSON을 계속 읽을 수 있는지 확인 |
| 점수 방식 변경 | `play_quiz()`, `show_best_score()` | `play_quiz()`에서 실제 점수를 계산하고, `show_best_score()`에서 저장된 최고 점수를 표시하므로 계산 기준과 표시 기준이 서로 맞아야 합니다. | `best_score`가 정답 수인지 점수인지 저장 기준 확인 |
| 퀴즈 속성 추가 | `Quiz.__init__()`, `to_dict()`, `from_dict()` | 예를 들어 난이도 같은 속성을 추가하면 Quiz 객체가 그 값을 가져야 하고, 프로그램 종료 후에도 유지하려면 JSON에 저장하고 다시 객체로 복원할 수 있어야 합니다. | JSON 스키마와 기존 데이터의 새 속성 기본값 확인 |
| 메뉴 추가 | `show_menu()`, `run()` | `show_menu()`는 새 메뉴를 화면에 보여 주고, `run()`은 사용자의 선택에 맞는 실제 기능을 실행합니다. 메뉴 번호가 늘어나면 입력 검증 범위도 함께 바뀌어야 합니다. | 메뉴 번호 입력 허용 범위 확인 |
| 출제 방식 변경 | `play_quiz()` | 문제를 어떤 순서와 방법으로 선택할지는 퀴즈 진행 로직에서 결정하므로, 랜덤 출제를 순차 출제 등으로 바꾸려면 이 부분을 수정해야 합니다. | `random.sample()`을 계속 사용할지 확인 |
| JSON → DB | `load_state()`, `save_state()`, `restore_backup()` | 현재는 JSON 파일에서 데이터를 읽고 저장하며 백업 파일로 복구합니다. DB로 변경하면 읽기·쓰기 방법뿐 아니라 장애 발생 시 복구 방식도 달라지므로 저장 관련 기능을 함께 바꿔야 합니다. | DB에 맞는 백업·복구 방식 재설계 |

### 변경 영향을 확인하는 순서

요구가 바뀌면 다음 순서로 영향을 확인합니다.

1. **데이터 모델** — `Quiz` 객체가 어떤 데이터를 가져야 하는지 확인
2. **게임 로직** — 입력, 출제, 채점, 메뉴 등 실제 동작이 어떻게 달라지는지 확인
3. **저장 구조** — 변경된 데이터를 `state.json`에 저장하고 다시 불러올 수 있는지 확인
4. **README** — 실제 구현과 사용 방법이 바뀌었다면 문서 설명도 함께 수정

예를 들어 **4지선다를 5지선다로 변경**한다면 `Quiz`의 선택지만 바꾸는 것으로 끝나지 않습니다. 문제 추가 기능은 보기 5개를 입력받아야 하고, 정답 입력은 1~5를 허용해야 하며, 기존 `state.json`에 저장된 4지선다 문제를 어떻게 처리할지도 결정해야 합니다.

또한 **퀴즈에 난이도 속성을 추가**한다면 `Quiz.__init__()`에 속성을 추가한 뒤 `to_dict()`로 저장하고 `from_dict()`로 다시 복원할 수 있어야 합니다. 즉 객체의 구조와 JSON 저장 구조가 서로 맞아야 데이터가 정상적으로 유지됩니다.

이처럼 변경할 코드의 위치뿐 아니라 **왜 그 부분이 연결되어 있는지까지 확인해야 요구사항 변경으로 인한 오류를 줄일 수 있습니다.**

---

## 17. 퀴즈가 1,000개 이상으로 커진다면?

현재 프로그램은 학습용 소규모 프로그램이므로 JSON 전체를 읽어 리스트에 저장하고 목록도 순차적으로 출력합니다.

1,000개 이상의 대규모 데이터로 확장해야 한다면 다음을 검토할 수 있습니다.

- 목록 페이징
- 전체 JSON을 매번 저장하지 않는 방식
- 표준 라이브러리 `sqlite3`를 이용한 로컬 DB
- 문제 ID·카테고리를 이용한 검색
- `time.perf_counter()`로 처리시간 측정
- `tracemalloc`로 메모리 사용량 측정

**이 내용은 향후 확장 방안이며 현재 프로그램을 1,000문제로 성능 측정했다는 뜻은 아닙니다.**

---

## 18. 평가 피드백 반영

| 평가 지적 | 반영 내용 | 상태 |
|---|---|---|
| 메뉴 실행 증빙 부족 | 실제 실행에서 메인 메뉴 1~7번 출력 확인 | ✅ 실행 확인 |
| 입력 실패 증빙 부족 | `abc`, 범위 밖 값 `9`, 빈 입력을 실제 실행으로 확인 | ✅ 실행 확인 |
| 재실행 영속성 증빙 부족 | 새 퀴즈 추가 후 종료·재실행하여 동일한 6번째 퀴즈 유지 확인 | ✅ 실행 확인 |
| 기본 5문제 일치 설명 | `quiz_data.py` 5문제 명시 | ✅ |
| 10개 이상 커밋 증빙 | `git log --oneline --graph --decorate --all` 실제 실행으로 30개 이상 커밋 확인 | ✅ 실행 확인 |
| branch/merge 증빙 | `feature/quiz-play`, `feature/bonus-features`와 merge 커밋을 Git graph에서 확인 | ✅ 실행 확인 |
| clone/pull 증빙 | 별도 `python-quiz-game-clone` 폴더 clone 성공 및 `git status` clean 확인, 기존 작업 폴더의 `git pull origin main` 성공 확인 | ✅ 실행 확인 |
| 클래스 책임 설명 | 메서드별 책임 표 추가 | ✅ |
| 로직 분리 설명 | 입력·게임·IO 책임 구분 | ✅ |
| Ctrl+C/EOF | 실제 코드 설명 | ✅ |
| 커밋 규칙 | 타입·메시지 규칙 추가 | ✅ |
| 추상화·재사용성 | 클래스 채택 이유 추가 | ✅ |
| JSON 선택 이유 | CSV와 비교하여 설명 | ✅ |
| 권한 오류 | `PermissionError` 안내 구현 | ✅ |
| 1,000개 이상 대응 | 확장 계획 명시 | ✅ |
| 자동 백업·복구 | `state.json.bak` 실제 구현 | ✅ |
| 변경 영향도 | 수정 위치 표 추가 | ✅ |

---

## 19. 제출 증빙 체크리스트

2026-11-18 실제 로컬 실행으로 다음 항목을 확인했습니다.

- 메인 메뉴 1~7 정상 출력
- 문자 `abc`, 범위 밖 숫자 `9`, 빈 입력 처리 확인
- 새 퀴즈를 추가하여 총 6문제로 증가 확인
- 프로그램 종료 후 `python main.py`로 다시 실행하고 목록을 조회했을 때 추가한 6번째 퀴즈가 그대로 유지됨을 확인
- `git log --oneline --graph --decorate --all`에서 30개 이상의 커밋과 feature branch/merge 이력 확인
- 별도 `python-quiz-game-clone` 디렉터리로 `git clone` 성공
- clone 저장소에서 `git status` 결과 `main`, `origin/main` 최신 상태, working tree clean 확인
- 기존 작업 저장소에서 `git pull origin main` Fast-forward 성공 확인

따라서 코드 구현 여부뿐 아니라 주요 평가 항목을 실제 터미널 실행으로 재검증했습니다. 평가자가 이미지 파일 제출을 요구하는 경우 아래 권장 경로에 실제 캡처본을 추가할 수 있습니다.

권장 경로:

```text
docs/screenshots/
├─ environment.png
├─ menu.png
├─ input-error.png
├─ add_quiz.png
├─ persistence.png
├─ list.png
├─ play.png
├─ score.png
├─ git-log.png
└─ clone-pull.png
```

### Git 이력 캡처 명령

```powershell
git log --oneline --graph --decorate --all
```

이 화면은 **10개 이상 커밋 + branch + merge** 증빙에 사용할 수 있습니다.

> 위 항목은 실제 터미널 실행으로 확인한 사실을 기록한 것입니다. 이미지 파일 자체가 저장소에 업로드되지 않은 경우에는 README에서 이미지가 업로드되었다고 표시하지 않습니다.

---

## 20. 평가 때 설명할 핵심 질문

**Q. 프로그램 전체 구조는?**  
> `main.py`가 시작하고 `QuizGame`이 게임 전체를 관리합니다. 문제 하나는 `Quiz` 객체로 관리하고 기본 문제는 `quiz_data.py`, 저장 데이터는 `state.json`에서 관리합니다.

**Q. 클래스란?**  
> 객체를 만들기 위한 설계도입니다. 이 프로젝트에서는 `Quiz`와 `QuizGame` 두 클래스로 문제와 게임 전체의 책임을 나눴습니다.

**Q. __init__과 self는?**  
> `__init__`은 객체 생성 시 초기값을 설정하고, `self`는 현재 객체 자기 자신을 가리킵니다.

**Q. JSON은 왜 사용했나?**  
> 프로그램을 종료해도 퀴즈와 점수를 유지하고, 문제·보기·정답처럼 구조화된 데이터를 저장하기 위해 사용했습니다.

**Q. state.json이 손상되면?**  
> 백업 파일을 먼저 확인해 복구하고, 사용할 수 있는 백업도 없으면 기본 퀴즈 5개로 복구합니다.

**Q. Ctrl+C를 누르면?**  
> `KeyboardInterrupt`를 `except`에서 처리하고, `finally`에서 `save_state()`를 실행해 가능한 범위에서 저장 후 종료합니다.

**Q. Git과 GitHub 차이는?**  
> Git은 변경 이력을 관리하는 버전관리 도구이고 GitHub는 Git 저장소를 온라인에 보관·공유하는 서비스입니다.

**Q. clone과 pull 차이는?**  
> clone은 저장소 전체를 처음 복제하는 것이고 pull은 이미 있는 로컬 저장소에 원격 변경사항을 가져오는 것입니다.

---

## 21. 최종 제출 체크

| 제출 요구사항 | 상태 |
|---|---|
| GitHub 저장소 | ✅ |
| Python 3.10 이상 | ✅ Python 3.12.10 사용 |
| 외부 라이브러리 없이 표준 라이브러리 사용 | ✅ |
| 기본 메뉴 기능 | ✅ |
| 기본 퀴즈 5개 이상 | ✅ |
| 최소 2개 클래스 | ✅ |
| 기능별 메서드 분리 | ✅ |
| state.json UTF-8 저장 | ✅ |
| 파일 미존재·손상 예외 처리 | ✅ |
| Ctrl+C / EOF 처리 | ✅ |
| 10개 이상 의미 있는 커밋 | ✅ |
| branch / merge | ✅ |
| clone / pull 수행 | ✅ |
| README 필수 항목 | ✅ |
| 프로그램 실행 검증 | ✅ 메뉴·입력검증·퀴즈 추가·재실행 영속성 실제 확인 |
| git graph 검증 | ✅ 실제 터미널에서 커밋·branch·merge 확인 |
| clone/pull 검증 | ✅ 실제 clone·status·pull 성공 확인 |

---

## 22. GitHub 저장소

GitHub Repository: https://github.com/soyeon74/python-quiz-game

---

## 마지막 정리

이 프로젝트는 **실행 흐름**과 **문제·데이터의 역할**을 나누어 이해하면 쉽습니다.

```text
[실행 흐름]
main.py
   ↓
QuizGame
   ↓
저장 데이터 확인
   ↓
메뉴와 게임 실행

[문제 구조]
Quiz class
   └── 문제 하나의 구조를 정의

[데이터 역할]
quiz_data.py
   └── 처음 사용할 기본 문제 5개 제공

state.json
   └── 현재 퀴즈와 점수 데이터 저장

state.json.bak
   └── 직전 정상 저장본 백업
```

따라서 `Quiz → quiz_data.py → state.json`을 하나의 실행 순서로 외우는 것이 아니라, **`main.py`가 시작하고 `QuizGame`이 전체 실행을 관리하며, `Quiz`는 문제의 구조를 정의하고, `quiz_data.py`와 `state.json`은 서로 다른 목적의 데이터를 담당한다**고 이해하는 것이 정확합니다.

프로그램을 만드는 과정에서 Python 문법만 사용한 것이 아니라, **class로 역할을 나누고, JSON으로 데이터를 유지하고, 예외를 처리하고, Git으로 개발 과정을 기록하는 전체 흐름**을 경험했습니다.
