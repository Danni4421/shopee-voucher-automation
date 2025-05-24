import os
import importlib

def run(driver):
    current_dir = os.path.dirname(__file__)
    for filename in os.listdir(current_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            modulename = filename[:-3]
            module = importlib.import_module(f'auto.{modulename}')
            if hasattr(module, 'run'):
                module.run(driver)