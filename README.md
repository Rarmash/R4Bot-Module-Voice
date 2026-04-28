# R4Bot-Module-Voice

Внешний модуль учёта голосовой активности для [R4Bot](https://github.com/Rarmash/R4Bot).

## Что делает
- отслеживает активное время участников в голосовых каналах
- учитывает время только если у участника не выключены микрофон и звук
- периодически сохраняет голосовую активность в Firebase
- если установлен модуль `leaderboards`, добавляет вкладку `/leaderboard voice`
- использует runtime services из `bot.r4_services`
- не требует отдельного модульного конфига

## Требования
- R4Bot `>= 2.0`
- runtime context с `bot.r4_services`
- сервис `firebase`

## Интеграции
- модуль может зарегистрировать leaderboard-provider
- если `leaderboards` не установлен, это не считается ошибкой и модуль продолжает учитывать голосовую активность

## Структура
- `module.json` — метаданные модуля
- `cog.py` — учёт голосовой активности и listeners
- `service.py` — регистрация вкладки для модуля лидербордов
- `requirements.txt` — зависимости для IDE и локальной проверки

## Установка в R4Bot
```powershell
python manage_modules.py install github:Rarmash/R4Bot-Module-Voice@master --enable
```

## Разработка
Для нормальной подсветки импортов в IDE и локальной проверки модуля рекомендуется установить зависимости:

```powershell
python -m pip install -r requirements.txt
```
