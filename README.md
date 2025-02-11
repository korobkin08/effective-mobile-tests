# Effective Mobile UI Tests

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.10
- Docker (опционально)
- Git

### Установка
```bash
git clone https://github.com/korobkin08/effective-mobile-tests.git
cd effective-mobile-tests
python -m venv venv

# Для Windows:
venv\Scripts\activate

# Для Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
playwright install
```

### Запуск тестов
```bash
# Обычный запуск
pytest tests/

# С генерацией Allure отчета
pytest --alluredir=allure-results
allure serve allure-results
```

### Запуск в Docker
```bash
docker build -t effective-tests .
docker run -v $(pwd)/allure-results:/app/allure-results effective-tests
```

## 🧩 Структура проекта
```
.
├── pages/        # Page Object модели
├── tests/        # Тестовые сценарии
├── utils/        # Вспомогательные утилиты
├── conftest.py   # Конфигурация Pytest
└── Dockerfile    # Конфигурация Docker
```

## 🔧 Troubleshooting
Если тесты падают:
1. Проверьте актуальность CSS-селекторов в `pages/main_page.py`
2. Убедитесь что сайт доступен: https://effective-mobile.ru
3. Для Docker проблем:
```bash
docker system prune -a
docker build --no-cache -t effective-tests .
```

## 📊 Отчеты Allure
```bash
allure serve allure-results