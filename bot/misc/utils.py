from collections.abc import Sequence

from bot.misc.logs import InterceptHandler
from bot.misc.types import HandlerType


def get_handlers_for_filtered() -> Sequence[HandlerType]:
    """Function for generating a sequence of handlers for logging."""
    handlers_obj = (InterceptHandler,)
    return [handler() for handler in handlers_obj]
