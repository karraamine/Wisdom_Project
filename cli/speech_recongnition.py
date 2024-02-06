import speech_recognition as sr

def SpeechRecognition():
    recognizer = sr.Recognizer()

    for _ in range(3):
        try:
            choice = int(input("Enter the number of the languages (En: 1; Fr: 2; Sp: 3; It: 4): "))
            if choice in [1, 2, 3, 4]:
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("Listening!")

    try:
        mic = sr.Microphone(device_index=0)
        
        if mic is None:
            print("Error: Unable to access the specified microphone.")
            return ""

        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.2)

            languages = ["en-EN", "fr-FR", "es-ES", "it-IT"]
            Text = recognizer.recognize_google(recognizer.listen(source), language=languages[choice - 1])

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
