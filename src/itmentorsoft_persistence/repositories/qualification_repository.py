from abc import ABC, abstractmethod

from itmentorsoft_persistence.dto.qualifier_result import QualifierResult, TopicResult
from itmentorsoft_persistence.dto.question import Question


class QualificationRepository(ABC):

    @abstractmethod
    async def save_assessment_qualification(self, qualifier_result: QualifierResult):
        """Save the qualification result of an assessment

        Args:
            qualifier_result (QualifierResult): The result of the qualification to be saved.
        """
        pass

    @abstractmethod
    async def save_topic_result(self, topic_result: TopicResult):
        """Save the topic result of an assessment

        Args:
            topic_result (TopicResult): The result of the topic to be saved.
        """
        pass

    @abstractmethod
    async def get_question_rubrics_bulk(
        self, question_ids: list[str]
    ) -> dict[str, Question]:
        """Obtain rubrics for multiple questions in a single query.

        Args:
            question_ids (list[str]): The IDs of the questions to retrieve rubrics for.

        Returns:
            dict[str, Question]: A dictionary mapping question_id to Question objects with rubric data.
                Missing question IDs are omitted from the result.
        """
        pass

    @abstractmethod
    async def is_already_qualified(self, assessment_id: str) -> bool:
        """Check if an assessment has already been qualified.

        Args:
            assessment_id (str): The ID of the assessment to check.

        Returns:
            bool: True if the assessment has already been qualified, False otherwise.
        """
        pass
