from .. import content_filler

def main():
    LanguageContent = content_filler.LanguageContent
    content_filler.LANG = 'english'

    eng = LanguageContent('Английский', 'english')
    eng.section('Спорт', 'sport')\
        .lesson(1)\
         .word("Мяч", "Мячи", 'Ball', 'Balls')