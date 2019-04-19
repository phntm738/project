from .. import content_filler

def main():
    LexContent = content_filler.LexContent
    GramContent = content_filler.GramContent
    content_filler.LANG = 'spanish'

    span_lex = LexContent('Испанский', 'spanish')
    span_lex.section('Еда', 'food')\
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
    .section('Город', 'city')\
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
            .word('транспорт', 'транспорт', 'el transporte', 'el transporte')\
            .word('автобус', 'автобусы', 'el autobus', 'los autobuses')\
            .word('трамвай', 'трамваи', 'el tranvía', 'los tranvías')\
            .word('поезд', 'поезда', 'el tren', 'los trenes')\
            .phrase('Этот {} опаздывает.', 'поезд', 'Este {} llega tarde', 'tren')\
            .phrase('{} 12 идёт до музея?', 'Трамвай', 'Va el {} 12 al museo?', 'tranvía')\
        .end()\
        .lesson(2)\
            .word('машина', 'машины', 'el coche', 'los coches')\
            .word('такси', 'такси', 'el taxi', 'los taxis')\
            .word('велосипед', 'велосипеды', 'la bicicleta', 'la bicicletas')\
            .word('мотоцикл', 'мотоциклы', 'la motocicleta', 'las motocicletas')\
            .word('грузовик', 'грузовики', 'el camion', 'los camiones')\
            .phrase('До центра можно добраться на {} или метро.', 'такси', 'Se puede llegar al centro en {} o metro.', 'taxi')\
        .end()\
        .lesson(3)\
            .word('метро', 'метро', 'el metro', 'el metro')\
            .word('станция', 'станции', 'la estacion', 'las estationes')\
            .word('остановка', 'остановки', 'la parada', 'las paradas')\
			.word('пассажир', 'пассажиры', 'el pasajero', 'los pasajeros')\
            .phrase('{} московского метро очень красивые.', 'Станции', 'Las {} del metro de Moscú son muy bonitas.', 'estaciones')\
        .end()\
        .lesson(4)\
            .word('лодка', 'лодки', 'el bote', 'los bote`s')\
            .word('корабль', 'корабли', 'el barco', 'los barcos')\
            .word('самолёт', 'самолёты', 'el avion', 'los aviones')\
            .word('вертолёт', 'вертолёты', 'el helicoptero', 'los helicopteros')\
            .phrase('{} причалил к пристани.', 'Корабль', 'El {} amarrado al muelle.', 'barco')\
        .end()\