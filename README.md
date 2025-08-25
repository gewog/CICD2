RUS/ENG:
#  CICD2Public — FastAPI + GitHub Actions CI/CD Pipeline

> **Цель проекта**: Построение полноценного CI/CD пайплайна без этапа деплоя для тренировки навыков автоматизации разработки.
---

### 🔧 Стек технологий

- **Python 3.11**
- **FastAPI** — веб-фреймворк для API
- **Uvicorn** — ASGI-сервер
- **pytest** — тестирование
- **GitHub Actions** — CI/CD
- **Docker** — сборка образов

---

### 📦 Файлы проекта

| Файл | Назначение |
|------|----------|
| `app.py` | Основной файл приложения с обработчиками `/main` и `/home` |
| `tests.py` | Тесты с использованием `pytest` и `AsyncClient` |
| `Dockerfile` | Сборка Docker-образа |
| `.github/workflows/ci.yml` | Автоматический CI/CD пайплайн |
| `requirements.txt` | Список зависимостей |

---

### 🛠 Как запустить локально

1. Убедитесь, что установлены:
   - Python 3.11
   - Docker
   - Git

2. Клонируйте репозиторий:
```bash
git clone https://github.com/gewog/CICD2.git
cd CICD2
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```


4. Запустите приложение:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

5. Откройте в браузере:
http://localhost:8000/main → {"message": "OK"}
http://localhost:8000/home → {"page_title": "home"}

### 🐳 Как собрать Docker-образ
```bash
docker build -t my-fastapi-image:latest .
```
Запустите контейнер:
```bash
docker run -p 8000:8000 my-fastapi-image:latest
```

### 🔄 Как работает CI/CD

При каждом git push или pull request на ветку master:

1. Автоматически проверяется код
2. Устанавливаются зависимости
3. Запускаются тесты (pytest)
4. Собирается Docker-образ

✅ Пример работы

$ curl http://localhost:8000/main
{"message": "OK"}

$ curl http://localhost:8000/home
{"page_title": "home"}

🎯 Цель проекта
Тренировка построения CI/CD пайплайна без деплоя — чтобы понять, как работают автоматические тесты, сборка образов и контроль качества кода.

📝 Автор
gewog
📧 gewoggewog@gmail.com

---
# 🚀 CICD2Public — FastAPI + GitHub Actions CI/CD Pipeline
> **Project Goal**: Building a full-fledged CI/CD pipeline without the deployment stage to practice development automation skills.
---
### 🔧 Technology Stack
- **Python 3.11**
- **FastAPI** — web framework for APIs
- **Uvicorn** — ASGI server
- **pytest** — testing
- **GitHub Actions** — CI/CD
- **Docker** — building images
---
### 📦 Project Files
   File | Purpose |
 |------|----------|
 | `app.py` | Main application file with `/main` and `/home` handlers |
 | `tests.py` | Tests using `pytest` and `AsyncClient` |
 | `Dockerfile` | Docker image build configuration |
 | `.github/workflows/ci.yml` | Automatic CI/CD pipeline |
 | `requirements.txt` | List of dependencies |
---
### 🛠 How to Run Locally
1. Ensure you have installed:
   - Python 3.11
   - Docker
   - Git
2. Clone the repository:
```bash
git clone https://github.com/gewog/CICD2.git
cd CICD2
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the application:
```bash
uvicorn app\:app --host 0.0.0.0 --port 8000 --reload
```

5. Open in your browser:
http://localhost:8000/main → {"message": "OK"}
http://localhost:8000/home → {"page_title": "home"}

### 🐳 How to Build a Docker Image
 Copydocker build -t my-fastapi-image\:latest .
Run the container:
```bash
docker run -p 8000:8000 my-fastapi-image\:latest
```

### 🔄 How CI/CD Works
On every git push or pull request to the master branch:

1. Code is automatically checked
2. Dependencies are installed
3. Tests are run (pytest)
4. Docker image is built

✅ Example Output
$ curl http://localhost:8000/main
{"message": "OK"}

$ curl http://localhost:8000/home
{"page_title": "home"}

📝 Author
gewog
📧 gewoggewog@gmail.com