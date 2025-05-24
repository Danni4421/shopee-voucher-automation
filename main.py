from src.lib.appium import Appium
from src.auto import run

app = Appium()

def main():
    app.start(run)

if __name__ == "__main__":
    main()