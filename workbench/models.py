from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class StrictBaseModel(BaseModel):
    """Base for all Pydantic models in this repo.

    Enforces strict type validation, forbids extra fields, and disallows arbitrary types.
    """

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        arbitrary_types_allowed=False,
    )


__all__ = ["StrictBaseModel"]
