from flask import Flask, render_template, request ,redirect
import speech_recognition as sr
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/pilihadits")
def pilihadits():
    return render_template('pilihan_hadits.html')

@app.route("/hadits1", methods=["GET", "POST"])
def hadits1():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            f = open('hadits.json')
            data = json.load(f)
            hadits = data['hadits_data'][0]['lafadz']

            recognizer = sr.Recognizer()
            lang = 'ar-AR'

            audioFile = sr.AudioFile(file)
            with audioFile as source:
                haditsrec = recognizer.record(source)
            arabrec = recognizer.recognize_google(haditsrec, language=lang)
            f = open('text.txt', 'w', encoding='utf-8')
            f.writelines(arabrec + '\n')
            f.close()
            with open("text.txt") as f:
                firstline = f.readline().rstrip()

            if hadits == firstline:
                transcript = "Benar"
            elif hadits != firstline:
                transcript = "Salah"
            else:
                transcript = "Haditsnya mana?"

    return render_template('hadits1.html', transcript=transcript)

@app.route("/hadits9", methods=["GET", "POST"])
def hadits9():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            f = open('hadits.json')
            data = json.load(f)
            hadits = data['hadits_data'][1]['lafadz']

            recognizer = sr.Recognizer()
            lang = 'ar-AR'

            audioFile = sr.AudioFile(file)
            with audioFile as source:
                haditsrec = recognizer.record(source)
            arabrec = recognizer.recognize_google(haditsrec, language=lang)
            f = open('text.txt', 'w', encoding='utf-8')
            f.writelines(arabrec + '\n')
            f.close()
            with open("text.txt") as f:
                firstline = f.readline().rstrip()

            if hadits == firstline:
                transcript = "Benar"
            elif hadits != firstline:
                transcript = "Salah"
            else:
                transcript = "Haditsnya mana?"

    return render_template('hadits9.html', transcript=transcript)

@app.route("/hadits10", methods=["GET", "POST"])
def hadits10():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            f = open('hadits.json')
            data = json.load(f)
            hadits = data['hadits_data'][2]['lafadz']

            recognizer = sr.Recognizer()
            lang = 'ar-AR'

            audioFile = sr.AudioFile(file)
            with audioFile as source:
                haditsrec = recognizer.record(source)
            arabrec = recognizer.recognize_google(haditsrec, language=lang)
            f = open('text.txt', 'w', encoding='utf-8')
            f.writelines(arabrec + '\n')
            f.close()
            with open("text.txt") as f:
                firstline = f.readline().rstrip()

            if hadits == firstline:
                transcript = "Benar"
            elif hadits != firstline:
                transcript = "Salah"
            else:
                transcript = "Haditsnya mana?"

    return render_template('hadits10.html', transcript=transcript)

if __name__ == "__main__":
    app.run(debug=True)