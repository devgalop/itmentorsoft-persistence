from itmentorsoft_persistence.dto.rate_content import (
    RateContent,
)
from itmentorsoft_persistence.models.postgresql_content_rating import (
    ContentRating,
)


class RateContentMapper:

    @staticmethod
    def to_entity(request: RateContent) -> ContentRating:
        return ContentRating(
            id=request.id,
            content_id=request.content_id,
            user_id=request.user_id,
            rating=request.rating,
            comment=request.comment,
        )

    @staticmethod
    def to_model(entity: ContentRating) -> RateContent:
        return RateContent(
            id=entity.id,
            content_id=entity.content_id,
            user_id=entity.user_id,
            rating=entity.rating,
            comment=entity.comment,
        )
