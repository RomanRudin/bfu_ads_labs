Labs on the subject of "Algorythms and data structures" (Алгоритмы и структуры данных АСД) 2-nd course

This ReadMe.md consists of:
- [Labs done](#Labs-done)
- - [Python](#Labs-done-python)
- - [C++](#Labs-done-c++)
- [Text of the lab](#Labs-text)
- [Explanation for each lab](#Explanation-labs)
- [Presentations from our lecturer](#Presentations)
- [Some explanation of extra things that I made](#Explanation-extra)
 
Labs of first semester have numeration 1-17.

Labs of second semester have numeration 18-???.

Currently I'm using English, but a bit later I'll use Russian, 'cause I don't care about those who doesn't know both of those languages.





<a name="Labs-done">

# Labs done
</a>
<a name="Labs-done-python">

### Python <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg"  title="Python" alt="Python" width="40" height="40"/>&nbsp;
</a>

1. [x] ["Задача о скобках"](/Semester_1/Labs/Lab1/lab_1.py)
2. [x] ["Задача об арифметическом выражении"](/Semester_1/Labs/Lab2/lab_2.py)
3. [x] ["Задача о простых множителях"](/Semester_1/Labs/Lab3/lab_3.py)
4. [x] [Comb sort (Сортировка методом прочесывания)](/Semester_1/Labs/Lab4/lab_4.py)
5. [x] [Insertion sort (Сортировка вставками)](/Semester_1/Labs/Lab5/lab_5.py)
6. [x] [Selection sort (Сортировка выбором)](/Semester_1/Labs/Lab6/lab_6.py)
7. [x] [Shell sort (Сортировка Шелла)](/Semester_1/Labs/Lab7/lab_7.py)
8. [x] [Radix sort (Поразрядная сортировка)](/Semester_1/Labs/Lab8/lab_8.py)
9. [x] [Heap sort (Сортировка пирамидальная)](/Semester_1/Labs/Lab9/lab_9.py)
10. [x] [Merge sort (Сортировка слиянием)](/Semester_1/Labs/Lab10/lab_10.py)
11. [x] [QSort (Быстрая сортировка)](/Semester_1/Labs/Lab11/lab_11.py)
12. [ ] [External multiphase merge sort (Внешняя многофазная сортировка слиянием)](/Semester_1/Labs/Lab12/lab_12.py)
13. [ ] [Хэш-табоица с открытой адресацией](/Semester_1/Labs/Lab13/lab_13.py)
14. [ ] [Хэш-табоица со списками](/Semester_1/Labs/Lab14/lab_14.py)
15. [ ] [Рекурсивные обходы (прямой, центральный, концевой)](/Semester_1/Labs/Lab15/lab_15.py)
16. [ ] [Не рекурсивный прямой обход](/Semester_1/Labs/Lab16/lab_16.py)
17. [ ] [Операции над БНП: поиск, добавление, удаление](/Semester_1/Labs/Lab17/lab_17.py)


<a name="Labs-done-c++">

### C++ <img src="https://github.com/devicons/devicon/blob/master/icons/cplusplus/cplusplus-original.svg"  title="Python" alt="Python" width="40" height="40"/>&nbsp;
</a>

1. [x] ["Задача о скобках"](/Semester_1/Labs/Lab1/1.cpp)
2. [ ] ["Задача об арифметическом выражении"](/Semester_1/Labs/Lab2/2.cpp)
3. [x] ["Задача о простых множителях"](/Semester_1/Labs/Lab3/3.cpp)
4. [x] [Comb sort (Сортировка методом прочесывания)](/Semester_1/Labs/Lab4/4.cpp)
5. [x] [Insertion sort (Сортировка вставками)](/Semester_1/Labs/Lab5/5.cpp)
6. [x] [Selection sort (Сортировка выбором)](/Semester_1/Labs/Lab6/6.cpp)
7. [x] [Shell sort (Сортировка Шелла)](/Semester_1/Labs/Lab7/7.cpp)
8. [x] [Radix sort (Поразрядная сортировка)](/Semester_1/Labs/Lab8/8.cpp)
9. [x] [Heap sort (Сортировка пирамидальная)](/Semester_1/Labs/Lab9/9.cpp)
10. [x] [Merge sort (Сортировка слиянием)](/Semester_1/Labs/Lab10/10.cpp)
11. [x] [QSort (Быстрая сортировка)](/Semester_1/Labs/Lab11/11.cpp)
12. [ ] [External multiphase merge sort (Внешняя многофазная сортировка слиянием)](/Semester_1/Labs/Lab12/12.cpp)
13. [ ] [Хэш-табоица с открытой адресацией](/Semester_1/Labs/Lab13/13.cpp)
14. [ ] [Хэш-табоица со списками](/Semester_1/Labs/Lab14/14.cpp)
15. [ ] [Рекурсивные обходы (прямой, центральный, концевой)](/Semester_1/Labs/Lab15/15.cpp)
16. [ ] [Не рекурсивный прямой обход](/Semester_1/Labs/Lab16/16.cpp)
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

1. Используем [стэк](https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B5%D0%BA). Кладём туда открывающие скобочки по мере их поступления и убираем оттуда по одной последние, если встречаем нужную закрывающую. Навалено много синтаксического сахара, версию без наворотов смотреть [тут](/Semester_1/Labs/Lab1/Lab_1_simple.py).
2. Читаем на Википедии про [обратную польскую нотацию](https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D0%B0%D1%8F_%D0%BF%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B0%D1%8F_%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D1%8C) и вникаем.
3. Простой перебор по степеням с ограничением логарифмом. Это задача факторизации, если есть желание упороться и написать эффективно - [читаем](https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%BA%D1%82%D0%BE%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F_%D1%86%D0%B5%D0%BB%D1%8B%D1%85_%D1%87%D0%B8%D1%81%D0%B5%D0%BB).

Далее статьи могут быть на инглише, но вы его должны знать, если вы программист. Ну или у вас всегда есть под рукой переводчик.

4. [Читаем](https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D1%80%D0%B0%D1%81%D1%87%D1%91%D1%81%D0%BA%D0%BE%D0%B9) 
5. [Читаем](https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D0%B2%D1%81%D1%82%D0%B0%D0%B2%D0%BA%D0%B0%D0%BC%D0%B8)
6. [Читаем](https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D0%B2%D1%8B%D0%B1%D0%BE%D1%80%D0%BE%D0%BC)
7. [Читаем](https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D0%A8%D0%B5%D0%BB%D0%BB%D0%B0)
8. [Читаем](https://thecode.media/radix/)
9. [Читаем](https://habr.com/ru/companies/otus/articles/460087/). [Heap](https://www.geeksforgeeks.org/binary-heap/) - специальная структура, бинарное дерево, у которого родительский жлемент всегда больше любого из дочерних. 
10. [Читаем](https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D1%81%D0%BB%D0%B8%D1%8F%D0%BD%D0%B8%D0%B5%D0%BC)
11. [Читаем](https://ru.wikipedia.org/wiki/%D0%91%D1%8B%D1%81%D1%82%D1%80%D0%B0%D1%8F_%D1%81%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0)
12. [Читаем](https://habr.com/ru/companies/otus/articles/712234/). Я этих формулировок труба шатал.

Итак, у хэш-таблиц есть 2 типа обхода коллизии (Это и имеется в виду): 
- с открытой адресацией (подразделяются на Линейное зондирование, Квадратичное зондирование и Двойное хеширование)

![Open adressation method](/docs/images_for_readme/hash_table_13.png)

- метод цепочек. 

![Chain method](/docs/images_for_readme/hash_table_14.png)

Вот, учите инглиш а затем...
[читайте](https://op-al.gitbook.io/s-30-voprosy-i-dop.-voprosy/31.-khesh-tablicy.-kollizii.-sposoby-razresheniya-kollizii.-otkrytaya-adresaciya), 

[читайте](https://medium.com/codex/hash-tables-hashing-and-collision-handling-8e4629506572), 

[читайте](https://habr.com/ru/articles/509220/), 

[читайте](https://algolist.ru/ds/s_has.php), 

[читайте](https://habr.com/ru/articles/704724/), 

[читайте](https://www.geeksforgeeks.org/program-to-implement-hash-table-using-open-addressing/), 

[Линейный probing + TDD](https://realpython.com/python-hash-table/#hash-table-vs-dictionary)

13. В процессе
14. В процессе
15. В процессе
16. В процессе
17. В процессе





<a name="Presentations">

# Presentations from our lecturer
</a>

- [Введение (зачем???)](/docs/Lektsia_1_Vvedenie.pptx)
- [Введение в структуры данных](/docs/Lektsia_2_Struktury_dannykh.pptx)
- [Виды сортировок + псевдокод к ним (господи, я искал эту хрень месяц, а потом он просто скинул эту презентацию бл#$&!)](/docs/)





<a name="Explanation-extra">

# Some explanation of extra things that I wrote here
</a>
Гуляя по репозиторию Вы можете наткнуться на различную фигню, которую я для себя сделал, но которая точно, прямо 100%, прямо прямо да, стоила затраченных усчтвенных сил, времени и нервов. Пройдёмся немного по подобным штукам:

- [Файл с автоматическими тестами](/Semester_1/Tests/sorting_tests.py) 

Просто мне было лень придумывать примеры, поэтому я написал простенькие функции для тестирования кода в автоматическом формате, с генерацией тестов, замером времени, возможностью изменять параметры тестирования и красивым выводом в консоль. Запускаются тесты через [run_file.py](/Semester_1/Tests/sorting_run_file.py), а в [test_logs.txt](/Semester_1/Tests/test_logs.txt) сохраняются результаты проверок в случае, если тест был длиннее пары чисел.

- [Файл с автоматичесим тестированием хэш-таблицы](/Semester_1/Tests/hastables_tests.py)

В процессе

- [Файл с автоматичесим тестированием хэш-таблицы]()
