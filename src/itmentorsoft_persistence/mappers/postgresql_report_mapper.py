from itmentorsoft_persistence.dto.student_report import (
    StudentBasicSummary,
    StudentKnowledgeProfile,
)
from itmentorsoft_persistence.models.postgresql_assessment_model import (
    ClassificationResultEntity,
    TopicResultEntity,
)


class PostgresReportMapper:
    @staticmethod
    def from_classification_result_to_student_basic_summary(
        request: ClassificationResultEntity,
    ) -> StudentBasicSummary:
        return StudentBasicSummary(
            student_id=request.user_id,
            student_name=request.user.name if request.user else "Unknown",
            knowledge_classification=request.classification,
        )

    @staticmethod
    def to_knowledge_profile(entity: TopicResultEntity) -> StudentKnowledgeProfile:
        return StudentKnowledgeProfile(
            topic=entity.topic,
            score=entity.score,
        )
