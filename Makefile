save-dev:
	@echo "Saving dependencies..."
	@pip freeze > requirements.txt
	@echo "Dependencies saved to requirements.txt"