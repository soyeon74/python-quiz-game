# Python & Git 퀴즈 게임

Python과 Git의 기초 내용을 학습할 수 있는 **터미널 기반 퀴즈 게임**입니다.  
Python의 클래스, 함수, 조건문, 반복문, 예외 처리, JSON 파일 저장 기능을 활용하고, Git으로 기능별 개발 이력과 브랜치 병합 과정을 관리했습니다.

## 1. 프로젝트 개요

사용자가 터미널 메뉴에서 퀴즈 풀기, 퀴즈 추가, 퀴즈 목록 조회, 최고 점수 확인, 종료를 선택할 수 있습니다.

- 기본 퀴즈: Python & Git 기초 5문제
- 각 문제: 선택지 4개, 정답 번호 1~4
- 사용자 추가 퀴즈 영구 저장
- 최고 점수 영구 저장
- 잘못된 입력 및 중단 입력 예외 처리
- 손상되거나 없는 저장 파일 복구
- 보너스: 랜덤 출제, 문제 수 선택, 힌트, 퀴즈 삭제, 점수 기록

## 2. 퀴즈 주제와 선정 이유

**주제: Python & Git 기초**

이번 과제에서 실제로 사용하는 Python과 Git의 핵심 개념을 퀴즈로 다시 학습할 수 있도록 선정했습니다.

## 3. 주요 기능

1. **퀴즈 풀기** — 등록된 문제를 풀고 즉시 정답 여부와 최종 점수를 확인합니다.
2. **퀴즈 추가** — 문제, 선택지 4개, 정답 번호를 입력하여 새 퀴즈를 저장합니다.
3. **퀴즈 목록** — 현재 등록된 문제와 선택지를 확인합니다.
4. **점수 확인** — 저장된 최고 정답 수를 확인합니다.
5. **보너스 기능** — 문제 순서 랜덤, 출제 문제 수 선택, `h` 힌트, 퀴즈 삭제, 점수 기록 조회를 지원합니다.
6. **입력 검증** — 빈 값, 숫자가 아닌 값, 범위를 벗어난 값, 잘못된 메뉴 번호를 처리합니다.
7. **안전한 종료** — `KeyboardInterrupt`, `EOFError` 발생 시 가능한 범위에서 데이터를 저장하고 종료합니다.
8. **저장 파일 복구** — `state.json`이 없으면 기본 퀴즈를 생성하고, JSON 손상/읽기 오류가 발생하면 기본 데이터로 복구합니다.

## 4. 실행 환경

- Python 3.10 이상
- 개발 및 검증 환경: Python 3.12.10
- Python 표준 라이브러리만 사용
- Git
- Windows PowerShell / VS Code

## 5. 실행 방법

```powershell
git clone https://github.com/soyeon74/python-quiz-game.git
cd python-quiz-game
python main.py
```

실행 메뉴:

```text
================================
     Python & Git 퀴즈 게임
================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
6. 퀴즈 삭제 (보너스)
7. 점수 기록 (보너스)
================================
```

## 6. 파일 구조

```text
python-quiz-game/
├─ main.py
├─ quiz.py
├─ quiz_data.py
├─ quiz_game.py
├─ state.json
├─ README.md
└─ .gitignore
```

- `main.py`: 프로그램 시작점
- `quiz.py`: `Quiz` 클래스
- `quiz_data.py`: 기본 퀴즈 5문제
- `quiz_game.py`: `QuizGame` 클래스 및 메뉴/게임/저장 기능
- `state.json`: 퀴즈와 최고 점수 저장
- `README.md`: 프로젝트 설명 및 제출 증빙

## 7. 클래스 구조

### Quiz

주요 속성:
- `question`: 문제
- `choices`: 4개의 선택지
- `answer`: 정답 번호(1~4)

주요 메서드:
- `display()`
- `check_answer()`
- `to_dict()`
- `from_dict()`

### QuizGame

주요 역할:
- 상태 불러오기/저장
- 메뉴 실행
- 퀴즈 풀기
- 퀴즈 추가
- 퀴즈 목록
- 최고 점수 확인
- 입력값 검증

## 8. state.json 저장 구조

위치: **프로젝트 루트의 `state.json`**

역할:
- 기본 및 사용자 추가 퀴즈 저장
- 최고 점수 저장
- 퀴즈별 힌트 및 점수 기록 저장
- 프로그램 재실행 후 데이터 유지

예시 구조:

```json
{
  "quizzes": [
    {
      "question": "Python에서 화면에 내용을 출력할 때 사용하는 함수는?",
      "choices": ["input()", "print()", "len()", "type()"],
      "answer": 2
    }
  ],
  "best_score": 5,
  "score_history": [
    {"score": 5, "total": 5}
  ]
}
```

## 9. 최종 실행 검증 결과

최종 실행에서 기본 퀴즈 5문제를 모두 풀어 다음 결과를 확인했습니다.

```text
=== 퀴즈 결과 ===
총 문제 수: 5
정답 수: 5
점수: 5/5
새로운 최고 점수입니다!

=== 최고 점수 ===
최고 정답 수: 5개
```

