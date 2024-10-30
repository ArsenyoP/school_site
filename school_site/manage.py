#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_site.settings')

    # Отримання порту з змінних середовища
    port = int(os.environ.get("PORT", 8000))  # 8000 - порт за замовчуванням

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Додаємо порт до аргументів командного рядка
    sys.argv.append(f'0.0.0.0:{port}')
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
