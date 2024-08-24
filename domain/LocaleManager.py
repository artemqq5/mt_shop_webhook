from typing import Any

from aiogram_i18n.managers import BaseManager


class LocaleManager(BaseManager):

    async def set_locale(self, *args: Any, **kwargs: Any) -> None:
        pass

    async def get_locale(self, *args: Any, **kwargs: Any) -> str:
        return "en"
