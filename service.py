LEADERBOARD_PROVIDERS_HOOK = "leaderboards.providers"


class VoiceService:
    def __init__(self, module):
        self.module = module

    def register_hooks(self):
        self.module.register_hook_provider(
            LEADERBOARD_PROVIDERS_HOOK,
            {
                "name": "voice",
                "description": "Посмотреть таблицу лидеров по голосовой активности",
                "callback": self.module.show_voice_leaderboard,
            },
        )

    def unregister_hooks(self):
        self.module.unregister_hook_provider(LEADERBOARD_PROVIDERS_HOOK)
