from app import create_app
import sys

sys.dont_write_bytecode = True

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

