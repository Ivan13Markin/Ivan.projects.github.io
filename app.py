from flask import Flask, render_template # type: ignore

app = Flask(__name__)  # Создаем приложение Flask

# Главная страница
@app.route('/')  # При переходе на http://localhost:5000/
def home():
    return render_template('index.html')  # Показываем HTML-страницу

# Запускаем сервер
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Добавьте host и port
