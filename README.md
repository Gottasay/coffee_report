# Coffee report

CLI утилита для построения отчетов по данным подготовки студентов к экзаменам.

Поддерживаемые отчеты:
- median-coffee — медианная сумма трат на кофе по каждому студенту.

Пример запуска:

python src/main.py \
--files data/math.csv data/physics.csv data/programming.csv \
--report median-coffee
