import os
import importlib

def build(root):
    current_dir = os.path.dirname(__file__)
    for filename in os.listdir(current_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            modulename = filename[:-3]
            module = importlib.import_module(f'src.app.components.{modulename}')
            if hasattr(module, 'build'):
                module.build(root)