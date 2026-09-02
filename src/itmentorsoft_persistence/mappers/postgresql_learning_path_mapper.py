from itmentorsoft_persistence.dto.learning_path import (
    LearningPath,
)
import uuid
from itmentorsoft_persistence.models.postgresql_learning_path_model import (
    LearningPathContentEntity,
    LearningPathEntity,
)


class PostgresLearningPathMapper:

    @staticmethod
    def to_learning_path_entity(model: LearningPath) -> LearningPathEntity:
        learning_path_entity = LearningPathEntity(
            id=model.path_id,
            user_id=model.user_id,
            topic=model.topic,
            is_completed=model.is_completed,
        )
        return learning_path_entity

    @staticmethod
    def to_learning_path_contents(
        model: LearningPath,
    ) -> list[LearningPathContentEntity]:
        return [
            LearningPathContentEntity(
                id=uuid.uuid4().hex,
                learning_path_id=model.path_id,
                content_id=content.content_id,
                is_completed=False,
            )
            for content in model.contents
        ]
