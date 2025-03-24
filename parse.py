import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# Настройки доступа
SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]
CREDS = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", SCOPE)
CLIENT = gspread.authorize(CREDS)

# Укажите ссылку или ID вашей таблицы
SHEET_ID = "ваш_ид_таблицы"  # Замените на реальный ID
SHEET_NAME = "Лист1"

def main():
    try:
        # Открытие таблицы
        sheet = CLIENT.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
        data = sheet.get_all_values()

        # Извлечение столбцов B (индекс 1) и D (индекс 3)
        filtered_data = []
        for row in data:
            if len(row) >= 4 and row[1] and row[3]:  # Пропуск пустых строк
                filtered_data.append([row[1], row[3]])

        # Сохранение в CSV
        df = pd.DataFrame(filtered_data, columns=["Никнейм", "Направления"])
        df.to_csv("mc.csv", index=False, encoding="utf-8-sig", sep=";")
        print("Файл mc.csv успешно создан!")

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
