import os
import base64

# הגדרת נתיב התיקייה המכילה את קובצי ה-MP3
audio_folder = "top_k_songs_audio"
output_folder = "top_k_songs_base64"

# יצירת תיקיית הפלט אם אינה קיימת
os.makedirs(output_folder, exist_ok=True)


def convert_audio_to_base64(audio_path):
    """ממיר קובץ אודיו ל-Base64 ומחזיר את המחרוזת"""
    try:
        with open(audio_path, "rb") as audio_file:
            return base64.b64encode(audio_file.read()).decode()
    except FileNotFoundError:
        return None


# מעבר על כל הקבצים בתיקייה
for filename in os.listdir(audio_folder):
    if filename.endswith(".mp3"):
        audio_path = os.path.join(audio_folder, filename)
        base64_str = convert_audio_to_base64(audio_path)

        if base64_str:
            # שמירה של התוכן כקובץ טקסט עם אותו שם
            txt_filename = os.path.splitext(filename)[0] + ".txt"
            txt_path = os.path.join(output_folder, txt_filename)

            with open(txt_path, "w", encoding="utf-8") as txt_file:
                txt_file.write(base64_str)

print("✔ כל הקבצים הומרו בהצלחה ל-Base64 ונשמרו בתיקייה:", output_folder)
