class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        """퀴즈 문제와 선택지를 화면에 출력합니다."""
        print(f"\n문제: {self.question}")

        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def check_answer(self, user_answer):
        """사용자가 입력한 답이 정답인지 확인합니다."""
        return user_answer == self.answer

    def to_dict(self):
        """Quiz 객체를 JSON 저장이 가능한 dict 형태로 변환합니다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data):
        """dict 데이터를 Quiz 객체로 변환합니다."""
        return cls(
            data["question"],
            data["choices"],
            data["answer"],
        )