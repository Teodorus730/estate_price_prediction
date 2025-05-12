from app import app
from config import load_port


PORT=load_port()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)