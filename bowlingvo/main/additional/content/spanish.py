from .. import content_filler

def main():
    LexContent = content_filler.LexContent
    GramContent = content_filler.GramContent
    content_filler.LANG = 'spanish'

    span_lex = LexContent('Испанский', 'spanish')
    span_lex.section('Еда', 'comida')\
        .lesson(1)\
            .word('завтрак', 'завтраки', 'el desayuno', 'los desayunos')\
            .word('хлеб', 'хлеба', 'el pan', 'los panes')\
            .word('сыр', 'сыры', 'el queso', 'los quesos')\
            .word('сливочное масло', 'сливочное масло', 'la manteca', 'las mantecas')\
            .word('йогурт', 'йогурты', 'el yogurt', 'los yogures')\
            .phrase('Я ем на завтрак тост и {}.', 'сыр', 'Como tostadas y {} para el desayuno.', 'queso')\
            .phrase('Мой брат любит персиковый {}.', 'йогурт', 'A mi hermano le gusta el {} de durazno.', 'yogurt')\
            .phrase('{} - важный приём пищи.', 'Завтрак', 'El {} es una comida importante..', 'desayuno')\
        .end()\
        .lesson(2)\
            .word('чай', 'чаи', 'el té', 'los tés')\
            .word('кофе', 'кофе', 'el café', 'los cafés')\
            .word('молоко', 'молоко', 'la leche', 'la leche')\
            .word('хлопья', 'хлопья', 'el cereal', 'los cereales')\
            .word('сахар', 'сахар', 'el azucar', 'los azucares')\
            .phrase('Я не пью {} с молоком.', 'чай', 'No bebo {} con leche.', 'té')\
            .phrase('Ты ешь {} на завтрак?', 'хлопья', 'Comes {} para el desayuno?', 'cereal')\
        .end()\
        .lesson(3)\
            .word('десерт', 'десерты', 'el postre', 'los postres')\
            .word('торт', 'торты', 'el pastel', 'los pasteles')\
            .word('печенье', 'печенья', 'la galleta', 'las galletas')\
            .word('блин', 'блины', 'el panqueque', 'los panqueques')\
            .phrase('Я люблю есть {} на завтрак.', 'блины', 'Me gusta comer {} para el desayuno.', 'panqueques')\
        .end()\
        .lesson(4)\
            .word('мороженое', 'мороженое', 'el helado', 'los helados')\
            .word('варенье', 'варенья', 'la mermelada', 'las marmeladas')\
            .word('мёд', 'мёд', 'el cariño', 'el cariño')\
            .word('сметана', 'сметана', 'la crema agria', 'la crema agria')\
            .word('конфета', 'конфеты', 'el dulce', 'los dulces')\
            .phrase('Какой вкус {} твой любимый?', 'мороженого', 'Cuál es tu sabor de {} favorito?', 'helado')\
        .end()\
        .lesson(5)\
            .word('обед', 'обеды', 'el almuerzo', 'los almuerzos')\
            .word('ужин','ужины', 'la cena', 'las cenas')\
            .word('салат', 'салаты', 'la ensalada', 'las ensaladas')\
            .word('сок', 'соки', 'el jugo', 'los jogos')\
            .word('стейк', 'стейки', 'el filete', 'los filetes')\
            .phrase('Я не очень люблю {}, но мне нравятся стейки.', 'салаты', 'Realmente no me gustan las {}, pero me gustan los filetes.', 'ensaladas')\
            .phrase('Вы бы хотели немного {}?', 'сока', 'Te gustaría un poco de {}?', 'jugo')\
        .end()\
        .lesson(6)\
            .word('фрукт', 'фрукты', 'la fruta', 'las frutas')\
            .word('яблоко', 'яблоки', 'la manzana', 'las manzanas')\
            .word('апельсин', 'апельсины', 'la naranja', 'las naranjas')\
            .word('груша', 'груши', 'la pera', 'las peras')\
            .word('лимон', 'лимоны', 'el limon', 'los limones')\
            .phrase('Какой твой любимый {}?', 'фрукт', 'Cuál es tu {} favorita?', 'fruta')\
            .phrase('Это {} очень кислое.', 'яблоко', 'Esta {} es muy amarga.', 'manzana')\
            .phrase('{} - мой любимый фрукт.', 'Груша', 'La {} es mi fruta favorita.', 'pera')\
        .end()\
    .end()\
    .section('Город', 'cuidad')\
        .lesson(1)\
            .word('город', 'города', 'la ciudad', 'las ciudades')\
            .word('городок', 'городки', 'el pueblo', 'los pueblos')\
            .word('дорога', 'дороги', 'el camino', 'los caminos')\
            .word('здание', 'здания', 'el costruccion', 'los construcciones')\
            .word('столица', 'столицы', 'la capital', 'las capitales')\
            .phrase('Давай заедем в мой любимый {}.', 'городок', 'Vamos a mi {} favorito', 'pueblo')\
        .end()\
        .lesson(2)\
            .word('улица', 'улицы', 'la calle', 'las calles')\
            .word('проспект', 'проспекты', 'la avenida', 'las avenidas')\
            .word('квартал', 'кварталы', 'el cuarto', 'los cuartos')\
            .word('район', 'районы', 'el distrito', 'los distritos')\
            .phrase('Пройдите этот {} и поверните налево.', 'квартал', 'Pasa por este {} y gira a la izquierda.', 'cuarto')\
            .phrase('Этот {} проходит через весь город с севера на юг.', 'проспект', 'Esta {} atraviesa la ciudad de norte a sur.', 'avenida')\
        .end()\
        .lesson(3)\
            .word('пекарня', 'пекарни', 'la panadería', 'las panaderías')\
            .word('продуктовый магазин', 'продуктовые магазины', 'la tienda', 'las tiendas')\
            .word('супермаркет', 'супермаркеты', 'el supermercado', 'los supermercados')\
            .word('торговый центр', 'торговые центры', 'shopping mall', 'shopping malls')\
            .word('кафе', 'кафе', 'cafe', 'cafes')\
            .phrase('По дороге домой они зашли в {}.', 'торговый центр', 'On the way back home they visited a {}.', 'shopping mall')\
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
        .lesson(3)\
            .word('метро', 'метро', 'metro', 'metro')\
            .word('метро (UK)', 'метро (UK)', 'underground', 'underground')\
            .word('метро (US)', 'метро (US)', 'subway', 'subway')\
            .word('станция', 'станции', 'station', 'stations')\
            .word('остановка', 'остановки', 'stop', 'stops')\
            .phrase('{} московского метро очень красивые.', 'Станции', 'Moscow metro {} are very beautiful.', 'stations')\
            .phrase('Самое старое {} в Лондоне.', 'метро', 'London {} is the oldest one.', 'underground')\
        .end()\
        .lesson(4)\
            .word('лодка', 'лодки', 'boat', 'boats')\
            .word('корабль', 'корабли', 'ship', 'ships')\
            .word('самолёт', 'самолёты', 'plane', 'planes')\
            .word('вертолёт', 'вертолёты', 'helicopter', 'helicopters')\
            .phrase('{} причалил к пристани.', 'Корабль', 'The {} moored to the pier.', 'ship')\
        .end()\
        .lesson(5)\
            .word('расписание', 'расписания', 'schedule', 'schedules')\
            .word('маршрут', 'маршруты', 'route', 'routes')\
            .word('линия', 'линии', 'line', 'lines')\
            .word('конечная', 'конечные', 'terminal', 'terminal')\
            .word('пересадка', 'пересадки', 'transfer', 'transfers')\
            .phrase('Здесь есть {} на поезда линии 5.', 'пересадка', 'There is a {} for the line 5 trains.', 'transfer')\
        .end()\
        .lesson(6)\
            .word('пассажир', 'пассажиры', 'passenger', 'passengers')\
            .word('билет', 'билеты', 'ticket', 'tickets')\
            .word('багаж', 'багаж', 'luggage', 'luggage')\
            .word('отбытие', 'отбытия', 'departure', 'departures')\
            .word('прибытие', 'прибытия', 'arrival', 'arrivals')\
            .phrase('Предъявите ваши {}.', 'билеты', 'Present your {}.', 'tickets')\
        .end()\
    .end()\
    .section('Дом', 'house')\
        .lesson(1)\
            .word('дом (здание)', 'дома (здания)', 'house', 'houses')\
            .word('дом', 'дом', 'home', 'home')\
            .word('этаж', 'этажи', 'floor', 'floors')\
            .word('комната', 'комнаты', 'room', 'rooms')\
            .word('крыша', 'крыши', 'roof', 'roofs')\
            .phrase('Мы переехали в новый {}.', 'дом', 'We moved to a new {}.', 'house')\
            .phrase('Я хочу вернуться {}.', 'домой', 'I want to return {}.', 'home')\
        .end()\
        .lesson(2)\
            .word('дверь', 'двери', 'door', 'doors')\
            .word('окно', 'окна', 'window', 'windows')\
            .word('пол', 'полы', 'floor/2', 'floors/2')\
            .word('потолок', 'потолки', 'ceiling', 'ceilings')\
            .word('балкон', 'балконы', 'balcony', 'balconies')\
            .phrase('Можно ли мне открыть {}?', 'окно', 'May I open the {}?', 'window')\
        .end()\
        .lesson(3)\
            .word('кухня', 'кухни', 'kitchen', 'kitchens')\
            .word('гостиная', 'гостиные', 'living room', 'living rooms')\
            .word('прихожая', 'прихожие', 'hall', 'halls')\
            .word('спальня', 'спальни', 'bedroom', 'bedrooms')\
            .word('ванная', 'ванные', 'bathroom', 'bathrooms')\
            .word('туалет', 'туалеты', 'toilet', 'toilets')\
            .phrase('Моё любимое место в доме - {}.', 'кухня', 'My favourite place in house is {}.', 'kitchen')\
        .end()\
        .lesson(4)\
            .word('стена', 'стены', 'wall', 'walls')\
            .word('шкаф', 'шкафы', 'cupboard', 'cupboards')\
            .word('ящик', 'ящики', 'drawer', 'drawers')\
            .word('стол', 'столы', 'table', 'tables')\
            .word('стул', 'стулья', 'chair', 'chairs')\
            .phrase('Уберите свои вещи в {}.', 'ящик', 'Put your stuff into the {}.', 'drawer')\
        .end()\
        .lesson(5)\
            .word('диван', 'диваны', 'sofa', 'sofas')\
            .word('кресло', 'кресла', 'armchair', 'armchairs')\
            .word('полка', 'полки', 'shelf', 'shelves')\
            .word('ковёр', 'ковры', 'carpet', 'carpets')\
            .word('комнатное растение', 'комнатные растения', 'indoor plant', 'indoor plants')\
            .phrase('Я хочу купить новый {}.', 'диван', 'I want to buy a new {}.', 'sofa')\
            .phrase('Этот {} просто ужасен!', 'ковёр', 'This {} is absolutely awful!', 'carpet')\
        .end()\
        .lesson(6)\
            .word('лампа', 'лампы', 'lamp', 'lamps')\
            .word('кровать', 'кровати', 'bed', 'beds')\
            .word('зеркало', 'зеркала', 'mirror', 'mirrors')\
            .word('штора', 'шторы', 'curtain', 'curtains')\
            .word('платяной шкаф', 'платяные шкафы', 'wardrobe', 'wardrobes')\
            .phrase('Выключи {}, пожалуйста, я хочу спать.', 'лампу', 'Please turn off the {}, I want to sleep.', 'lamp')\
        .end()\
        .lesson(7)\
            .word('подушка', 'подушки', 'pillow', 'pillows')\
            .word('одеяло', 'одеяла', 'blanket', 'blankets')\
            .word('матрац', 'матрацы', 'mattress', 'mattresses')\
            .word('простыня', 'простыни', 'sheet', 'sheets')\
            .word('будильник', 'будильники', 'alarm clock', 'alarm clocks')\
            .phrase('Мне нужно новое {}.', 'одеяло', 'I need a new {}.', 'blanket')\
        .end()\
        .lesson(8)\
            .word('плита', 'плиты', 'cooker', 'cookers')\
            .word('духовка', 'духовки', 'oven', 'ovens')\
            .word('холодильник', 'холодильники', 'fridge/refrigerator', 'fridges/refrigerators')\
            .word('раковина', 'раковины', 'sink', 'sinks')\
            .word('посудомоечная машина', 'посудомойки', 'dishwasher', 'dishwashers')\
            .phrase('Выключайте {} перед уходом.', 'плиту', 'Turn off the {} before leaving.', 'cooker')\
        .end()\
        .lesson(9)\
            .word('сковорода', 'сковороды', 'pan', 'pans')\
            .word('кастрюля', 'кастрюли', 'saucepan', 'saucepans')\
            .word('чайник', 'чайники', 'kettle', 'kettles')\
            .word('тостер', 'тостеры', 'toaster', 'toasters')\
            .word('миска', 'миски', 'bowl', 'bowls')\
            .phrase('{} ещё не закипел?', 'Чайник', 'Did {} boil?', 'kettle')\
        .end()\
        .lesson(10)\
            .word('ванна', 'ванны', 'bath', 'baths')\
            .word('душ', 'душ', 'shower', 'showers')\
            .word('кран', 'краны', 'tap', 'taps')\
            .word('мыло', 'мыла', 'soap', 'soaps')\
            .word('полотенце', 'полотенца', 'towel', 'towels')\
            .phrase('Мне определённо нужна горячая {}.', 'ванна', 'I definitely need a hot {}.', 'bath')\
            .phrase('Ты можешь взять красное {}.', 'полотенце', 'You can take a red {}.', 'towel')\
        .end()\
        .lesson(11)\
            .word('утюг', 'утюги', 'iron', 'irons')\
            .word('пылесос', 'пылесосы', 'vacuum cleaner', 'vacuum cleaners')\
            .word('ведро', 'вёдра', 'bucket', 'buckets')\
            .word('стиральная машина', 'стиральные машины', 'washing machine', 'washing machines')\
            .word('щётка', 'щётки', 'brush', 'brushes')\
            .phrase('Ты выключил {}?', 'утюг', 'Did you turn off the {}?', 'iron')\
        .end()\
        .lesson(12)\
            .word('пыль', 'пыль', 'dust', 'dust')\
            .word('часы', 'часы', 'clock', 'clock')\
            .word('книжная полка', 'книжные полки', 'bookshelf', 'bookshelves')\
            .word('метла', 'мётлы', 'broom', 'brooms')\
            .word('ключ', 'ключи', 'key', 'keys')\
            .phrase('{} остановились.', 'Часы', 'The {} stopped.', 'clock')\
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
            .phrase('В это {} я поеду в Лондон.', 'воскресенье', 'This {} I\'ll go to London.', 'sunday')\
        .end()\
        .lesson(2)\
            .word('вчера', 'вчера', 'yesterday', 'yesterday')\
            .word('сегодня', 'сегодня', 'today', 'today')\
            .word('завтра', 'завтра', 'tomorrow', 'tomorrow')\
            .word('день', 'дни', 'day', 'days')\
            .word('месяц', 'месяцы', 'month', 'months')\
            .word('год', 'года', 'year', 'years')\
            .phrase('Этот учебный {} был довольно простым.', 'год', 'This academic {} was quite an easy one.', 'year')\
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
        .lesson(4)\
            .word('время года', 'времена года', 'season', 'seasons')\
            .word('осень', 'осени', 'autumn', 'autumns')\
            .word('зима', 'зимы', 'winter', 'winters')\
            .word('весна', 'вёсны', 'spring', 'springs')\
            .word('лето', 'лета', 'summer', 'summers')\
            .phrase('Это {} будет лучшим в моей жизни.', 'лето', 'This {} will be the best in my life.', 'summer')\
        .end()\
        .lesson(5)\
            .word('календарь', 'календари', 'calendar', 'calendars')\
            .word('час', 'часы', 'hour', 'hours')\
            .word('минута', 'минуты', 'minute', 'minutes')\
            .word('секунда', 'секунды', 'second', 'seconds')\
            .word('ночь', 'ночи', 'night', 'nights')\
            .phrase('Сколько {} до конца урока?', 'минут', 'How many {} till the end of the lesson?', 'minutes')\
        .end()\
        .lesson(6)\
            .word('полдень', 'полудни', 'noon', 'noons')\
            .word('закат', 'закаты', 'sunset', 'sunsets')\
            .word('рассвет', 'рассветы', 'dawn', 'dawns')\
            .word('сумерки', 'сумерки', 'dusk', 'dusks')\
            .word('утро', 'утра', 'morning', 'mornings')\
            .word('вечер', 'вечера', 'evening', 'evenings')\
            .phrase('Моё любимое время суток - {}.', 'сумерки', 'My favourite time of the day is {}.', 'dusk')\
        .end()\
    .end()\
    .section('Профессии', 'professions')\
        .lesson(1)\
            .word('актёр', 'актёры', 'actor', 'actors')\
            .word('архитектор', 'архитекторы', 'architect', 'architects')\
            .word('художник', 'художники', 'artist', 'artists')\
            .word('атлет', 'атлеты', 'athlete', 'athletes')\
            .word('банкир', 'банкиры', 'banker', 'banker')\
            .phrase('Моя мама - {}.', 'архитектор', 'My mom is an {}.', 'architect')\
            .phrase('В вашей семье есть {}?', 'банкир', 'Is there a {} in your family?', 'banker')\
        .end()\
        .lesson(2)\
            .word('кузнец', 'кузнецы', 'blacksmith', 'blacksmiths')\
            .word('мясник', 'мясники', 'butcher', 'butchers')\
            .word('плотник', 'плотники', 'carpenter', 'carpenters')\
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
            .phrase('Эта семейная пара - {}.', 'доктора', 'These spouses are {}.', 'doctors')\
        .end()\
        .lesson(4)\
            .word('пожарник', 'пожарники', 'firefighter', 'firefighters')\
            .word('финансист', 'финансисты', 'financier', 'financiers')\
            .word('фабричный работник', 'фабричные работники', 'factory worker', 'factory workers')\
            .word('садовник', 'садовники', 'gardener', 'gardeners')\
            .word('ювелир', 'ювелиры', 'jeweler', 'jewelers')\
            .phrase('Мама моего друга - {}.', 'ювелир', 'The mother of my friend is a {}.', 'jeweler')\
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
            .word('музыкант', 'музыканты', 'musician', 'musicians')\
            .word('медсестра/медбрат', 'медсёстры/медбратья', 'nurse', 'nurses')\
            .word('пилот', 'пилоты', 'pilot', 'pilots')\
            .word('полицейский', 'полицейские', 'police officer', 'police officers')\
            .word('водопроводчик', 'водопроводчики', 'plumber', 'plumbers')\
            .phrase('{} - очень ответственная работа.', 'Пилот', '{} is a highly responsible work.', 'Pilot')\
        .end()\
        .lesson(7)\
            .word('тур-агент', 'тур-агенты', 'travel agent', 'travel agents')\
            .word('программист', 'программисты', 'programmer', 'programmers')\
            .word('учитель', 'учителя', 'teacher', 'teachers')\
            .word('официант', 'официанты', 'waiter', 'waiters')\
            .word('писатель', 'писатели', 'writer', 'writers')\
            .phrase('Мой {} получил премию за свою работу.', 'учитель', 'My {} received a bonus for his work.', 'teacher')\
        .end()\
    .end()\
    .section('Спорт', 'sport')\
        .lesson(1)\
            .word('спорт', 'спорт', 'sport', 'sport')\
            .word('футбол', 'футбол', 'football', 'football')\
            .word('баскетбол', 'баскетбол', 'basketball', 'basketball')\
            .word('волейбол', 'волейбол', 'volleyball', 'volleyball')\
            .word('мяч', 'мячи', 'ball', 'balls')\
            .phrase('Брось мне {}.', 'мяч', 'Throw me a {}.', 'ball')\
        .end()\
        .lesson(2)\
            .word('ворота/2', 'ворота/2', 'goal', 'goals')\
            .word('кольцо', 'кольца', 'basket ring', 'basket rings')\
            .word('судья на поле', 'судьи на поле', 'referee', 'referees')\
            .word('судья', 'судьи', 'judge', 'judges')\
            .word('сетка', 'сетки', 'net', 'nets')\
            .phrase('Цель игры - забить мяч в {}.', 'ворота', 'The purpose of the game is to score the ball into the {}.', 'goal')\
            .phrase('{} показал мне жёлтую карточку.', 'Судья', '{} showed me a yellow card.', 'Referee')\
        .end()\
        .lesson(3)\
            .word('теннис', 'теннис', 'tennis', 'tennis')\
            .word('ракетка', 'ракетки', 'racket', 'rackets')\
            .word('гольф', 'гольф', 'golf', 'golf')\
            .word('клюшка для гольфа', 'клюшки для гольфа', 'club/2', 'clubs/2')\
            .word('лунка', 'лунки', 'hole', 'holes')\
            .phrase('{} лежат на столе.', 'Ракетки', 'The {} are on the table.', 'rackets')\
        .end()\
        .lesson(4)\
            .word('бадминтон', 'бадминтон', 'badminton', 'badminton')\
            .word('воланчик', 'воланчики', 'shuttlecock', 'shuttlecock')\
            .word('хоккей', 'хоккей', 'hockey', 'hockey')\
            .word('клюшка', 'клюшки', 'stick', 'sticks')\
            .word('коньки', 'коньки', 'ice skates', 'ice skates')\
            .phrase('В хоккее используются {}.', 'коньки', '{} are used in hockey', 'Ice skates')\
        .end()\
    .end()\
    .section('Семья', 'family')\
        .lesson(1)\
            .word('семья', 'семьи', 'family', 'families')\
            .word('мать', 'матери', 'mother', 'mothers')\
            .word('отец', 'отцы', 'father', 'fathers')\
            .word('сестра', 'сёстры', 'sister', 'sisters')\
            .word('брат', 'братья', 'brother', 'brothers')\
            .phrase('У тебя есть {}?', 'братья', 'Do you have {}?', 'brothers')\
            .phrase('Кем работает твой {}?', 'отец', 'What is your {}\'s job?', 'father')\
        .end()\
        .lesson(2)\
            .word('сын', 'сыновья', 'son', 'sons')\
            .word('дочь', 'дочери', 'daughter', 'daughters')\
            .word('дедушка', 'дедушки', 'grandfather', 'grandfathers')\
            .word('бабушка', 'бабушки', 'grandmother', 'grandmothers')\
            .word('дядя', 'дяди', 'uncle', 'uncles')\
            .word('тётя', 'тёти', 'aunt', 'aunts')\
            .phrase('Где живёт твоя {}?', 'тётя', 'Where does your {} live?', 'aunt')\
        .end()\
        .lesson(3)\
            .word('родитель', 'родители', 'parent', 'parents')\
            .word('ребёнок', 'дети', 'child', 'children')\
            .word('племянник', 'племянники', 'nephew', 'nephews')\
            .word('племянница', 'племянницы', 'niece', 'nieces')\
            .word('кузен/кузина', 'кузены', 'cousin', 'cousins')\
            .phrase('{} играют перед домом.', 'Дети', 'The {} are playing in front of the house', 'children')\
        .end()\
    .end()\
    .section('Тело человека', 'body')\
        .lesson(1)\
            .word('тело', 'тела', 'body', 'bodies')\
            .word('кожа', 'кожа', 'skin', 'skin')\
            .word('голова', 'головы', 'head', 'heads')\
            .word('череп', 'черепа', 'skull', 'skulls')\
            .word('мозг', 'мозги', 'brain', 'brains')\
            .word('лицо', 'лица', 'face', 'faces')\
            .phrase('Я не узнаю его {}.', 'лицо', 'I don\'t recognize his {}.', 'face')\
            .phrase('У меня болит {}.', 'голова', 'My {} aches.', 'head')\
        .end()\
        .lesson(2)\
            .word('глаз', 'глаза', 'eye', 'eyes')\
            .word('нос', 'носы', 'nose', 'noses')\
            .word('ухо', 'уши', 'ear', 'ears')\
            .word('волос', 'волосы', 'hair', 'hair')\
            .word('рот', 'рты', 'mouth', 'mouths')\
            .word('губа', 'губы', 'lip', 'lips')\
            .phrase('У неё красивые серые {}.', 'глаза', 'She has beautiful gray {}.', 'eyes')\
            .phrase('Мне нравятся мои вьющиеся {}.', 'волосы', 'I love my curly {}.', 'hair')\
        .end()\
        .lesson(3)\
            .word('шея', 'шеи', 'neck', 'necks')\
            .word('зуб', 'зубы', 'tooth', 'teeth')\
            .word('лоб', 'лбы', 'forehead', 'forehead')\
            .word('щека', 'щёки', 'cheek', 'cheeks')\
            .word('челюсть', 'челюсти', 'jaw', 'jaws')\
            .word('язык', 'языки', 'tongue', 'tongues')\
            .phrase('У моего ребёнка выпал молочный {}.', 'зуб', 'My child\'s milk {} fell out.', 'tooth')\
        .end()\
        .lesson(4)\
            .word('туловище', 'туловища', 'torso', 'torsos')\
            .word('скелет', 'скелеты', 'skeleton', 'skeletons')\
            .word('кость', 'кости', 'bone', 'bones')\
            .word('грудная клетка', 'грудные клетки', 'chest', 'chests')\
            .word('спина', 'спины', 'back', 'backs')\
            .phrase('Собака грызёт {}.', 'кость', 'The dog gnaws a {}.', 'bone')\
        .end()\
        .lesson(5)\
            .word('плечо', 'плечи', 'shoulder', 'shoulders')\
            .word('ребро', 'рёбра', 'rib', 'ribs')\
            .word('талия', 'талии', 'waist', 'waists')\
            .word('живот', 'животы', 'stomach', 'stomaches')\
            .word('конечность', 'конечности', 'limb', 'limbs')\
            .phrase('Болит ли у тебя {}?', 'живот', 'Do you have a {} pain?', 'stomach')\
        .end()\
        .lesson(6)\
            .word('рука', 'руки', 'arm', 'arms')\
            .word('палец руки', 'пальцы руки', 'finger', 'fingers')\
            .word('ноготь', 'ногти', 'nail', 'nails')\
            .word('ладонь', 'ладони', 'palm', 'palms')\
            .word('кисть', 'кисти', 'hand', 'hands')\
            .word('кулак', 'кулаки', 'fist', 'fists')\
            .word('локоть', 'локти', 'elbow', 'elbows')\
            .phrase('Я ношу кольцо на указательном {}.', 'пальце', 'I wear a ring on my index {}.', 'finger')\
        .end()\
        .lesson(7)\
            .word('нога', 'ноги', 'leg', 'legs')\
            .word('стопа', 'стопы', 'foot', 'feet')\
            .word('палец ноги', 'пальцы ноги', 'toe', 'toes')\
            .word('колено', 'колени', 'knee', 'knees')\
            .word('пятка', 'пятки', 'heel', 'heels')\
            .word('лодыжка', 'лодыжки', 'ankle', 'ankles')\
            .phrase('Я ударил {}.', 'колено', 'I hit my {}.', 'knee')\
        .end()\
        .lesson(8)\
            .word('внутренний орган', 'внутренние органы', 'internal organ', 'internal organs')\
            .word('сердце', 'сердца', 'heart', 'hearts')\
            .word('печень', 'печени', 'liver', 'livers')\
            .word('лёгкое', 'лёгкие', 'lung', 'lungs')\
            .word('почка', 'почки', 'kidney', 'kidneys')\
            .phrase('Моя любимая песня - \'Ничто не разбивается, как {}\'.', 'сердце', 'My favourite song is \'Nothing breaks like a {}\'.', 'heart')\
        .end()\
    .end()\
    .section('Одежда', 'clothing')\
        .lesson(1)\
            .word('одежда', 'одежда', 'clothing', 'clothing')\
            .word('мода', 'мода', 'fashion', 'fashion')\
            .word('костюм', 'костюмы', 'suit', 'suits')\
            .word('пиджак', 'пиджаки', 'jacket', 'jackets')\
            .word('брюки', 'брюки', 'trousers', 'trousers')\
            .phrase('Я надену {} завтра.', 'костюм', 'I\'ll put on a {} tomorrow.', 'suit')\
        .end()\
        .lesson(2)\
            .word('рубашка', 'рубашки', 'shirt', 'shirts')\
            .word('галстук', 'галстуки', 'tie', 'ties')\
            .word('жилет', 'жилеты', 'vest', 'vests')\
            .word('ботинок', 'ботинки', 'boot', 'boots')\
            .word('ремень', 'ремни', 'belt', 'belts')\
            .phrase('Эти {} мне малы.', 'ботинки', 'This {} are small for me.', 'boots')\
        .end()\
        .lesson(3)\
            .word('футболка', 'футболки', 'T-shirt', 'T-shirts')\
            .word('свитер', 'свитеры', 'sweater', 'sweaters')\
            .word('джинсы', 'джинсы', 'jeans', 'jeans')\
            .word('жакет', 'жакеты', 'jacket/2', 'jackets/2')\
            .word('кроссовок', 'кроссовки', 'sneaker', 'sneakers')\
            .phrase('У вас есть такая {}, только маленькая?', 'футболка', 'Do you have this {} in small?', 'T-shirt')\
        .end()\
        .lesson(4)\
            .word('платье', 'платья', 'dress', 'dresses')\
            .word('юбка', 'юбки', 'skirt', 'skirts')\
            .word('блузка', 'блузки', 'blouse', 'blouses')\
            .word('шорты', 'шорты', 'shorts', 'shorts')\
            .word('пальто', 'пальто', 'coat', 'coats')\
            .phrase('Это персиковое {} тебе не идёт.', 'пальто', 'This peach {} doesn\'t fit you.', 'coat')\
        .end()\
        .lesson(5)\
            .word('шарф', 'шарфы', 'skarf', 'skarfs')\
            .word('носок', 'носки', 'sock', 'socks')\
            .word('нижнее бельё', 'нижнее бельё', 'underwear', 'underwear')\
            .word('перчатка', 'перчатки', 'glove', 'gloves')\
            .word('колготки', 'колготки', 'tights', 'tights')\
            .phrase('На улице холодно, надень {}.', 'шарф', 'It is cold outside, put on a {}.', 'scarf')\
        .end()\
        .lesson(6)\
            .word('воротник', 'воротники', 'collar', 'collars')\
            .word('карман', 'карманы', 'pocket', 'pockets')\
            .word('пуговица', 'пуговицы', 'button', 'buttons')\
            .word('рукав', 'рукава', 'sleeve', 'sleeves')\
            .word('капюшон', 'капюшоны', 'hood', 'hoods')\
            .phrase('У тебя небольшое пятно на {}.', 'воротнике', 'You have a little spot on your {}.', 'collar')\
        .end()\
        .lesson(7)\
            .word('браслет', 'браслеты', 'bracelet', 'bracelets')\
            .word('кольцо/2', 'кольца/2', 'ring', 'rings')\
            .word('серьга', 'серьги', 'earring', 'earrings')\
            .word('платок', 'платки', 'handkerchief', 'handkerchieves')\
            .word('молния', 'молнии', 'zipper', 'zippers')\
            .phrase('Мне нравится твоё {} с рубином.', 'кольцо', 'I like your {} with ruby.', 'ring')\
        .end()\
    .end()\