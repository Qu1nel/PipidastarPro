from aiogram import Dispatcher, F, Router

import bot.keyboards as kb
from bot.callbacks.paginators import pagination_handler

callbacks_router = Router(name="callbacks_router")


callbacks_router.callback_query.register(
    pagination_handler,
    kb.fabrics.Pagination.filter(F.action.in_(["prev", "next"])),
)


def register_all_callbacks(dp: Dispatcher) -> None:
    dp.include_router(callbacks_router)
