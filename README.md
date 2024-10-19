Labs on the subject of "Algorythms and data structures" (Алгоритмы и структуры данных АСД) 2-nd course

This ReadMe.md consists of:
- [Labs done](#Labs-done)
- - [Python](#Labs-done-python)
- - [C++](#Labs-done-c++)
- [Text of the lab](#Labs-text)
- [Explanation for each lab](#Explanation-labs)
- [Presentations from our lecturer](#Presentations)
- [Some extra things that I made](#Extra)

Крайне рекомендую от себя читать объяснения к лабам. Особенно те объяснения, что написаны мной вручную, те, где даны не только ссылки. Там информация изложена в максимально понятном ключе и должна достаточно просто восприниматься.
 
Если ссылка с выполненной лабы ведёт на объяснение лабы - просто почитайте там дальше, видимо, есть несколько вариантов её выполнения и дальше таам будут ссылки.

Labs of first semester have numeration 1-17.

Labs of second semester have numeration 18-???.

Currently I'm using English, but a bit later I'll use Russian, 'cause I don't care about those who don't know both of those languages.





<a name="Labs-done">

# Labs done
</a>
<a name="Labs-done-python">

### Python <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg"  title="Python" alt="Python" width="40" height="40"/>&nbsp;
</a>

1. [x] ["Задача о скобках"](#lab-1-explanation)
2. [x] ["Задача об арифметическом выражении"](/Semester_1/Labs/Lab2/Reversed_polish_notation.py)
3. [x] ["Задача о простых множителях"](/Semester_1/Labs/Lab3/lab_3.py)
4. [x] [Comb sort (Сортировка методом прочесывания)](/Semester_1/Labs/Lab4/comb_sort.py)
5. [x] [Insertion sort (Сортировка вставками)](/Semester_1/Labs/Lab5/insertion_sort.py)
6. [x] [Selection sort (Сортировка выбором)](/Semester_1/Labs/Lab6/selection_sort.py)
7. [x] [Shell sort (Сортировка Шелла)](/Semester_1/Labs/Lab7/shell_sort.py)
8. [x] [Radix sort (Поразрядная сортировка)](/Semester_1/Labs/Lab8/radix_sort.py)
9. [x] [Heap sort (Сортировка пирамидальная)](/Semester_1/Labs/Lab9/heap_sort.py)
10. [x] [Merge sort (Сортировка слиянием)](/Semester_1/Labs/Lab10/merge_sort.py)
11. [x] [QSort (Быстрая сортировка)](/Semester_1/Labs/Lab11/quick_sort.py)
12. [x] [External multiphase merge sort (Внешняя многофазная сортировка слиянием)](/Semester_1/Labs/Lab12/external_multiphase_sort.py)
13. [x] [Хэш-табоица с открытой адресацией](#lab-13-explanation)
14. [x] [Хэш-табоица со списками](#lab-14-explanation)
15. [x] [Рекурсивные обходы (прямой, центральный, концевой)](/Semester_1/Labs/Lab15/lab_15.py)
16. [x] [Не рекурсивный прямой обход](/Semester_1/Labs/Lab16/lab_16.py)
17. [x] [Операции над БНП: поиск, добавление, удаление](#lab-17-explanation)


<a name="Labs-done-c++">

### C++ <img src="https://github.com/devicons/devicon/blob/master/icons/cplusplus/cplusplus-original.svg"  title="Python" alt="Python" width="40" height="40"/>&nbsp;
</a>

1. [x] ["Задача о скобках"](/Semester_1/Labs/Lab2/lab_1.cpp)
2. [x] ["Задача об арифметическом выражении"](/Semester_1/Labs/Lab2/lab_2.cpp)
3. [x] ["Задача о простых множителях"](/Semester_1/Labs/Lab3/lab_3.cpp)
4. [x] [Comb sort (Сортировка методом прочесывания)](/Semester_1/Labs/Lab4/сomb_sort.cpp)
5. [x] [Insertion sort (Сортировка вставками)](/Semester_1/Labs/Lab5/insertion_sort.cpp)
6. [x] [Selection sort (Сортировка выбором)](/Semester_1/Labs/Lab6/selection_sort.cpp)
7. [x] [Shell sort (Сортировка Шелла)](/Semester_1/Labs/Lab7/shell_sort.cpp)
8. [x] [Radix sort (Поразрядная сортировка)](/Semester_1/Labs/Lab8/radix_sort.cpp)
9. [x] [Heap sort (Сортировка пирамидальная)](/Semester_1/Labs/Lab9/heap_sort.cpp)
10. [x] [Merge sort (Сортировка слиянием)](/Semester_1/Labs/Lab10/merge_sort.cpp)
11. [x] [QSort (Быстрая сортировка)](/Semester_1/Labs/Lab11/quick_sort.cpp)
12. [x] [External multiphase merge sort (Внешняя многофазная сортировка слиянием)](/Semester_1/Labs/Lab12/external_multiphase_sort.cpp)
13. [x] [Хэш-табоица с открытой адресацией](#lab-13-explanation)
14. [x] [Хэш-табоица со списками](#lab-14-explanation)
15. [x] [Рекурсивные обходы (прямой, центральный, концевой)](/Semester_1/Labs/Lab15/5.cpp)
16. [x] [Не рекурсивный прямой обход](/Semester_1/Labs/Lab16/16.cpp)
17. [ ] [Операции над БНП: поиск, добавление, удаление](/Semester_1/Labs/Lab17/17.cpp)





<a name="Labs-text">

# Text of the lab
</a>

[Вордовский документ с тем же текстом лаб](/docs//Zadania_1_semestr_2024-2025.docx)

### Первые задачки

1. "Задача о скобках"

(Задача состоит из двух пунктов, но вы можете не париться и делать сразу второй)
На вход подаётся строка, состоящая из скобок. Программа должна определить правильность введённого скобочного выражения. Савкин сказал, что программа должна работать на русском языке: "Введите строку", "Строка не существует", "Строка существует" и т.п.
Пункт 1: В строке будут скобки только одного типа: или "()" , или "{}", или "[]"
Пункт 2: В строке будут все три вида скобок
Для успешной сдачи лабы оба пункта программа должна выполнять корректно (можно сделать отдельные программы на каждый пункт)
Пример входа:
()[({}())]

2. "Задача об арифметическом выражении"

На вход подаётся математическое выражение. Элементы - числа. Операции - "+ - * /". Также есть скобочки. Окончанием выражения служит "=". Программа должна вывести результат выражения
Пример ввода:

2+7*(3/9)-5=

Замечание:
Программа также должна делать "проверку на дурака": нет деления на 0, все скобки стоят верно (см лабу №1) и т.п.

3. "Задача о простых множителях"

На вход дается одно число х, нужно вывести все числа от 1 до х, удовлетворяющие условию: 
'3**K * 5**L * 7**M = Xi'
где K, L, M - натуральные числа или могут быть равны 0.

### Сортировки

Дана последовательность чисел. Отсортировать и вывести последовательность чисел, определённым методом.

4. Сортировка методом прочесывания

5. Вставками

6. Посредством выбора

7. Шелла

8. Поразрядная

9. Пирамидальная (heap sort)

10. Слиянием

11. Быстрая

12. Внешняя многофазная


### Хэш-таблицы

Дан текстовый файл с некоторым текстом на русском или английском языках произвольной длины (организовать чтение). Выбрав некоторую хеш-функцию, создать хеш-таблицу с (**Имеется в виду принцип обхода коллизии**):

13. “с наложением” (**Имеется в виду с открытой адресацией**)
14. “со списками”

Таблицу записать в результирующий файл.

### Бинарные деревья

В качестве входной информации для следующих лабораторных работ  вводится символьная строка (бинарное дерево) с помощью линейно-скобочной записи. Например 8 (3 (1, 6 (4,7)), 10 (, 14(13,)))
Что соответствует

![Screenshot from file](/docs/images_for_readme/1.png)

Структура бинарного дерева создается с помощь динамических переменных.

15. “Рекурсивные обходы (прямой, центральный, концевой)”

16. “Не рекурсивный прямой обход” (реализуется с помощью стека).

В качестве выходных данных формируется строка обхода. Например:
![Screenshot from file](/docs/images_for_readme/2.png)

17. “Операции над БНП: поиск, добавление, удаление”

Дерево вводится в программу в формате линейно-скобочной записи. Затем появляется меню, в котором доступна операция добавления, удаления и поиска вершины БДП. После выполнения операции программа должна возвращаться снова в меню. При выходе их него до завершения программы на экран должно быть выведено БДН любым способом (в виде линейно-скобочной записи или в графической форме).





<a name="Explanation-labs">

# Explanation for each lab
</a>

Ссылки на мой код внутри объяснений буду давать на питоновские файлы. На плюсах не так обширно реализовывал всю эту фигню и просто больше материала на питоне получилось.

1. Используем [стэк](https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B5%D0%BA). Кладём туда открывающие скобочки по мере их поступления и убираем оттуда по одной последние, если встречаем нужную закрывающую. Переусложнённую версию смотреть [здесь](/Semester_1/Labs/Lab1/Lab_1.py). Навалено много синтаксического сахара, версию без наворотов смотреть [тут](/Semester_1/Labs/Lab1/Lab_1_simple.py). <a id="lab-1-explanation"></a>
2. Читаем на Википедии про [обратную польскую нотацию](https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D0%B0%D1%8F_%D0%BF%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B0%D1%8F_%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D1%8C) и вникаем.
3. Простой перебор по степеням с ограничением логарифмом. Это задача факторизации, если есть желание упороться и написать эффективно - [читаем](https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%BA%D1%82%D0%BE%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F_%D1%86%D0%B5%D0%BB%D1%8B%D1%85_%D1%87%D0%B8%D1%81%D0%B5%D0%BB).

Далее статьи могут быть на инглише, но вы его должны знать, если вы программист. Ну или у вас всегда есть под рукой переводчик.

### Сортировки

4. [Читаем](https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D1%80%D0%B0%D1%81%D1%87%D1%91%D1%81%D0%BA%D0%BE%D0%B9) 
5. [Читаем](https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D0%B2%D1%81%D1%82%D0%B0%D0%B2%D0%BA%D0%B0%D0%BC%D0%B8)
6. [Читаем](https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D0%B2%D1%8B%D0%B1%D0%BE%D1%80%D0%BE%D0%BC)
7. [Читаем](https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D0%A8%D0%B5%D0%BB%D0%BB%D0%B0)
8. [Читаем](https://thecode.media/radix/)
9. [Читаем](https://habr.com/ru/companies/otus/articles/460087/). [Heap](https://www.geeksforgeeks.org/binary-heap/) - специальная структура, бинарное дерево, у которого родительский жлемент всегда больше любого из дочерних. 
10. [Читаем](https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D1%81%D0%BB%D0%B8%D1%8F%D0%BD%D0%B8%D0%B5%D0%BC)
11. [Читаем](https://ru.wikipedia.org/wiki/%D0%91%D1%8B%D1%81%D1%82%D1%80%D0%B0%D1%8F_%D1%81%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0)
12. [Читаем](https://habr.com/ru/companies/otus/articles/712234/). Я этих формулировок труба шатал.


### Что такое хэш-таблица? <a name="lab-13-explanation"></a>

Больше объяснений [тут](/docs/HashTable.md)

 13. Open Adressing

 - - Linear-Probing on [<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg"  title="Python" alt="Python" width="15" height="15"/>](/Semester_1/Labs/Lab13/HashTable_linear_probing.py), [<img src="https://github.com/devicons/devicon/blob/master/icons/cplusplus/cplusplus-original.svg"  title="Python" alt="Python" width="17" height="17"/>](Semester_1/Labs/Lab13/HashTable_linear_probing.cpp) - Значения при возникновении коллизии кладутся в следующие ячейки до тех пор, пока коллизий не будет. Ищется по такому же принципу (т.е. до тех пор, пока не найдём значение в следующих ячейках или пока следующая ячейка не будет пустой)

 - - Quadratic-Probing on [<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg"  title="Python" alt="Python" width="17" height="17"/>](/Semester_1/Labs/Lab13/HashTable_quadratic_probing.py), [<img src="https://github.com/devicons/devicon/blob/master/icons/cplusplus/cplusplus-original.svg"  title="Python" alt="Python" width="17" height="17"/>](Semester_1/Labs/Lab13/HashTable_quadratic_probing.cpp) - Значения при возникновении коллизии кладутся в следующие ячейки по принципу "сначала прибавим квадрат единички, потом сверху квадрат двойки, потом квадрат тройки и т.д." до тех пор, пока коллизий не будет. Ищется по такому же принципу (т.е. до тех пор, пока не найдём значение в следующих ячейках или пока следующая найденная подобным образом ячейка не будет пустой)

 - - Double-Hashing on [<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg"  title="Python" alt="Python" width="17" height="17"/>](/Semester_1/Labs/Lab13/HashTable_double_hashing.py), [<img src="https://github.com/devicons/devicon/blob/master/icons/cplusplus/cplusplus-original.svg"  title="Python" alt="Python" width="17" height="17"/>](Semester_1/Labs/Lab13/HashTable_double_hashing.cpp) - !!!Найдена ошмбка в алгоритме при одном из крайних случаев, в процессе исправления. Если хотите помочь - кидайте пулл-реквест!!! Сложнее. У нас есть вторая хэш-функция. Значения при возникновении коллизии кладутся в следующие ячейки по принципу "будет домножать хэш-код номер 2 на номер нашей попытки положить значение в следующую ячейку и пытаться класть его снова до тех пор, пока в конечном итоге не получится". Ищется по такому же принципу.

<a name="lab-14-explanation"></a>

*[статья на хабре, на которой есть всё про последующие лабы. Кажется,я знаю, откуда брали задания...](https://habr.com/ru/articles/267855/)*

 14. Chain method on [<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg"  title="Python" alt="Python" width="17" height="17"/>](/Semester_1/Labs/Lab14/HashTable_separate_chaining.py), [<img src="https://github.com/devicons/devicon/blob/master/icons/cplusplus/cplusplus-original.svg"  title="Python" alt="Python" width="17" height="17"/>](Semester_1/Labs/Lab14/HashTable_separate_chaining.cpp) - Коллизия - это лишь обман вашего восприятия. Если возникает коллизия - пф, не проблема. У нас заранее обозначено, что в ячейках лежат не просто значения, а "узлы", имеющие два параметра - собственное значение и указатель на следующий элемент. Теперь при возникновении колизии мы просто идём по своеобразному односвязному списку узлов до тех пор, пока указатель на следующий узел не будет нульпоинтером и добавляем новый узел. Поиск производится так же, нахождением списка элементов с данным хэш-кодом и пробегом по этому списку до тех пор, пока не найдём \ поймём, что не нашли нужный нам элемент. С некоторыми дополнительными методами типа `len()` и `__str__()` тут по сложнее. Я написал `@property`-методы (методы, заменяющие алгоритм получения каких-то собстевнных свойств класса) для получения сразу всех ключей и пар индекс-ключ на работающие за O(n). Зато работающие.

15. Рекурсивные обходы. Что говорить? Дерево состоит из узлов. Начиная с корневого узла прсото либо сначала печатаем, потом переходим к левому узлу в рекрсии, потом к правому в рекрсии. Либо сначала переходим к левым узлам рекурсивно, потом печатаем, потом к правым. Либо сначала к левым, потом к правым, потом печатаем. 

Интересный алгоритм ([<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg"  title="Python" alt="Python" width="17" height="17"/>](/Extra_things/BT_reader.py), [<img src="https://github.com/devicons/devicon/blob/master/icons/cplusplus/cplusplus-original.svg"  title="Python" alt="Python" width="17" height="17"/>](/Extra_things/BT_reader.cpp)) пришлось написать для чтения линейно-скобочной записи, но комментировать особо нечего, надо смотреть.

16. Для того, чтобы нерекурсивно пройти бинарное дерево можно просто взять стэк, проходить только по правым или левым узлам, и, соответственно, левые или правые узлы, которые увидели у родительских жлементов добавлять в стэк. А после каждого обхода возвращаться к стэку и начинать опять обход от него.

<a name="lab-17-explanation"></a>

17. Тут всё просто. [Читаем](https://ru.wikipedia.org/wiki/%D0%94%D0%B2%D0%BE%D0%B8%D1%87%D0%BD%D0%BE%D0%B5_%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%BE_%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0) про BST, смотрим код. Методы реализованы рекурсивно. Для лабы достаточно сдать то, тчо есть в [lab_17_simple.py](/Semester_1/Labs/Lab17/lab_17_simple.py) или [17.cpp](/Semester_1/Labs/Lab17/17.cpp), [lab_17.py](/Semester_1/Labs/Lab17/lab_17.py) - жуткий оверкилл, включающий в себя содержание лаб 15-16, а также в будущем алгоритм красивого вывода бинарного дерева.
 




<a name="Presentations">

# Presentations from our lecturer
</a>

- [Введение (зачем???)](/docs/Lektsia_1_Vvedenie.pptx)
- [Введение в структуры данных](/docs/Lektsia_2_Struktury_dannykh.pptx)
- [Виды сортировок + псевдокод к ним (господи, я искал эту хрень месяц, а потом он просто скинул эту презентацию бл#$&!)](/docs/Lektsia_3-4-5_Sortirovki.pptx)
- [Хэш-таблицы (HashTables)](/docs/Lektsia_6_Khesh-tablitsy.pptx)
<!-- - [Деревья (Binary Tree)](/docs/) -->
<!-- - [Бинарные деревья поиска (Binary Search Tree, BST)](/docs/) -->





<a name="Extra">

# Some extra things that I wrote here
</a>
Гуляя по репозиторию Вы можете наткнуться на различную фигню, которую я для себя сделал, но которая точно, прямо 100%, прямо прямо да, стоила затраченных усчтвенных сил, времени и нервов. Пройдёмся немного по подобным штукам:

- [Файл с автоматическими тестами](/Semester_1/Tests/sorting_tests.py) 

Просто мне было лень придумывать примеры, поэтому я написал простенькие функции для тестирования кода в автоматическом формате, с генерацией тестов, замером времени, возможностью изменять параметры тестирования и красивым выводом в консоль. Запускаются тесты через [run_file.py](/Semester_1/sorting_run_file.py), а в [test_logs.txt](/Semester_1/Tests/test_logs.txt) сохраняются результаты проверок в случае, если тест был длиннее пары чисел.


- [Файл с автоматичесим тестированием хэш-таблицы](/Semester_1/hastables_tests.py) 

Простой тест чисто по заданию. Увы, не хотелось пока что-то большее писать.


- [Визуализатор распределения ключей для хэш-таблицы](/Extra_things/hash_distribution.py)

Помог бы сделать свою хэш-функцию, так как если покрутить - хорошо показывает распределение. [Вот отсюда](https://realpython.com/python-hash-table/#hash-table-vs-dictionary) взял, понравилось, решил оставить после написания лабы.



- Ридеры (как их назвать?) бинарных деревьев ([<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg"  title="Python" alt="Python" width="17" height="17"/>](/Extra_things/BT_reader.py), [<img src="https://github.com/devicons/devicon/blob/master/icons/cplusplus/cplusplus-original.svg"  title="Python" alt="Python" width="17" height="17"/>](/Extra_things/BT_reader.cpp))

Переводят линейно-скобочную запись (нотацию) в построенное бинарное дерево. Используется в лабах 15-16, 17 (опционально).


- [Функция красивого вывода любого (бинарного или нет) дерева](/Extra_things/tree_printer.py)

Взял со [StackOverFlow](https://stackoverflow.com/questions/15675261/displaying-a-tree-in-ascii), переписал и залил. Самому уже было лень писать, когда готовился 17-ую лабу в октябре сдавать, решил всё же переделать готовый алгоритм. Пока переписываю.


- [Односвязный список](/Extra_things/Single-linked%20list/)

Была у нас на первом курсе [лаба по плюсам](https://github.com/RomanRudin/bfu_cpp_labs/tree/main/Semester_1/Advanced/8.%20Single-linked%20list)... Вот тогда написал. А тут по теме подходит, просто так сюда добавил.


- [Двусвязный список](/Extra_things/Double-linked%20lists/)

Двусвязный список из [лабы по плюсам первго](https://github.com/RomanRudin/bfu_cpp_labs/tree/main/Semester_1/Advanced/9.%20Double-linked%20lists) курса 2023 года.


- [Если вдруг когда-то решусь писать своё дерево](/Extra_things/NonBinary%20Tree/)

Если вдруг когда-то решусь писать своё дерево.


- [Если вдруг когда-то решусь писать своИ стэк и очередь](/Extra_things/Stack%20and%20queue/)

Если вдруг когда-то решусь писать своИ стэк и очередь.