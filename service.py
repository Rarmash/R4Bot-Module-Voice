from r4bot_sdk import register_hook_provider, unregister_hook_provider
MODULE_ID = "voice"
LEADERBOARD_PROVIDERS_HOOK = "leaderboards.providers"


class VoiceService:
    def __init__(self, module):
        self.module = module

    def register_hooks(self):
        register_hook_provider(
            self.module.bot,
            LEADERBOARD_PROVIDERS_HOOK,
            MODULE_ID,
            {
                "name": "voice",
                "description": "Посмотреть таблицу лидеров по голосовой активности",
                "callback": self.module.show_voice_leaderboard,
            },
        )

    def unregister_hooks(self):
        unregister_hook_provider(self.module.bot, LEADERBOARD_PROVIDERS_HOOK, MODULE_ID)
