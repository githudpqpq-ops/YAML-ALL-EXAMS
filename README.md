# Практическая работа: Синтаксис YAML для GitHub Actions

Репозиторий содержит выполненные три задания по YAML, спецификацию workflow, реальный GitHub Actions workflow и скрипт проверки.

## Задания
1. Базовые типы данных и массивы — строки, числа, boolean, null, комментарии, блочный список из трёх значений.
2. Вложенные структуры и специальные символы — вложенные объекты, кавычки и экранирование, блочный и inline-массивы.
3. Продвинутые конструкции — иерархия более трёх уровней, коллекции и многострочные блоки.

Подробные условия: [TASK.md](TASK.md).

## Структура
- simple-config.yml — задание 1.
- nested-structure.yml — задание 2.
- workflow-spec.yml — задание 3.
- .github/workflows/yaml-validation.yml — автоматическая проверка при push и pull request.
- scripts/validate_yaml.py — локальный валидатор YAML.
- TASK.md — условия и чек-лист выполнения.

## Локальный запуск
Требуется Python 3.11+:

    python -m pip install PyYAML
    python scripts/validate_yaml.py

GitHub Actions запускает проверку автоматически при push или pull request в main и develop.
