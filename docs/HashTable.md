### Что такое хэш-таблица?

Очень грубо говоря - динамический массив, куда мы кладём уникальные значения. Но для того, чтобы понять, в какую ячейку нам положить значение - мы действуем на него некоторой функцией (называем её хэш-функцикй) и так получаем нужный индекс. Однако хэш-функция может для разных наших значений дать один индекс. Данная ситуация называется коллизией. Вернёмся к ним парой строчек дальше. Хэш таблица в определённый момент закончится. Чтобы этого не допустить, мы делаем rehash, рехэш, рескейл таблицы. Когда значение загруженности таблицы (load factor = количество элементов / размер таблицы) доходит до критического (у меня 0.75), то таблица пересоздаётся с большим размером (у меня в два раза) и все элементы из старой таблицы переносятся в новую с учётом новых её размеров.

Итак, у хэш-таблиц есть 2 типа обхода коллизии (Это и имеется в виду): 
- с открытой адресацией (подразделяются на Линейное зондирование, Квадратичное зондирование и Двойное хеширование)

- метод цепочек. 

Спешу заметить, что в питоновской реализации присутствуют для удобства программиста методы, называемые [магическими](https://habr.com/ru/articles/186608/). Они позволяют нам менять алгоритм действий программы при вызове для наших собственных классов некоторых функций, например `__len__()` для `len()`, `__str__()` для `print()` и `str()`, `__eq__()` для `==` и т.д. Почитайте, интересная штука, на самом деле. И статейка короткая совсеим на хабре.

Все реализации у меня есть, все лежат. Выбираете любую по своему усмотрению (или какая вам просто под руку подвернулась) и смотрите:

ВАЖНО! На плюсах мне было лень писать запись и чтение в файл, но необходимый для лабы функционал протестирован и работает (если лаба выложена, хых) (по крайней мере на малом наборе данных)

 13. Open Adressing

 - - Linear-Probing on [<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg"  title="Python" alt="Python" width="15" height="15"/>](/Semester_1/Labs/Lab13/HashTable_linear_probing.py), [<img src="https://github.com/devicons/devicon/blob/master/icons/cplusplus/cplusplus-original.svg"  title="Python" alt="Python" width="17" height="17"/>](Semester_1/Labs/Lab13/HashTable_linear_probing.cpp) - Значения при возникновении коллизии кладутся в следующие ячейки до тех пор, пока коллизий не будет. Ищется по такому же принципу (т.е. до тех пор, пока не найдём значение в следующих ячейках или пока следующая ячейка не будет пустой)

 - - Quadratic-Probing on [<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg"  title="Python" alt="Python" width="17" height="17"/>](/Semester_1/Labs/Lab13/HashTable_quadratic_probing.py), [<img src="https://github.com/devicons/devicon/blob/master/icons/cplusplus/cplusplus-original.svg"  title="Python" alt="Python" width="17" height="17"/>](Semester_1/Labs/Lab13/HashTable_quadratic_probing.cpp) - Значения при возникновении коллизии кладутся в следующие ячейки по принципу "сначала прибавим квадрат единички, потом сверху квадрат двойки, потом квадрат тройки и т.д." до тех пор, пока коллизий не будет. Ищется по такому же принципу (т.е. до тех пор, пока не найдём значение в следующих ячейках или пока следующая найденная подобным образом ячейка не будет пустой)

 - - Double-Hashing on [<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg"  title="Python" alt="Python" width="17" height="17"/>](/Semester_1/Labs/Lab13/HashTable_double_hashing.py), [<img src="https://github.com/devicons/devicon/blob/master/icons/cplusplus/cplusplus-original.svg"  title="Python" alt="Python" width="17" height="17"/>](Semester_1/Labs/Lab13/HashTable_double_hashing.cpp) - !!!Найдена ошмбка в алгоритме при одном из крайних случаев, в процессе исправления. Если хотите помочь - кидайте пулл-реквест!!! Сложнее. У нас есть вторая хэш-функция. Значения при возникновении коллизии кладутся в следующие ячейки по принципу "будет домножать хэш-код номер 2 на номер нашей попытки положить значение в следующую ячейку и пытаться класть его снова до тех пор, пока в конечном итоге не получится". Ищется по такому же принципу.

 14. Chain method on [<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg"  title="Python" alt="Python" width="17" height="17"/>](/Semester_1/Labs/Lab13/HashTable_separate_chaining.py), [<img src="https://github.com/devicons/devicon/blob/master/icons/cplusplus/cplusplus-original.svg"  title="Python" alt="Python" width="17" height="17"/>](Semester_1/Labs/Lab14/HashTable_separate_chaining.cpp) - Коллизия - это лишь обман вашего восприятия. Если возникает коллизия - пф, не проблема. У нас заранее обозначено, что в ячейках лежат не просто значения, а "узлы", имеющие два параметра - собственное значение и указатель на следующий элемент. Теперь при возникновении колизии мы просто идём по своеобразному односвязному списку узлов до тех пор, пока указатель на следующий узел не будет нульпоинтером и добавляем новый узел. Поиск производится так же, нахождением списка элементов с данным хэш-кодом и пробегом по этому списку до тех пор, пока не найдём \ поймём, что не нашли нужный нам элемент. С некоторыми дополнительными методами типа `len()` и `__str__()` тут по сложнее. Я написал `@property`-методы (методы, заменяющие алгоритм получения каких-то собстевнных свойств класса) для получения сразу всех ключей и пар индекс-ключ на работающие за O(n). Зато работающие.

Если кому-то ОЧЕНЬ захочется УГЛУБИТЬСЯ в тему, то овт... [Читайте](https://op-al.gitbook.io/s-30-voprosy-i-dop.-voprosy/31.-khesh-tablicy.-kollizii.-sposoby-razresheniya-kollizii.-otkrytaya-adresaciya), 
[читайте](https://medium.com/codex/hash-tables-hashing-and-collision-handling-8e4629506572), 
[читайте](https://habr.com/ru/articles/509220/), 
[читайте](https://algolist.ru/ds/s_has.php), 
[читайте](https://habr.com/ru/articles/704724/), 
[читайте](https://www.geeksforgeeks.org/program-to-implement-hash-table-using-open-addressing/), 
[Линейный probing + TDD](https://realpython.com/python-hash-table/#hash-table-vs-dictionary)