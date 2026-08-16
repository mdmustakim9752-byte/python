import sqlite3
import os

# 📍 GPS (Exact path dhoondho taaki naya DB na ban jaye)
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, "zoya_brain.db")

# Asli database se direct connection
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 4 din purani date force inject kar rahe hain (Wednesday, 12 August)
cursor.execute("UPDATE user_profiles SET last_seen = 'Wednesday, 12 August 2026, 10:41 PM'")
conn.commit()
conn.close()

print("⏳ BOOM! TIME TRAVEL SUCCESSFUL! Asli database update ho gaya!")
