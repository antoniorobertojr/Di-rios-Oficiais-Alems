import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "diários_oficiais_alems.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import diários_oficiais_alems.users.signals  # noqa: F401
