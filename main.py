import io
import PySimpleGUI as sg
from PIL import Image
import generateSentences as sentences

def turnImageToPng(image):
    pil_image = Image.open(io.BytesIO(image))
    pil_image = pil_image.resize((350, 280))
    png_bio = io.BytesIO()
    pil_image.save(png_bio, format="PNG")
    png_data = png_bio.getvalue()
    return png_data

# URL, Image & inputs
image_viewer = [
    [sg.Text("Ingrese una URL para mostrar la imagen a analizar", key="-SLCT-", )],
    [sg.In(size=(50, 1), expand_x=True, key="-IMAGE URL-")],
    [sg.Button(button_text="Show image", enable_events=True, key="-SHOW IMAGE-")],
    [sg.Image(size=(10, 300), key="-IMAGE-")],
    [
        sg.Button(button_text="Get tags from image", disabled=True, enable_events=True, key="-TAGS BUTTON-"),
        sg.Button(button_text="Describe image", disabled=True, enable_events=True, key="-DESCRIBE BUTTON-"), 
    ],
    [sg.Text("Words per sentence:")],
    [sg.In(size=(20, 1), disabled=True, key="-WORDS SENTENCES-")],
    [sg.Text("Sentences:")],
    [sg.In(size=(20, 1), disabled=True, key="-SENTENCES-")],
]

# Tags & Sentences
text_boxs = [
    [sg.Text("TAGS:")],
    [sg.Multiline(size=(250, 3), disabled=True, key="-TAGS TEXT-", autoscroll=True)],
    [sg.Text("SENTENCES:")],
    [sg.Multiline(size=(250, 50), disabled=True, key="-SENTENCE TEXT-", autoscroll=True)],
]

# ----- Full layout -----
layout = [
    [
        sg.Column(image_viewer, expand_y=True, vertical_alignment="center"),
        sg.VSeperator(),
        sg.Column(text_boxs),
    ]
]

window = sg.Window("ContextVision", layout, size=(1380, 800))

# Run the Event Loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "-SHOW IMAGE-":
        import requests
        try:
            image_url = window["-IMAGE URL-"].get()
            full_image = requests.get(image_url).content
            window["-IMAGE-"].update(turnImageToPng(full_image))
            window["-WORDS SENTENCES-"].update(disabled=False)
            window["-SENTENCES-"].update(disabled=False)
            window["-TAGS BUTTON-"].update(disabled=False)
        except:
            pass
    elif event == "-TAGS BUTTON-":
        multilineTagsTextBox = window["-TAGS TEXT-"]
        multilineTagsTextBox.update("")
        try:
            window["-TAGS BUTTON-"].update(disabled=True)
            window["-DESCRIBE BUTTON-"].update(disabled=False)
            multilineTagsTextBox.update(sentences.getTags(window["-IMAGE URL-"].get()))
        except:
            pass
    elif event == "-DESCRIBE BUTTON-":
        multilineSentenceTextBox = window["-SENTENCE TEXT-"]
        multilineSentenceTextBox.update("")
        try:
            multilineSentenceTextBox.update(sentences.generarOraciones(int(window["-WORDS SENTENCES-"].get()), int(window["-SENTENCES-"].get())))
        except:
            pass

window.close()