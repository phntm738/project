from .. import content_filler

def main():
    LanguageContent = content_filler.LanguageContent
    content_filler.LANG = 'french'

    fre = LanguageContent('Французский', 'french')
    fre.section('Еда', 'food')\
        .lesson(1)\
            .word('завтрак', 'завтраки', 'le petit déjeuner', 'les petits déjeuners')\
            .word('хлеб', 'хлеба', 'le pain', 'les pains')\
            .word('сыр', 'сыры', 'le fromage', 'les fromages')\
            .word('яйцо', 'яйца', "l'œuf (m)", 'les œufs')\
            .word('чай', 'чаи', 'le thé', 'les thés')\
            .phrase('Я ем хлеб и {}.', 'сыр', 'Je mange du pain et du {}.', 'fromage')\
            .phrase('Я пью {} с сахаром.', 'чай', 'Je bois du {} avec du sucre.', 'thé')\
        .end()\
        .lesson(2)\
            .word('фрукт', 'фрукты', 'le fruit', 'les fruits')\
            .word('яблоко', 'яблоки', 'la pomme', 'les pommes')\
            .word('банан', 'бананы', 'la banane', 'les bananes')\
            .word('апельсин', 'апельсины', "l'orange (m)", 'les oranges')\
            .word('ананас', 'анансаы', "l'ananas (m)", 'les ananas')\
            .phrase('Мой любимый фрукт - {}.', 'яблоко', 'Mon fruit préféré est {}.', 'pomme')\
            .phrase('Мой брат не любит {}.', 'апельсины', "Mon frère n'aime pas {}.", 'les oranges')\
        .end()\
    .end()\
    .section('Семья', 'family')\
        .lesson(1)\
            .word('семья', 'семьи', 'la famille', 'les familles')\
            .word('мать', 'матери', 'la mère', 'les mères')\
            .word('отец', 'отцы', 'le père', 'les pères')\
            .word('сестра', 'сёстры', 'la sœur', 'les sœurs')\
            .word('брат', 'братья', 'le frère', 'les frères')\
            .phrase('Моя {} живёт в Париже.', 'сестра', 'Ma {} habite à Paris.', 'sœur')\
            .phrase('Моя {} работает в Москве.', 'мать', 'Ma {} travaille à Moscou.', 'mère')\
        .end()\
    .end()\
    #.section('Время', 'time')\
    #    .lesson(1)\
    #        .word('неделя', 'недели', 'la semaine', 'les semaines')\
    #        .word('понедельник', '', 'lundi', '')\
    #        .word('вторник', '', 'mardi', '')\
    #        .word('среда', '', 'mercredi', '')\
    #        .word('четверг', '', 'jeudi', '')\
    #        .word('пятница', '', 'vendredi', '')\
    #        .word('суббота', '', 'samedi', '')\
    #        .word('воскресенье', '', 'dimanche', '')\
    #        .phrase('В {} я еду в Москву.', 'субботу', '{} je vais à Moscou.', 'Samedi')\
    #        .phrase('На следующей {} у меня два экзамена.', 'неделе', "J'ai deux exames la {} prochaine.", 'semaine')\
    #    .end()\
    #.end()\
    #.section('Цвета', 'colours')\
    #    .lesson(1)\
    #        .word('белый', '', 'blanc/blanche', '')\
    #        .word('чёрный', '', 'noir/noire', '')\
    #        .word('красный', '', 'rouge', '')\
    #        .word('оранжевый', '', 'orange', '')\
    #        .word('жёлтый', '', 'jaune', '')\
    #        .word('зелёный', '', 'vert/verte', '')\
    #        .phrase('Дани надевает {} пиджак.', 'зелёный', 'Dany met sa veste {}.', 'verte')\
    #        .phrase("Это кабаре называется '{} Мельница'.", 'Красная', "Ce cabaret s'appelle 'Moulin {}'.", 'Rouge')\
    #        .phrase('В вазе стоит {} цветок.', 'жёлтый', 'Il y a une fleur {} dans le vase.', 'jaune')\
    #    .end()\
    #    .lesson(2)\
    #        .word('синий', '', 'bleu/bleue', '')\
    #        .word('фиолетовый', '', 'violet/violette', '')\
    #        .word('розовый', '', 'rose', '')\
    #        .word('коричневый', '', 'brun/brune', '')\
    #        .word('серый', '', 'gris/grise', '')\
    #        .word('бежевый', '', 'beige', '')\
    #        .phrase('У моря красивый {} цвет.', 'синий', 'La mer a la belle couleur {}.', 'bleue')\
    #        .phrase('У Клер {} волосы и серые глаза.', 'коричневые', 'Cleire a les cheveux {} et les yeux gris.', 'bruns')\
    #        .phrase('У Клер коричневые волосы и {} глаза.', 'серые', 'Cleire a les cheveux bruns et les yeux {}.', 'gris')\
    #    .end()\
