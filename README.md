# CZ Service 1C UPP

Сервис интеграции 1С УПП с Честным Знаком.

Первая цель проекта: проверить связь между 1С и Python-сервисом по HTTP.

## Быстрый старт на Windows

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Проверка в браузере:

```text
http://127.0.0.1:8000/ping
```

Ожидаемый ответ:

```json
{
  "ok": true,
  "service": "CZ_Service_1C_UPP",
  "message": "Связь с сервисом работает"
}
```
