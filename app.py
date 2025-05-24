# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    yorum = ""
    if request.method == "POST":
        ekipman = request.form["ekipman"]
        tuketim = request.form["tuketim"]
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Sen deneyimli bir enerji yöneticisisin. Verilen ekipman ve enerji tüketimi bilgisine göre enerji verimliliği açısından analiz yap ve önerilerde bulun."},
                    {"role": "user", "content": f"{ekipman} adlı ekipmanın tüketimi {tuketim} kWh. Enerji verimliliği açısından değerlendir."}
                ]
            )
            yorum = response.choices[0].message.content.strip()
            yorum = yorum.encode('utf-8').decode('utf-8')
        except Exception as e:
            yorum = f"Hata oluştu: {str(e)}"
    return render_template("index.html", yorum=yorum)
yorum = yorum.encode('utf-8').decode('utf-8')
if __name__ == "__main__":
    app.run(debug=True)
