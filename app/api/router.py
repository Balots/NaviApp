import os  # Для работы с операционной системой, например, для доступа к переменным окружения.

from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
# APIRouter: для организации маршрутов API.
# UploadFile, File: для обработки загружаемых файлов.
# Depends: для инъекции зависимостей.
# HTTPException: для возврата HTTP-ошибок.

from app.api.schemas import Message
# Message: схема данных (Pydantic) для описания структуры сообщения.

from app.auth.models import User
# User: модель пользователя из модуля авторизации.

from app.config import settings
# settings: настройки приложения.

router = APIRouter(prefix='/api', tags=['API'])


