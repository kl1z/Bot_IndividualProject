bot_messages: dict = {
    "unknown_command": "Прости, я не знаю такой команды",
    "simple_error": "Что-то пошло не так...",
    "photo_classification_error": "Извини, с обработкой фотографии что-то пошло не так.",
}

PHOTO_FOR_MODEL_MESSAGE: str = """
Пришли мне фотографию, которую хочешь распознать:

<b>Примечание:</b> модель может различать 1000 классов живых существ и предметов.
<b>Важно:</b> много лишних деталей, неправильное расположение объекта в кадре, сильные искажения могут
сильно повлиять на ответ модели.
"""

MODEL_MESSAGE: str = "Модель думает, что это: <b>{}</b>"

WELCOME_MESSAGE: str = """
Привет, <b><a href='tg://user?id={}'>{}</a></b>!
Меня зовут - Rubin!
"""

ABOUT_MESSAGE: str = """
This Bot was created by <b>kl1z</b>
GitHub: https://github.com/kl1z
"""
