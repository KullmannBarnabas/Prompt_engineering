import speech_recognition as sr
import openai
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

def speech_to_text(audio_file_path):
    # Create a recognizer instance
    recognizer = sr.Recognizer()

    try:
        # Open the audio file
        with sr.AudioFile(audio_file_path) as source:
            print("Loading audio file...")
            audio_data = recognizer.record(source)  # Read the entire audio file

        # Perform speech recognition
        print("Converting speech to text...")
        text = recognizer.recognize_google(audio_data)  # Using Google Web Speech API
        print("Conversion complete!")
        return text

    except FileNotFoundError:
        print("Error: File not found.")
    except sr.UnknownValueError:
        print("Error: Could not understand the audio.")
    except sr.RequestError as e:
        print(f"Error: Could not request results from the speech recognition service; {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None


# Set up the OpenAI API key
my_api_key = "Your OpenAI API key" 
# Ha ellopod a kulcsot, az instant pokol!
# Replace with your OpenAI API key
from openai import OpenAI
def speedset():
    client = OpenAI(api_key=my_api_key)
    mymessages = [
    {"role": "system", "content": "determine the speed of a car\nguidelines:\nanswer only one number in km/h\n"}
]
    i = 0
    while True:
        try:
            #audio_path = input("Enter the path to the audio file: ")
            #print(audio_path)
            duration = 5
            freq = 44100
            name = "recording"
            name += str(i)
            name += ".wav"
            recording = sd.rec(int(duration * freq), 
				samplerate=freq, channels=2)
            print("Most már beszélj!\n")
            sd.wait()
            f = open(name, "w")
            wv.write(name, recording, freq, sampwidth=2)
            f.close()
            
            order = speech_to_text(name)
            # Call the OpenAI API to get a response
            print("Parancs: ", order, "\n")
            mymessages.append({"role": "user", "content": order})
            

            response = client.chat.completions.create(
               
                messages=mymessages,
                response_format={
                    "type": "text"        
                },
                 model="gpt-4o-mini",
                temperature=0.3,
                max_tokens=10,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            # Extract and print the chatbot's reply
            reply = response.choices[0].message.content
            print("Az auto sebessége: ",reply, "km/h \n")
            i += 1
            if i == 3:
                break

        except Exception as e:
            print(f"Error: {e}")
            return "error"
          

if __name__ == "__main__":
    speedset()
        
        
