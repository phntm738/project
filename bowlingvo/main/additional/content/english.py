from .. import content_filler

def main():
    LanguageContent = content_filler.LanguageContent
    content_filler.LANG = 'english'

    eng = LanguageContent('Английский', 'english')
    eng.section('Еда', 'food')\
        .lesson(1)\
            .word('завтрак', 'завтраки', 'breakfast', 'breakfasts')\
            .word('хлеб', 'хлеба', 'bread', 'bread')\
            .word('сыр', 'сыры', 'cheese', 'cheeses')\
            .word('сливочное масло', 'сливочное масло', 'butter', 'butter')\
            .word('йогурт', 'йогурты', 'yoghurt', 'yoghurts')\
            .phrase('Я ем на завтрак тост и {}.', 'сыр', 'I eat a toast and {} for breakfast.', 'cheese')\
            .phrase('Мой брат любит персиковый {}.', 'йогурт', 'My brother likes peach {}.', 'yoghurt')\
            .phrase('{} - важный приём пищи.', 'Завтрак', '{} is an important meal.', 'Breakfast')\
        .end()\
        .lesson(2)\
            .word('чай', 'чаи', 'tea', 'teas')\
            .word('кофе', 'кофе', 'coffee', 'coffee')\
            .word('молоко', 'молоко', 'milk', 'milk')\
            .word('хлопья', 'хлопья', 'cereals', 'cereals')\
            .word('сахар', 'сахар', 'sugar', 'sugar')\
            .phrase('Я не пью {} с молоком.', 'чай', 'I don\'t drink {} with milk.', 'tea')\
            .phrase('Ты ешь {} на завтрак?', 'хлопья', 'Do you have {} for breakfast?', 'cereals')\
        .end()\
        .lesson(3)\
            .word('десерт', 'десерты', 'dessert', 'desserts')\
            .word('торт', 'торты', 'cake', 'cakes')\
            .word('печенье', 'печенья', 'biscuit', 'biscuits')\
            .word('блин', 'блины', 'pancake', 'pancakes')\
            .word('пирог', 'пироги', 'pie', 'pies')\
            .phrase('Я люблю есть {} на завтрак.', 'блины', 'I like eating {} for breakfast.', 'pancakes')\
        .end()\
        .lesson(4)\
            .word('мороженое', 'мороженое', 'ice cream', 'ice cream')\
            .word('варенье', 'варенья', 'jam', 'jams')\
            .word('мёд', 'мёд', 'honey', 'honey')\
            .word('сметана', 'сметана', 'sour cream', 'sour cream')\
            .word('конфета', 'конфеты', 'candy', 'candies')\
            .phrase('Какой вкус {} твой любимый?', 'мороженого', 'What is your favourite {} flavour?', 'ice cream')\
        .end()\
        .lesson(5)\
            .word('обед', 'обеды', 'supper', 'suppers')\
            .word('ужин','ужины', 'dinner', 'dinners')\
            .word('салат', 'салаты', 'salad', 'salads')\
            .word('сок', 'соки', 'juice', 'juices')\
            .word('стейк', 'стейки', 'steak', 'steaks')\
            .phrase('Меня пригласили на {} к Роббинсонам.', 'ужин', 'I\'ve been invited for a {} with Robbinsons', 'dinner')\
            .phrase('Я не очень люблю {}, но мне нравятся стейки.', 'салаты', 'I\'m not fond of {}, but I like steaks.', 'salads')\
            .phrase('Вы бы хотели немного {}?', 'сока', 'Would you like some {}?', 'juice')\
        .end()\
        .lesson(6)\
            .word('фрукт', 'фрукты', 'fruit', 'fruits')\
            .word('яблоко', 'яблоки', 'apple', 'apples')\
            .word('апельсин', 'апельсины', 'orange', 'oranges')\
            .word('груша', 'груши', 'pear', 'pears')\
            .word('лимон', 'лимоны', 'lemon', 'lemons')\
            .phrase('Какой твой любимый {}?', 'фрукт', 'What is your favourite {}?', 'fruit')\
            .phrase('Это {} очень кислое.', 'яблоко', 'This {} is very sour.', 'apple')\
            .phrase('{} - мой любимый фрукт.', 'Груша', '{} is my favourite fruit.', 'Pear')\
        .end()\
        .lesson(7)\
            .word('персик', 'персики', 'peach', 'peaches')\
            .word('банан', 'бананы', 'banana', 'bananas')\
            .word('слива', 'сливы', 'plum', 'plums')\
            .word('абрикос', 'абрикосы', 'apricot', 'apricots')\
            .word('ананас', 'ананасы', 'pineapple', 'pineapples')\
            .phrase('{} выращивают на юге.', 'Бананы', '{} are grown in the south.', 'Bananas')\
            .phrase('В этой пицце есть {}.', 'ананасы', 'There are {} in this pizza.', 'pineapples')\
            .phrase('Ты будешь {} или сливу?', 'персик', 'Will you take a {} or a plum?', 'peach')\
        .end()\
        .lesson(8)\
            .word('ложка', 'ложки', 'spoon', 'spoons')\
            .word('вилка', 'вилки', 'fork', 'forks')\
            .word('нож', 'ножи', 'knife', 'knifes')\
            .word('тарелка', 'тарелки', 'plate', 'plates')\
            .word('чашка', 'чашки', 'cup', 'cups')\
            .phrase('Я буду {} чая.', 'чашку', 'I would like a {} of tea.', 'cup')\
            .phrase('Передайте мне {}, пожалуйста.', 'нож', 'Pass me the {}, please.', 'knife')\
            .phrase('Добавьте столовую {} муки.', 'ложку', 'Add a table {} of flour.', 'spoon')\
            .phrase('Используй {} и нож.', 'вилку', 'Use a {} and a knife.', 'fork')\
        .end()\
        .lesson(9)\
            .word('овощ', 'овощи', 'vegetable', 'vegetables')\
            .word('помидор', 'помидоры', 'tomato', 'tomatoes')\
            .word('картофель', 'картофель', 'potato', 'potatoes')\
            .word('морковь', 'морковь', 'carrot', 'carrots')\
            .word('огурец', 'огурцы', 'cucumber', 'cucumbers')\
            .phrase('Ты любишь {}?', 'овощи', 'Do you like {}?', 'vegetables')\
            .phrase('{} оранжевая, а огурец зелёный', 'Морковь', '{} is orange and cucumber is green', 'Carrot')\
        .end()\
        .lesson(10)\
            .word('капуста', 'капуста', 'cabbage', 'cabbages')\
            .word('сельдерей', 'сельдерей', 'celery', 'celeries')\
            .word('тыква', 'тыквы', 'pumpkin', 'pumpkins')\
            .word('перец', 'перцы', 'pepper', 'peppers')\
            .word('соль', 'соль', 'salt', 'salt')\
            .phrase('Ты добавил {} в воду?', 'соль', 'Did you put {} in water?', 'salt')\
            .phrase('Я не люблю {}, а ты?', 'сельдерей', 'I don\'t like {}, and you?', 'celery')\
            .phrase('Она забыла купить {}.', 'перец', 'She forgot to buy a {}.', 'pepper')\
        .end()\
        .lesson(11)\
            .word('мука', 'мука', 'flour', 'flour')\
            .word('рис', 'рис', 'rice', 'rice')\
            .word('паста', 'паста', 'pasta', 'pasta')\
            .word('лапша', 'лапша', 'noodles', 'noodles')\
            .word('орех', 'орехи', 'nut', 'nuts')\
            .phrase('Надо купить {} и соль.', 'рис', 'We need to buy {} and salt.', 'rice')\
            .phrase('На ужин у нас {}.', 'паста', 'We have {} for dinner.', 'pasta')\
        .end()\
        .lesson(12)\
            .word('пшеница', 'пшеница', 'wheat', 'wheat')\
            .word('кукуруза', 'кукуруза', 'corn', 'corn')\
            .word('овёс', 'овёс', 'oat', 'oat')\
            .word('гречка', 'гречка', 'buckwheat', 'buckwheat')\
            .word('пшено', 'пшено', 'millet', 'millet')\
            .phrase('Где выращивают {}?', 'пшеницу', 'Where is {} grown?', 'wheat')\
        .end()\
        .lesson(13)\
            .word('рыба', 'рыбы', 'fish', 'fishes')\
            .word('тунец', 'тунцы', 'tuna', 'tuna')\
            .word('креветка', 'креветки', 'shrimp', 'shrimps')\
            .word('лосось', 'лосось', 'salmon', 'salmon')\
            .word('форель', 'форель', 'trout', 'trout')\
            .phrase('Лосось - морская {}?', 'рыба', 'Is salmon a sea {}?', 'fish')\
        .end()\
        .lesson(14)\
            .word('говядина', 'говядина', 'beef', 'beef')\
            .word('ветчина', 'ветчина', 'ham', 'ham')\
            .word('баранина', 'баранина', 'mutton', 'mutton')\
            .word('свинина', 'свинина', 'pork', 'pork')\
            .word('курятина', 'курятина', 'chicken', 'chicken')\
            .phrase('У вас есть {} и сыр?', 'ветчина', 'Do you have {} and cheese?', 'ham')\
        .end()\
        .lesson(15)\
            .word('пицца', 'пиццы', 'pizza', 'pizzas')\
            .word('сосиска', 'сосиски', 'sausage', 'sausages')\
            .word('каша', 'каши', 'porridge', 'porridges')\
            .word('специя', 'специи', 'spice', 'spices')\
            .word('чеснок', 'чеснок', 'garlic', 'garlic')\
            .phrase('{} отпугивает вампиров.', 'Чеснок', '{} scares off vampires.', 'Garlic')\
            .phrase('Купи в магазине {}.', 'сосиски', 'Buy some {} in the shop.', 'sausages')\
        .end()\
        .lesson(16)\
            .word('соус', 'соусы', 'sauce', 'sauces')\
            .word('кетчуп', 'кетчупы', 'ketchup', 'ketchups')\
            .word('майонез', 'майонезы', 'mayonnaise', 'mayonnaises')\
            .word('уксус', 'уксусы', 'vinegar', 'vinegars')\
            .word('горчица', 'горчицы', 'mustard', 'mustards')\
            .phrase('Я буду картофель с сырным {}.', 'соусом', 'I\'d like french fries with cheese {}.', 'sauce')\
        .end()\
        .lesson(17)\
            .word('вкус', 'вкусы', 'taste', 'tastes')\
            .word('сладкий', 'сладкие', 'sweet', 'sweet')\
            .word('солёный', 'солёные', 'salty', 'salty')\
            .word('кислый', 'кислые', 'sour', 'sour')\
            .word('горький', 'горькие', 'bitter', 'bitter')\
            .word('острый', 'острые', 'spicy', 'spicy')\
            .word('пресный', 'пресные', 'insipid', 'insipid')\
            .phrase('Этот суп {}, ты добавил соль?', 'пресный', 'This soup is {}, did you add salt?', 'insipid')\
        .end()\
    .end()\
    .section('Город', 'city')\
        .lesson(1)\
            .word('город', 'города', 'city', 'cities')\
            .word('городок', 'городки', 'town', 'towns')\
            .word('дорога', 'дороги', 'road', 'roads')\
            .word('здание', 'здания', 'building', 'buildings')\
            .word('столица', 'столицы', 'capital', 'capitals')\
            .phrase('Давай заедем в мой любимый {}.', 'городок', 'Let\'s visit my favourite {}.', 'town')\
        .end()\
        .lesson(2)\
            .word('улица', 'улицы', 'street', 'streets')\
            .word('проспект', 'проспекты', 'avenue', 'avenues')\
            .word('площадь', 'площади', 'square', 'squares')\
            .word('квартал', 'кварталы', 'block', 'blocks')\
            .word('район', 'районы', 'district', 'districts')\
            .phrase('Пройдите этот {} и поверните налево.', 'квартал', 'Go through this {} and turn left.', 'block')\
            .phrase('Этот {} проходит через весь город с севера на юг.', 'проспект', 'This {} goes through the whole city from north to south.', 'avenue')\
        .end()\
        .lesson(3)\
            .word('пекарня', 'пекарни', 'bakery', 'bakeries')\
            .word('продуктовый магазин', 'продуктовые магазины', 'grocery', 'groceries')\
            .word('мясной магазин', 'мясные магазины', 'butcher\'s shop', 'butcher\'s shops')\
            .word('супермаркет', 'супермаркеты', 'supermarket', 'supermarkets')\
            .word('торговый центр', 'торговые центры', 'shopping mall', 'shopping malls')\
            .word('кафе', 'кафе', 'cafe', 'cafes')\
            .phrase('По дороге домой они зашли в {}.', 'торговый центр', 'On the way back home they visited a {}.', 'shopping mall')\
        .end()\
        .lesson(4)\
            .word('школа', 'школы', 'school', 'schools')\
            .word('больница', 'больницы', 'hospital', 'hospitals')\
            .word('театр', 'театры', 'theatre', 'theatres')\
            .word('кинотеатр', 'кинотеатры', 'cinema', 'cinemas')\
            .word('галерея', 'галереи', 'art gallery', 'art galleries')\
            .phrase('Давай сходим в {}.', 'театр', 'Let\'s go to the {}.', 'theatre')\
        .end()\
        .lesson(5)\
            .word('аптека', 'аптеки', 'pharmacy', 'pharmacies')\
            .word('почта', 'почты', 'post office', 'post offices')\
            .word('библиотека', 'библиотеки', 'library', 'libraries')\
            .word('церковь', 'церкви', 'church', 'churches')\
            .word('мечеть', 'мечети', 'mosque', 'mosques')\
            .phrase('На нашей улице недавно открылась {}.', 'библиотека', 'A {} has opened on our street recently.', 'library')\
            .phrase('{} находится за углом.', 'Аптека', 'The {} is around the corner.', 'pharmacy')\
        .end()\
        .lesson(6)\
            .word('клуб', 'клубы', 'club', 'clubs')\
            .word('вокзал', 'вокзалы', 'railway station', 'railway stations')\
            .word('аэропорт', 'аэропорты', 'airport', 'airports')\
            .word('банк', 'банки', 'bank', 'banks')\
            .word('музей', 'музеи', 'museum', 'museums')\
            .word('ресторан', 'рестораны', 'restaurant', 'restaurants')\
            .phrase('Где находится вегетарианский {}?', 'ресторан', 'Where is a vegetarian {}?', 'restaurant')\
        .end()\
        .lesson(7)\
            .word('кладбище', 'кладбища', 'graveyard', 'graveyard')\
            .word('отель', 'отели', 'hotel', 'hotels')\
            .word('река', 'реки', 'river', 'rivers')\
            .word('мост', 'мосты', 'bridge', 'bridges')\
            .word('набережная', 'набережные', 'embankment', 'embankments')\
            .phrase('{} Темзы - очень красивое место.', 'Набережная', 'The Thames {} is a beautiful place.', 'embankment')\
            .phrase('Какая {} протекает через Эдинбург?', 'река', 'What {} flows through Edinburgh?', 'river')\
        .end()\
        .lesson(8)\
            .word('цирк', 'цирки', 'circus', 'circuses')\
            .word('дворец', 'дворцы', 'palace', 'palaces')\
            .word('книжный магазин', 'книжные магазины', 'bookstore', 'bookstores')\
            .word('кондитерская', 'кондитерская', 'confectionery', 'confectioneries')\
            .word('парк', 'парки', 'park', 'parks')\
            .phrase('Какой {} самый известный?', 'парк', 'What {} is the most famous?', 'park')\
        .end()\
        .lesson(9)\
            .word('аллея', 'аллеи', 'alley', 'alleys')\
            .word('пешеходный переход', 'пешеходные переходы', 'crosswalk', 'crosswalks')\
            .word('светофор', 'светофоры', 'traffic light', 'traffic lights')\
            .word('фонарь', 'фонари', 'lantern', 'lanterns')\
            .word('фонтан', 'фонтаны', 'fountain', 'fountains')\
            .phrase('Эта {} проходит через центр города.', 'аллея', 'This {} goes through the centre of the city.', 'alley')\
        .end()\
        .lesson(10)\
            .word('поворот', 'повороты', 'turn', 'turns')\
            .word('перекрёсток', 'перекрёстки', 'crossroad', 'crossroads')\
            .word('забор', 'заборы', 'fence', 'fences')\
            .word('тротуар', 'тротуары', 'sidewalk', 'sidewalks')\
            .word('ворота', 'ворота', 'gate', 'gates')\
            # .phrase('', '', '', '')\
        .end()\
        .lesson(11)\
            .word('вход', 'входы', 'entrance', 'entrances')\
            .word('выход', 'выходы', 'exit', 'exits')\
            .word('рекламный щит', 'рекламные щиты', 'billboard', 'billboards')\
            .word('сад', 'сады', 'garden', 'gardens')\
            .word('бульвар', 'бульвары', 'boulevard', 'boulevards')\
            .phrase('Где находится {} в метро?', 'вход', 'Where is the subway {}?', 'entrance')\
        .end()\
        .lesson(12)\
            .word('шоссе', 'шоссе', 'highway', 'highways')\
            .word('парковка', 'парковки', 'parking', 'parkings')\
            .word('центр города', 'центры города', 'downtown', 'downtowns')\
            .word('жилые кварталы города', 'жилые кварталы города', 'uptown', 'uptowns')\
            .word('жилой район', 'жилые районы', 'residental area', 'residental areas')\
            .phrase('В центре города {} платная.', 'парковка', '{} in the downtown is paid.', 'Parking')\
            .phrase('{} позволяют быстрее выехать из города.', 'Шоссе', '{} allow to leave the city faster.', 'Highways')\
        .end()\
        .lesson(13)\
            .word('округ', 'округи', 'district/2', 'districts/2')\
            .word('пригород', 'пригороды', 'suburb', 'suburbs')\
            .word('пригородный поезд', 'пригородные поезда', 'local train', 'local trains')\
            .word('сельская местность', 'сельская местность', 'countryside', 'countryside')\
            .word('деревня', 'деревни', 'village', 'villages')\
            .phrase('Париж поделён на двадцать {}.', 'округов', 'Paris is divided into twenty {}.', 'districts')\
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
            .word('ворота', 'ворота', 'goal', 'goals')\
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
            .word('жакет', 'жакеты', 'jacket', 'jackets')\
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
            .word('кольцо', 'кольца', 'ring', 'rings')\
            .word('серьга', 'серьги', 'earring', 'earrings')\
            .word('платок', 'платки', 'handkerchief', 'handkerchieves')\
            .word('молния', 'молнии', 'zipper', 'zippers')\
            .phrase('Мне нравится твоё {} с рубином.', 'кольцо', 'I like your {} with ruby.', 'ring')\
        .end()\
    .end()\
    .section('Животные', 'animals')\
        .lesson(1)\
            .word('животное', 'животные', 'animal', 'animals')\
            .word('домашний', 'домашний', 'domestic', 'domestic')\
            .word('дикий', 'дикий', 'wild', 'wild')\
            .word('враждебный', 'враждебный', 'hostile', 'hostile')\
            .word('скот', 'скот', 'cattle', 'cattle')\
            .phrase('Медведь - {} зверь.', 'враждебный', 'Bear is a {} beast.', 'hostile')\
        .end()\
        .lesson(2)\
            .word('кот', 'коты', 'cat', 'cats')\
            .word('котёнок', 'котята', 'kitten', 'kittens')\
            .word('собака', 'собаки', 'dog', 'dogs')\
            .word('щенок', 'щенята', 'puppy', 'puppies')\
            .word('кролик', 'кролики', 'rabbit', 'rabbits')\
            .phrase('Я боюсь, что {} меня покусает.', 'собака', 'I\'m afraid, that {} will bite me.', 'dog')\
        .end()\
        .lesson(3)\
            .word('курица', 'курицы', 'chicken', 'chicken')\
            .word('корова', 'коровы', 'cow', 'cows')\
            .word('лошадь', 'лошади', 'horse', 'horses')\
            .word('свинья', 'свиньи', 'pig', 'pigs')\
            .word('овца', 'овцы', 'sheep', 'sheep')\
            .phrase('На этой ферме разводят {}.', 'коров', '{} are raised on this farm.', 'Cows')\
        .end()\
        .lesson(4)\
            .word('утка', 'утки', 'duck', 'ducks')\
            .word('осёл', 'ослы', 'donkey', 'donkeys')\
            .word('коза', 'козы', 'goat', 'goats')\
            .word('бык', 'быки', 'bull', 'bulls')\
            .word('индейка', 'индейки', 'turkey', 'turkeys')\
            .phrase('Посмотри, какая славная {}!', 'утка', 'Look, what a nice {}!', 'duck')\
        .end()\
        .lesson(5)\
            .word('заяц', 'зайцы', 'hare', 'hares')\
            .word('лиса', 'лисы', 'fox', 'foxes')\
            .word('волк', 'волки', 'wolf', 'wolves')\
            .word('медведь', 'медведи', 'bear', 'bears')\
            .word('олень', 'олени', 'deer', 'deers')\
            .phrase('{} зимой меняют цвет своей шерсти.', 'Зайцы', '{} change their coat color in winter.', 'Hares')\
        .end()\
        .lesson(6)\
            .word('тигр', 'тигры', 'tiger', 'tigers')\
            .word('лев', 'львы', 'lion', 'lions')\
            .word('обезьяна', 'обезьяны', 'monkey', 'monkeys')\
            .word('жираф', 'жирафы', 'giraffe', 'giraffes')\
            .word('носорог', 'носороги', 'rhino', 'rhinos')\
            .phrase('{} имеет очень длинную шею.', 'Жираф', '{} has a very long neck.', 'Giraffe')\
        .end()\
        .lesson(7)\
            .word('белка', 'белки', 'squirrel', 'squirrels')\
            .word('ёж', 'ежи', 'hedgehog', 'hedgehogs')\
            .word('енот', 'еноты', 'raccoon', 'raccoons')\
            .word('мышь', 'мыши', 'mouse', 'mice')\
            .word('крыса', 'крысы', 'rat', 'rats')\
            .phrase('{} съели всё зерно.', 'Мыши', '{} ate all the grain.', 'Mice')\
        .end()\
        .lesson(8)\
            .word('верблюд', 'верблюды', 'camel', 'camels')\
            .word('слоны', 'слоны', 'elephant', 'elephants')\
            .word('зебра', 'зебры', 'zebra', 'zebras')\
            .word('млекопитающее', 'млекопитающие', 'mammal', 'mammals')\
            .word('порода', 'породы', 'breed', 'breeds')\
            .phrase('Какая {} у этой собаки?', 'порода', 'What is this dog\'s {}?', 'breed')\
        .end()\
