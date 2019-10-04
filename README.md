
                                    First review task for Python
   
   Смоделирована экологическая система океана, в котором обитают рыбы и креветки. Океан пред-
ставляется двумерным массивом ячеек. Каждая ячейка может содержать:
    • рыбу
    • креветку
    • скалу
    • ничего  
    Все ячейки за границами игрового поля считаются пустыми. В каждый квант времени океан меня-
ется, причем атомарно — т.е. все ячейки меняют свое состояние одновременно. Соседи ячейки —это
не более 8 ячеек, у которых есть общая граница с ней (ячейки на границах поля имеют меньше 8
соседей). Изменение ячеек происходит по определенным правилам:
    1. Ячейки со скалами не меняются во времени.
    2. Если какой-то рыбе слишком тесно (у нее 4 и более соседей-рыб), либо слишком одиноко
    (меньше 2 соседей-рыб), то рыба погибает.
    3. Если у рыбы 2 или 3 соседа-рыбы, то она просто продолжает жить.
    4. Соседи-скалы и соседи-креветки никак не влияют на жизнь рыб.
    5. Креветки существуют по аналогичным правилам. Рыбы на них не влияют
    6. Если какая-то ячейка океана была пуста и имела ровно 3-х соседей рыб, то в следующий
момент времени в ней рождается рыба. В противном случае, если у ячейки было ровно три
соседа-креветки, в ней рождается креветка.
 
                                    Формат входных данных

   В первой строке записаны 3 целых положительных числа N, M, K (1 ⩽ N, M, K ⩽ 250000, причем
N · M · K ⩽ 250000). N обозначает количество строк, M —количество столбцов, K —количество
итераций игры.
Далее в N строках вводится по M символов, описывающих поле. Возможные символы: f,r,n,s.
Обозначения:
• f —рыба
• r —скала
• n —ничего
• s —креветка

                                    Формат выходных данных
                                
   Конечное поле в том же формате, в котором вводилось его начальное состояние, то
есть N строк по M символов.
"""
