class LanguageMixin:
    def __init__(self):
        self._language = 'EN'  # Язык по умолчанию

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        elif self._language == 'RU':
            self._language = 'EN'