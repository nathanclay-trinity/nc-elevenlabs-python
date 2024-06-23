# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import pydantic_v1
from ..core.unchecked_base_model import UncheckedBaseModel
from .chapter_response import ChapterResponse
from .project_state import ProjectState


class ProjectExtendedResponseModel(UncheckedBaseModel):
    project_id: str
    name: str
    create_date_unix: int
    default_title_voice_id: str
    default_paragraph_voice_id: str
    default_model_id: str
    last_conversion_date_unix: int
    can_be_downloaded: bool
    state: ProjectState
    chapters: typing.List[ChapterResponse]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
