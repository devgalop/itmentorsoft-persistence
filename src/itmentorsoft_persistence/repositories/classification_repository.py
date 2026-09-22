from abc import ABC, abstractmethod

from itmentorsoft_persistence.dto.classification_result import ClassificationResult


class ClassificationRepository(ABC):

    @abstractmethod
    async def save_classification_result(
        self, classification_result: ClassificationResult
    ):
        """Save the classification result of an assessment

        Args:
            classification_result (ClassificationResult): The result of the classification to be saved.
        """
        pass

    @abstractmethod
    async def is_qualification_completed(
        self, user_id: str, assessment_id: str
    ) -> bool:
        """Check if the qualification process is completed for a user

        Args:
            user_id (str): The ID of the user to check.
            assessment_id (str): The ID of the assessment to check.

        Returns:
            bool: True if the qualification process is completed for the user and assessment, False otherwise.
        """
        pass
