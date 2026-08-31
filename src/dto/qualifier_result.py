class QualifierResult:
    def __init__(
        self,
        id: str,
        question_id: str,
        user_id: str,
        score: int,
        feedback: str,
        key_concepts_detected: list[str],
        misconceptions_detected: list[str],
        question_topic: str,
        assessment_id: str,
        question_difficulty: str,
        answer_id: str,
    ):
        self.id = id
        self.question_id = question_id
        self.user_id = user_id
        self.score = score
        self.feedback = feedback
        self.key_concepts_detected = key_concepts_detected or []
        self.misconceptions_detected = misconceptions_detected or []
        self.question_topic = question_topic
        self.assessment_id = assessment_id
        self.question_difficulty = question_difficulty
        self.answer_id = answer_id


class TopicResult:
    def __init__(self, user_id: str, topic: str, score: int):
        self.user_id = user_id
        self.topic = topic
        self.score = score