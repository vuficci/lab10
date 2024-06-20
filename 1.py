from flask import Flask, render_template
import datetime

app = Flask(__name__)

# Функция для определения времени суток
def get_time_of_day():
    current_time = datetime.datetime.now().time()
    if current_time >= datetime.time(6, 0) and current_time < datetime.time(12, 0):
        return "Доброе утро"
    elif current_time >= datetime.time(12, 0) and current_time < datetime.time(18, 0):
        return "Добрый день"
    elif current_time >= datetime.time(18, 0) and current_time < datetime.time(24, 0):
        return "Добрый вечер"
    else:
        return "Доброй ночи"

@app.route('/')
def index():
    time_of_day = get_time_of_day()
    return render_template('index.html', time_of_day=time_of_day)

if __name__ == '__main__':
    app.run(debug=True)