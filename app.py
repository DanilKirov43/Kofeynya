from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

# Конфигурация соединения с базой данных
DB_CONFIG = {
    "host": "localhost",
    "database": "coffee_registration",
    "user": "postgres",
    "password": "613930"
}

# Функция для подключения к базе данных
def connect_to_db():
    return psycopg2.connect(**DB_CONFIG)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Получение данных из формы
        first_name = request.form["first-name"]
        last_name = request.form["last-name"]
        middle_name = request.form["middle-name"]
        password = request.form["password"]

        # Сохранение данных в базу данных
        try:
            conn = connect_to_db()
            cursor = conn.cursor()
            query = """
                INSERT INTO users (first_name, last_name, middle_name, password)
                VALUES (%s, %s, %s, %s);
            """
            cursor.execute(query, (first_name, last_name, middle_name, password))
            conn.commit()
            cursor.close()
            conn.close()
            return "Регистрация успешна!"
        except Exception as e:
            return f"Ошибка: {str(e)}"

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
