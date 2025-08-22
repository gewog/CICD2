from python:3.11
workdir /app
run pip install --no-cache-dir -r requirements.txt
copy . ./
expose 8000
cmd ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]