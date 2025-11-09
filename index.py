from flask import Flask
import time
from datetime import datetime




app = Flask(__name__)

@app.route('/')
def home():
    dni = time.time() / (60 * 60 * 24)
    teraz = datetime.now()
    minuta_dnia = teraz.hour * 60 + teraz.minute

    return f'''
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="refresh" content="1" >
        <title>My Calendar</title>
    
    </head>

    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #b4b4b6;
            padding: 20px;
            text-align: center;
            margin: 0;
            margin-top: 0;
            margin-bottom: 0;
            margin-left: 0;
            margin-right: 0;
        }}
        .day {{
            font-size: 48px;
            margin-bottom: 20px;
            background-color: #a4a4d6;  
            position: fixed;
            top: 5%;
            padding-bottom: 20px;
            text-align: center;
            line-height: 500%;
            height: 40%;
            width: 95%;
        }}
        .time {{
            font-size: 48px;
            margin-top: 20px;
            background-color: #d4a4a6;
            position: fixed;
            bottom: 5%;
            padding-top: 20px;
            text-align: center;
            line-height: 500%;
            height: 40%;
            width: 95%;

        }}
    </style>

    <body>
        <div class="day">📆day: {dni:.0f}📆</div>
        <div class="time">⏰time: {minuta_dnia}⏰</div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
