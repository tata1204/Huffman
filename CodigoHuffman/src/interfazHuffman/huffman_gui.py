from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import sys
sys.path.append("src")  # Agrega el directorio "src" al path para importar el módulo personalizado

# Importar las funciones de codificación y decodificación desde el módulo huffman
from huffmanCode.huffman import encode_message, decode_message

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        # Diseño de la pantalla principal
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

        # Título
        title_label = Label(text='Seleccionar modo:', font_size=24, size_hint=(1, 0.5), pos_hint={'top': 0.9})
        layout.add_widget(title_label)

        # Botones para seleccionar modo de codificación o decodificación
        self.encode_button = Button(text='Codificar', size_hint=(1, None), size=(200, 100), font_size=20)
        self.encode_button.bind(on_press=self.switch_to_encode_screen)
        layout.add_widget(self.encode_button)

        self.decode_button = Button(text='Decodificar', size_hint=(1, None), size=(200, 100), font_size=20)
        self.decode_button.bind(on_press=self.switch_to_decode_screen)
        layout.add_widget(self.decode_button)

        self.add_widget(layout)

    def switch_to_encode_screen(self, instance):
        # Cambia a la pantalla de codificación
        self.manager.current = 'encode'

    def switch_to_decode_screen(self, instance):
        # Cambia a la pantalla de decodificación
        self.manager.current = 'decode'


class EncodeScreen(Screen):
    def __init__(self, **kwargs):
        super(EncodeScreen, self).__init__(**kwargs)

        # Diseño de la pantalla de codificación
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Ingrese el mensaje:'))
        self.message_input = TextInput(multiline=False)
        layout.add_widget(self.message_input)
        encode_button = Button(text='Codificar Mensaje', size_hint=(None, None), size=(150, 50))
        encode_button.bind(on_press=self.encode_message)
        layout.add_widget(encode_button)
        layout.add_widget(Label(text='Secuencia Huffman del mensaje ingresado:'))
        self.encoded_output = TextInput(readonly=True)
        layout.add_widget(self.encoded_output)
        layout.add_widget(Label(text='Diccionario:'))
        self.dictionary_output = TextInput(readonly=True, multiline=True)
        layout.add_widget(self.dictionary_output)
        back_button = Button(text='Regresar', size_hint=(None, None), size=(100, 50))
        back_button.bind(on_press=self.switch_to_main_screen)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def encode_message(self, instance):
        # Codifica el mensaje ingresado
        message = self.message_input.text.strip()  
        encoded, dictionary = encode_message(message)
        self.encoded_output.text = encoded
        self.dictionary_output.text = dictionary

    def switch_to_main_screen(self, instance):
        # Regresa a la pantalla principal
        self.manager.current = 'main'


class DecodeScreen(Screen):
    def __init__(self, **kwargs):
        super(DecodeScreen, self).__init__(**kwargs)

        # Diseño de la pantalla de decodificación
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Ingrese el código:'))
        self.encoded_input = TextInput(multiline=False)
        layout.add_widget(self.encoded_input)
        decode_button = Button(text='Decodificar Mensaje', size_hint=(None, None), size=(150, 50))
        decode_button.bind(on_press=self.decode_message)
        layout.add_widget(decode_button)
        layout.add_widget(Label(text='Mensaje decodificado:'))
        self.decoded_output = TextInput(readonly=True)
        layout.add_widget(self.decoded_output)
        back_button = Button(text='Regresar', size_hint=(None, None), size=(100, 50))
        back_button.bind(on_press=self.switch_to_main_screen)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def decode_message(self, instance):
        # Decodifica el código ingresado
        encoded = self.encoded_input.text.strip()  
        decoded = decode_message(encoded, self.parent.get_screen('encode').dictionary_output.text)
        self.decoded_output.text = decoded

    def switch_to_main_screen(self, instance):
        # Regresa a la pantalla principal
        self.manager.current = 'main'



class HuffmanApp(App):
    def build(self):
        # Configura el ScreenManager con las distintas pantallas
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(EncodeScreen(name='encode'))
        sm.add_widget(DecodeScreen(name='decode'))
        return sm

    def encode_message(self, message):
        # Codifica el mensaje y guarda la información de codificación
        encoded, dictionary = encode_message(message)
        self.root.get_screen('encode').encoded_output.text = encoded
        self.root.get_screen('encode').dictionary_output.text = dictionary

    def decode_message(self, encoded):
        # Decodifica el mensaje y muestra la información de decodificación
        decoded = decode_message(encoded)
        self.root.get_screen('decode').decoded_output.text = decoded

# Ejecuta la aplicación
if __name__ == '__main__':
    HuffmanApp().run()
