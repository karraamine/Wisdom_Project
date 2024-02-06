import speech_recognition as sr

def SpeechRecognition():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold += 280

    try:
        mic = sr.Microphone(device_index=0)
        
        if mic is None:
            print("Error: Unable to access the specified microphone.")
            return ""

        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.2)

            languages = ["en-EN", "fr-FR", "es-ES", "it-IT"]
            Text = recognizer.recognize_google(recognizer.listen(source), language=languages[0])

            Text = str(Text).lower()
            return Text

    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"Error: {e}")

    return ""

print("You said: " + SpeechRecognition())