프로그램 메뉴의 **5. 종료**를 선택하여 정상 종료되는 것도 확인했습니다.

## 10. 예외 및 데이터 저장 검증

다음 항목을 실제 실행으로 확인했습니다.

- `state.json`이 없을 때 기본 퀴즈 5문제 생성
- 추가한 퀴즈가 재실행 후 유지
- 최고 점수가 재실행 후 유지
- 손상된 JSON 파일에서 기본 퀴즈로 복구
- 빈 입력, 숫자가 아닌 입력, 범위 밖 입력 재입력 처리
- Ctrl+C / EOF 입력 중단 처리

## 11. Git / GitHub 수행 내역

과제에서 요구한 Git 명령과 버전 관리 과정을 수행했습니다.

- `git init`
- `git add`
- `git commit`
- `git checkout`
- `git push`
- `git clone`
- `git pull`
- 기능 브랜치 `feature/quiz-play` 생성
- 기능 브랜치 개발 후 `main`에 merge
- 별도 폴더에 저장소 clone
- clone된 저장소에서 README 수정 → commit → push
- 원본 저장소에서 `git pull origin main` 실행 및 Fast-forward 동기화 확인
- 과제 기준 10개 이상의 의미 있는 커밋 작성

대표 Git 이력:

```text
bd6b7c3 Docs: clone 환경에서 README 수정
1e9ce89 Docs: 프로젝트 실행 방법 및 데이터 구조 문서화
c1b7c4a Fix: QuizGame 메뉴 실행 구조 오류 수정
f08f671 Refactor: QuizGame 중심으로 메뉴 실행 구조 정리
9c0c21a Feat: state.json 데이터 저장 및 최고 점수 유지 구현
342dc9b Feat: 퀴즈 추가 및 목록 조회 기능 구현
90e288c Feat: 사용자 퀴즈 추가 기능 구현
f773e6d Merge: 퀴즈 플레이 기능 브랜치 병합
985dac0 Feat: 퀴즈 출제 및 점수 계산 기능 구현
3bdf3af Feat: Python과 Git 기본 퀴즈 5문제 추가
65ddda1 Feat: Quiz 클래스 및 정답 확인 기능 구현
42e30e3 Feat: 퀴즈 게임 메뉴 및 입력 예외 처리 구현
12a6353 Chore: 프로젝트 초기 구조 설정
```

## 12. 제출 요구사항 체크

| 요구사항 | 결과 |
|---|---|
| Python 3.10+ | ✅ Python 3.12.10 |
| 표준 라이브러리 사용 | ✅ |
| 메뉴 5종 | ✅ |
| 기본 퀴즈 5문제 이상 | ✅ |
| Quiz / QuizGame 2개 이상 클래스 | ✅ |
| 문제·선택지4·정답1~4 구조 | ✅ |
| 입력값 검증 | ✅ |
| Ctrl+C / EOF 처리 | ✅ |
| state.json 영구 저장 | ✅ |
| 저장 파일 미존재/손상 복구 | ✅ |
| README 작성 | ✅ |
| 의미 있는 커밋 10개 이상 | ✅ |
| 별도 브랜치 생성 | ✅ |
| 브랜치 merge 기록 | ✅ |
| push | ✅ |
| clone | ✅ |
| pull | ✅ |
| GitHub 저장소 공개 | ✅ |

## 13. 제출 증빙

### 프로그램 실행 증빙

최종 테스트 결과:
- 퀴즈 풀기 정상 동작
- 5문제 중 5문제 정답
- 최종 점수 `5/5`
- 최고 정답 수 `5개`
- 정상 종료 확인

### Git 증빙

`git log --oneline --graph --decorate --all`에서 다음을 확인할 수 있습니다.
- `main` 브랜치
- `feature/quiz-play` 브랜치
- merge 이력
- 10개 이상의 의미 있는 커밋
- 원격 브랜치 `origin/main`, `origin/feature/quiz-play`

### Clone / Pull 증빙

별도 디렉터리 `python-quiz-game-clone`에 저장소를 clone한 뒤 README를 수정하여 push했고, 원본 프로젝트에서 `git pull origin main`을 실행해 Fast-forward 동기화를 확인했습니다.

## 14. 제출 링크

GitHub Repository: https://github.com/soyeon74/python-quiz-game

## 15. 보너스 과제 구현

다음 선택 기능을 추가 구현했습니다.

- **문제 순서 랜덤**: `random.sample()`로 매 실행마다 문제 순서를 무작위로 구성합니다.
- **출제 문제 수 선택**: 등록된 문제 수 범위 안에서 원하는 출제 수를 선택합니다.
- **힌트 기능**: 문제 풀이 중 `h`를 입력하면 힌트를 확인할 수 있습니다.
- **퀴즈 삭제**: 메뉴 6에서 등록된 퀴즈 번호를 선택해 삭제하고 즉시 저장합니다.
- **점수 기록**: 매 완료 게임의 `score/total`을 `state.json`에 누적하고 메뉴 7에서 조회합니다.

기존 `state.json`에 `hint` 또는 `score_history`가 없어도 기본값을 사용하도록 하위 호환 처리했습니다.
