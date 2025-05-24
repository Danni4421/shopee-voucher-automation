save-dev:
	@echo "Saving dependencies..."
	@pip freeze > requirements.txt
	@echo "Dependencies saved to requirements.txt"

pip-install:
	@read -p "Enter the package name to install: " pkg; \
	pip install $$pkg && pip freeze > requirements.txt

run:
	@echo "Running the script..."
	@if command -v python3 >/dev/null 2>&1; then \
		python3 main.py; \
	else \
		python main.py; \
	fi