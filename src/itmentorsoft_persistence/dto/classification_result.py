class ClassificationResult:
    def __init__(
        self, user_id: str, assessment_id: str, classification: str, feedback: str
    ):
        self.user_id = user_id
        self.assessment_id = assessment_id
        self.classification = classification
        self.feedback = feedback