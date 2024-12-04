# Prompt Engineering

Hangalapú vezérlés megvalósítása A35

## Leírás

Ez a projekt egy hangalapú vezérlőrendszert valósít meg, amely a felhasználó által mondott parancsokat szöveggé alakítja, majd az OpenAI API segítségével feldolgozza azokat. A rendszer képes meghatározni egy autó sebességét a felhasználó által adott parancs alapján.

## Fájlok

- `speech.py`: A fő Python szkript, amely tartalmazza a hangfelismerés és az OpenAI API-val való kommunikáció logikáját.

## Használat

1. Győződj meg róla, hogy telepítve vannak a szükséges Python csomagok:
    ```sh
    pip install speechrecognition openai sounddevice scipy wavio
    ```

2. Állítsd be az OpenAI API kulcsot a `speech.py` fájlban:
    ```python
    my_api_key = "YOUR_OPENAI_API_KEY"
    ```

3. Futtasd a `speech.py` szkriptet:
    ```sh
    python speech.py
    ```

4. A szkript elindul, és hangfelvételt készít. Beszélj a mikrofonba, amikor a "Most már beszélj!" üzenet megjelenik.

5. A szkript a felvett hangot szöveggé alakítja, majd az OpenAI API segítségével meghatározza az autó sebességét, és megjeleníti az eredményt.

## Megjegyzések

- A `speech_to_text` függvény a Google Web Speech API-t használja a hang szöveggé alakításához.
- A `speedset` függvény az OpenAI API-t használja a parancsok feldolgozásához és az autó sebességének meghatározásához.

## Licenc

Minden jog fenntartva Kullmann Barnabás által!!!!