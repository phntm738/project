from .. import content_filler

def main():
    LanguageContent = content_filler.LanguageContent
    content_filler.LANG = 'english'

    eng = LanguageContent('Английский', 'english')
    eng.section('Еда', 'food')\
        .lesson(1)\
            .word('завтрак', 'завтраки', 'breakfast', 'breakfasts')\
            .word('хлеб', 'хлеба', 'bread', 'bread')\
            .word('сыр', 'сыры', 'cheese', 'cheese')\
            .word('сливочное масло', 'сливочное масло', 'butter', 'butter')\
            .word('йогурт', 'йогурты', 'yoghurt', 'yoghurt')\
            .phrase('Я ем на завтрак тост и {}.', 'сыр', 'I eat a toast and {} for breakfast.', 'cheese')\
            .phrase('Мой брат любит персиковый {}.', 'йогурт', 'My brother likes peach {}.', 'yoghurt')\
            .phrase('{} - важный приём пищи.', 'Завтрак', '{} is an important meal.', 'Breakfast')\
            .end()\
        .lesson(2)\
            .word('чай', 'чаи', 'tea', 'tea')\
            .word('кофе', 'кофе', 'coffee', 'coffee')\
            .word('молоко', 'молоко', 'milk', 'milk')\
            .word('хлопья', 'хлопья', 'cereals', 'cereals')\
            .word('сахар', 'сахар', 'sugar', 'sugar')\
            .phrase('Я не пью {} с молоком.', 'чай', 'I don\'t drink {} with milk.', 'tea')\
            .phrase('Ты ешь {} на завтрак?', 'хлопья', 'Do you have {} for breakfast?', 'cereals')\
        .end()\
        .lesson(3)\
            .word('обед', 'обеды', 'supper', 'suppers')\
            .word('ужин','ужины', 'dinner', 'dinners')\
            .word('салат', 'салаты', 'salad', 'salads')\
            .word('сок', 'соки', 'juice', 'juices')\
            .word('стейк', 'стейки', 'steak', 'steaks')\
            .phrase('Меня пригласили на {} к Роббинсонам.', 'ужин', 'I\'ve been invited for a {} with Robbinsons', 'dinner')\
            .phrase('Я не очень люблю {}, но мне нравятся стейки.', 'салаты', 'I\'m not fond of {}, but I like steaks.', 'salads')\
            .phrase('Вы бы хотели немного {}?', 'сока', 'Would you like some {}?', 'juice')\
        .end()\
        .lesson(4)\
            .word('фрукт', 'фрукты', 'fruit', 'fruit')\
            .word('яблоко', 'яблоки', 'apple', 'apples')\
            .word('апельсин', 'апельсины', 'orange', 'oranges')\
            .word('груша', 'груши', 'pear', 'pears')\
            .word('лимон', 'лимоны', 'lemon', 'lemons')\
            .phrase('Какой твой любимый {}?', 'фрукт', 'What is your favourite {}?', 'fruit')\
            .phrase('Это {} очень кислое.', 'яблоко', 'This {} is very sour.', 'apple')\
            .phrase('{} - мой любимый фрукт.', 'Груша', '{} is my favourite fruit.', 'Pear')\
        .end()\
        .lesson(5)\
            .word('персик', 'персики', 'peach', 'peaches')\
            .word('банан', 'бананы', 'banana', 'bananas')\
            .word('слива', 'сливы', 'plum', 'plums')\
            .word('абрикос', 'абрикосы', 'apricot', 'apricots')\
            .word('ананас', 'ананасы', 'pineapple', 'pineapples')\
            .phrase('{} выращивают на юге.', 'Бананы', '{} are grown in the south.', 'Bananas')\
            .phrase('В этой пицце есть {}.', 'ананасы', 'There are {} in this pizza.', 'pineapples')\
            .phrase('Ты будешь {} или сливу?', 'персик', 'Will you take a {} or a plum?', 'peach')\
        .end()\
        .lesson(6)\
            .word('ложка', 'ложки', 'spoon', 'spoons')\
            .word('вилка', 'вилки', 'fork', 'forks')\
            .word('нож', 'ножи', 'knife', 'knifes')\
            .word('тарелка', 'тарелки', 'plate', 'plates')\
            .word('чашка', 'чашки', 'cup', 'cups')\
            .phrase('Я буду {} чая.', 'чашку', 'I would like a {} of tea.', 'cup')\
            .phrase('Передайте мне {}, пожалуйста.', 'нож', 'Give me the {}, please.', 'knife')\
            .phrase('Добавьте столовую {} муки.', 'ложку', 'Add a table {} of flour.', 'spoon')\
            .phrase('Испоьзуй {} и нож.', 'вилку', 'Use a {} and a knife.', 'fork')\
        .end()\
        .lesson(7)\
            .word('овощ', 'овощи', 'vegetable', 'vegetables')\
            .word('помидор', 'помидоры', 'tomato', 'tomatoes')\
            .word('картофель', 'картофель', 'potato', 'potatoes')\
            .word('морковь', 'морковь', 'carrot', 'carrots')\
            .word('огурец', 'огурцы', 'cucumber', 'cucumbers')\
            .phrase('Ты любишь {}?', 'овощи', 'Do you like {}?', 'vegetables')\
            .phrase('{} оранжевая, а огурец зелёный', 'Морковь', '{} is orange and cucumber is green', 'Carrot')\
        .end()\
        .lesson(8)\
            .word('капуста', 'капуста', 'cabbage', 'cabbages')\
            .word('сельдерей', 'сельдерей', 'celery', 'celeries')\
            .word('тыква', 'тыквы', 'pumpkin', 'pumpkins')\
            .word('перец', 'перцы', 'pepper', 'peppers')\
            .word('соль', 'соль', 'salt', 'salt')\
            .phrase('Ты добавил {} в воду?', 'соль', 'Did you put {} in water?', 'salt')\
            .phrase('Я не люблю {}, а ты?', 'сельдерей', "I don't like {}, and you?", 'celery')\
            .phrase('Она забыла купить {}.', 'перец', 'She forgot to buy {}.', 'pepper')\
        .end()\
        .lesson(9)\
            .word('мука', 'мука', 'flour', 'flour')\
            .word('рис', 'рис', 'rice', 'rice')\
            .word('паста', 'паста', 'pasta', 'pasta')\
            .word('лапша', 'лапша', 'noodles', 'noodles')\
            .word('орех', 'орехи', 'nut', 'nuts')\
            .phrase('Надо купить {} и соль.', 'рис', 'We need to buy {} and salt.', 'rice')\
            .phrase('На ужин у нас {}.', 'паста', 'We have {} for dinner.', 'pasta')\
        .end()\
        .lesson(10)\
            .word('рыба', 'рыбы', 'fish', 'fishes')\
            .word('тунец', 'тунцы', 'tuna', 'tuna')\
            .word('креветка', 'креветки', 'shrimp', 'shrimps')\
            .word('лосось', 'лосось', 'salmon', 'salmon')\
            .word('форель', 'форель', 'trout', 'trout')\
            .phrase('Лосось - морская {}?', 'рыба', 'Is salmon a sea {}?', 'fish')\
        .end()\
        .lesson(11)\
            .word('говядина', 'говядина', 'beef', 'beef')\
            .word('ветчина', 'ветчина', 'ham', 'ham')\
            .word('баранина', 'баранина', 'mutton', 'mutton')\
            .word('свинина', 'свинина', 'pork', 'pork')\
            .word('курица', 'курица', 'chicken', 'chicken')\
            .phrase('У вас есть {} и сыр?', 'ветчина', 'Do you have {} and cheese?', 'ham')\
        .end()\
    .end()\
    .section('Город', 'city')\
        .lesson(1)\
            .word('город', 'города', 'city', 'cities')\
            .word('городок', 'городки', 'town', 'towns')\
            .word('дорога', 'дороги', 'road', 'roads')\
            .word('здание', 'здания', 'building', 'buildings')\
            .word('кафе', 'кафе', 'cafe', 'cafes')\
            .phrase('Давай зайдём в моё любимое {}.', 'кафе', "Let's visit my favourite {}.", 'cafe')\
        .end()\
        .lesson(2)\
            .word('пекарня', 'пекарни', 'bakery', 'bakeries')\
            .word('бакалейный магазин', 'бакалейные магазины', 'grocery', 'groceries')\
            .word('мясной магазин', 'мясные магазины', "butcher's", "butcher's")\
            .word('супермаркет', 'супермаркеты', 'supermarket', 'supermarkets')\
            .word('торговый центр', 'торговые центры', 'shopping mall', 'shopping malls')\
            .phrase('По дороге домой они зашли в {}.', 'торговый центр', 'On the way back home they visited a {}.', 'shopping mall')\
        .end()\
        .lesson(3)\
            .word('школа', 'школы', 'school', 'schools')\
            .word('больница', 'больницы', 'hospital', 'hospitals')\
            .word('театр', 'театры', 'theatre', 'theatres')\
            .word('кинотеатр', 'кинотеатры', 'cinema', 'cinemas')\
            .word('галерея', 'галереи', 'art gallery', 'art galleries')\
            .phrase('Давай сходим в {}?', 'театр', "Let's go to the {}.", 'theatre')\
        .end()\
        .lesson(4)\
            .word('аптека', 'аптеки', 'pharmacy', 'pharmacies')\
            .word('почта', 'почты', 'post office', 'post offices')\
            .word('библиотека', 'библиотеки', 'library', 'libraries')\
            .word('церковь', 'церкви', 'church', 'churches')\
            .word('мечеть', 'мечети', 'mosque', 'mosques')\
            .phrase('На нашей улице недавно открылась {}.', 'библиотека', 'A {} has opened on our street recently.', 'library')\
            .phrase('{} находится за углом.', 'Аптека', 'The {} is around the corner.', 'pharmacy')\
        .end()\
        .lesson(5)\
            .word('клуб', 'клубы', 'club', 'clubs')\
            .word('вокзал', 'вокзалы', 'railway station', 'railway stations')\
            .word('банк', 'банки', 'bank', 'banks')\
            .word('музей', 'музеи', 'museum', 'museums')\
            .word('ресторан', 'рестораны', 'restaurant', 'restaurants')\
            .phrase('Где находится вегетарианский {}?', 'ресторан', 'Where is a vegetarian {}?', 'restaurant')\
        .end()\
    .end()\
    .section('Транспорт', 'transport')\
        .lesson(1)\
            .word('транспорт', 'транспорт', 'transport', 'transport')\
            .word('автобус', 'автобусы', 'bus', 'buses')\
            .word('трамвай', 'трамваи', 'tram', 'trams')\
            .word('троллейбус', 'троллейбусы', 'trolleybus', 'trolleybuses')\
            .word('поезд', 'поезда', 'train', 'trains')\
            .phrase('Этот {} опаздывает.', 'поезд', 'This {} is late.', 'train')\
            .phrase('{} 12 идёт до музея?', 'Трамвай', 'Does {} 12 go to the museum?', 'tram')\
        .end()\
        .lesson(2)\
            .word('машина', 'машины', 'car', 'cars')\
            .word('такси', 'такси', 'taxi', 'taxis')\
            .word('велосипед', 'велосипеды', 'bike', 'bikes')\
            .word('мотоцикл', 'мотоциклы', 'motorbike', 'motorbikes')\
            .word('грузовик', 'грузовики', 'truck', 'trucks')\
            .phrase('До центра можно добраться на {} или метро.', 'такси', 'The center can be reached by {} or by metro.', 'taxi')\
        .end()\
    .end()\
    .section('Время', 'time')\
        .lesson(1)\
            .word('неделя', 'недели', 'week', 'weeks')\
            .word('понедельник', 'понедельники', 'monday', 'mondays')\
            .word('вторник', 'вторники', 'tuesday', 'tuesdays')\
            .word('среда', 'среды', 'wednesday', 'wednesdays')\
            .word('четверг', 'четверги', 'thursday', 'thursdays')\
            .word('пятница', 'пятницы', 'friday', 'fridays')\
            .word('суббота', 'субботы', 'saturday', 'saturdays')\
            .word('воскресенье', 'воскресенья', 'sunday', 'sundays')\
            .phrase('В это {} я поеду в Лондон.', 'воскресенье', "This {} I'll go to London.", 'sunday')\
        .end()\
        .lesson(2)\
            .word('вчера', 'вчера', 'yesterday', 'yesterday')\
            .word('сегодня', 'сегодня', 'today', 'today')\
            .word('завтра', 'завтра', 'tomorrow', 'tomorrow')\
            .word('месяц', 'месяцы', 'month', 'months')\
            .word('год', 'года', 'year', 'years')\
            .phrase('Этот учебный {} был довольно простым.', 'год', 'This academic {} has been quite an easy one.', 'year')\
            .phrase('Следующий {} я проведу в Лондоне.', 'месяц', 'I will spend the next {} in London.', 'month')\
            .phrase('{} я иду к дантисту.', 'Завтра', '{} I am visiting the dentist.', 'Tomorrow')\
        .end()\
        .lesson(3)\
            .word('январь', 'январь', 'january', 'january')\
            .word('февраль', 'февраль', 'february', 'february')\
            .word('март', 'март', 'march', 'march')\
            .word('апрель', 'апрель', 'april', 'april')\
            .word('май', 'май', 'may', 'may')\
            .word('июнь', 'июнь', 'june', 'june')\
            .word('июль', 'июль', 'july', 'july')\
            .word('август', 'август', 'august', 'august')\
            .word('сентябрь', 'сентябрь', 'september', 'september')\
            .word('октябрь', 'октябрь', 'october', 'october')\
            .word('ноябрь', 'ноябрь', 'november', 'november')\
            .word('декабрь', 'декабрь', 'december', 'december')\
            .phrase('Месяц моего рождения - {}.', 'август', '{} is a month of my birth.', 'August')\
        .end()\
    .end()\
    .section('Профессии', 'professions')\
        .lesson(1)\
            .word('актёр', 'актёры', 'actor', 'actors')\
            .word('архитектор', 'архитекторы', 'architect', 'architects')\
            .word('художник', 'художники', 'artist', 'artists')\
            .word('атлет', 'атлеты', 'athlete', 'athletes')\
            .word('банкир', 'банкиры', 'banker', 'banker')\
            .phrase('Моя мама - {}.', 'архитектор', 'My mom is an {}', 'architect')\
            .phrase('В вашей семье есть {}?', 'банкир', 'Is there a {} in your family?', 'banker')\
        .end()\
        .lesson(2)\
            .word('кузнец', 'кузнецы', 'blacksmith', 'blacksmith')\
            .word('мясник', 'мясники', 'butcher', 'butchers')\
            .word('плотник', 'плотники', 'carpenter', 'carpenter')\
            .word('кассир', 'кассиры', 'cashier', 'cashiers')\
            .word('повар', 'повара', 'cook', 'cooks')\
            .phrase('Мой брат - {} в ресторане на главной улице.', 'повар', 'My brother is a {} in the restaurant on the main street.', 'cook')\
        .end()\
        .lesson(3)\
            .word('дантист', 'дантисты', 'dentist', 'dentists')\
            .word('доктор', 'доктора', 'doctor', 'doctors')\
            .word('электрик', 'электрики', 'electrician', 'electricians')\
            .word('инженер', 'инженеры', 'engineer', 'engineers')\
            .word('фермер', 'фермеры', 'farmer', 'farmers')\
            .phrase('Эта семейная пара - {}.', 'доктора', 'This spouses are {}.', 'doctors')\
        .end()\
        .lesson(4)\
            .word('пожарник', 'пожарники', 'firefighter', 'firefighters')\
            .word('финансист', 'финансисты', 'financier', 'financiers')\
            .word('фабричный работник', 'фабричные работники', 'factory worker', 'factory workers')\
            .word('садовник', 'садовники', 'gardener', 'gardeners')\
            .word('ювелир', 'ювелиры', 'goldsmith', 'goldsmiths')\
            .phrase('Мама моего друга - {}.', 'ювелир', 'The mother of my friend is a {}.', 'goldsmith')\
        .end()\
        .lesson(5)\
            .word('парикмахер', 'парикмахеры', 'hairdresser', 'hairdressers')\
            .word('юрист/адвокат', 'юристы/адвокаты', 'lawyer', 'lawyers')\
            .word('библиотекарь', 'библиотекари', 'librarian', 'librarians')\
            .word('механик', 'механики', 'mechanic', 'mechanics')\
            .word('модель', 'модели', 'model', 'models')\
            .phrase('{} - востребованная профессия.', 'Юрист', '{} is a demanded trade.', 'Lawyer')\
        .end()\
        .lesson(6)\
            .word('музыкант', 'музыканты', 'musician', 'musician')\
            .word('медсестра/медбрат', 'медсёстры/медбратья', 'nurse', 'nurses')\
            .word('пилот', 'пилоты', 'pilot', 'pilots')\
            .word('полицейский', 'полицейские', 'police officer', 'police officers')\
            .word('водопроводчик', 'водопроводчики', 'plumber', 'plumbers')\
            .phrase('{} - очень ответственная работа.', 'Пилот', '{} is a responsible work.', 'Pilot')\
        .end()\
        .lesson(7)\
            .word('тур-агент', 'тур-агенты', 'travel agent', 'travel agents')\
            .word('программист', 'программисты', 'programmer', 'programmers')\
            .word('учитель', 'учителя', 'teacher', 'teachers')\
            .word('официант', 'официанты', 'waiter', 'waiters')\
            .word('писатель', 'писатели', 'writer', 'writers')\
            .phrase('Мой {} получил премию за свою работу.', 'учитель', 'My {} received a bounty for his work.', 'teacher')\
        .end()\
    .end()\
