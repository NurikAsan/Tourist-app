run:
	@echo "Starting Django server..."
	. $(VENV)/bin/activate && python manage.py runserver


migrate:
	@echo "Applying migrations..."
	. $(VENV)/bin/activate && python manage.py migrate


shell:
	@echo "Starting Django shell..."
	. $(VENV)/bin/activate && python manage.py shell
