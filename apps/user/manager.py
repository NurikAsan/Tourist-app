from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def _create(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Не указан номер телефона')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number,  password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self._create(phone_number, password, **extra_fields)

    def create_user(self, phone_number, password=None, **extra_fields):
        return self._create(phone_number, password, **extra_fields)
