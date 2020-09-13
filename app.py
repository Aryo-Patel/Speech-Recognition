from flask import Flask, render_template, request, redirect

import speech_recognition as sr

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    transcript = ""
    if request.method == 'POST':
        print('hello world')

        if "file" not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == "":
            return redirect(request.url)
        
        if file:
            recognizer = sr.Recognizer()
            ###Create audio file and parse that in to recognizer###
            audioFile = sr.AudioFile(file)

            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data)
            
    return render_template('index.html', transcript = transcript)


if __name__ == "__main__":
    app.run(debug=True, threaded = True)