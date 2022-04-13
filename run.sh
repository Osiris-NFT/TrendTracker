cd ./src/
uvicorn main:app --host 0.0.0.0 --port 8080 &
python3 -u script.py