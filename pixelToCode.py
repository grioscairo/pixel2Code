from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window as wind
from kivy.config import Config
from pathlib import Path
from PIL import Image as imagen

class pixel2Code(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols=1        
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        wind.bind(on_dropfile = self.on_file_drop)
        Config.set('graphics', 'width', '500')
        Config.set('graphics', 'height', '900')
        Config.write()
        self.window.size_hint = (0.55, 0.85)
        
        #add widgets to window

        #image widget
        self.window.add_widget(Image(source = "Window-elements\converter-logo.png"))
        #label widget
        self.titulo = Label(
                        text = "Pixel2Code",
                        font_size = 24,
                        color = '#ffc40d'
                        )
        self.subtitulo = Label(
                        text = "Conversor de pixel art a código para [b]MiniWin[/b]",
                        markup = True,
                        font_size = 16,
                        color = '#dddede'
                        )                      
        self.confirma = Label(
                        text = "",
                        font_size = 18,
                        color = '#ffc40d'
                        )
        self.location = Label(
                        text = "",
                        font_size = 18,
                        color = '#ffc40d',
                        text_size = (400, 20),   
                        shorten_from = 'left',
                        halign = 'center'
                        )                       
        self.greeting = Label(
                        text = "Arrastra el pixel art a convertir:",
                        font_size = 18,
                        color = '#ffc40d'
                        )  
        self.firma = Label(
                        text = "©2022 Gabriel Rios Cairo \nGitHub: @grioscairo",
                        font_size = 16,
                        color = '#a0885c',
                        text_size = (None, 140),
                        halign = 'center'
                        )         
        self.window.add_widget(self.titulo)
        self.window.add_widget(self.subtitulo)
        self.window.add_widget(self.confirma)
        self.window.add_widget(self.greeting)
        self.window.add_widget(self.location)

        self.cuadX = Label(text = "# pixeles en eje X: ")
        self.cuadY = Label(text = "# pixeles en eje Y: ")
        self.espacio = Label(text = "Tamaño del pixel: ")
        self.inix = Label(text = "Punto de inicio X: ")
        self.iniy = Label(text = "Punto de inicio Y: ")        
        
        
        #text input widget
        self.numCuadX = TextInput(
                    multiline = False,
                    padding_y = (5, 4),
                    size_hint = (1, 0.9),
                    input_filter = 'int'
                    )
        self.numCuadY = TextInput(
                    multiline = False,
                    padding_y = (5, 4),
                    size_hint = (1, 0.9),
                    input_filter = 'int'
                    )
        self.numEspacio = TextInput(
                    multiline = False,
                    padding_y = (5, 4),
                    size_hint = (1, 0.9),
                    input_filter = 'float'
                    )
        self.numIniX = TextInput(
                    multiline = False,
                    padding_y = (5, 4),
                    size_hint = (1, 0.9),
                    input_filter = 'float'
                    )
        self.numIniY = TextInput(
                    multiline = False,
                    padding_y = (5, 4),
                    size_hint = (1, 0.9),
                    input_filter = 'float'
                    )

        self.window.add_widget(self.cuadX)                    
        self.window.add_widget(self.numCuadX)
        self.window.add_widget(self.cuadY)                    
        self.window.add_widget(self.numCuadY)
        self.window.add_widget(self.espacio)                    
        self.window.add_widget(self.numEspacio)
        self.window.add_widget(self.inix)                    
        self.window.add_widget(self.numIniX)
        self.window.add_widget(self.iniy)                    
        self.window.add_widget(self.numIniY)

        #button widget
        self.button = Button(
                      text="Generar .txt",
                      size_hint = (1, 1),
                      bold = True, 
                      background_color = '#e8b419',
                      background_normal = ""
                      )
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)
        self.window.add_widget(self.firma)

        return self.window
    
    def on_file_drop(self, window, file_path):
        fp = file_path.decode("utf-8")
        self.greeting.text = "Ubicación de pixel art:"
        self.location.text = fp 
    
    def pixel_rgb(self, img_path, x, y):
        im = imagen.open(img_path).convert('RGB')
        r, g, b = im.getpixel((x, y))
        a = (r, g, b)
        return a

    #callback
    def callback(self, instance):
        img = self.location.text

        ruta = 'nume.txt'
        path = Path('nume.txt')

        if not path.is_file():
            creaN = open(ruta,'x')
            with creaN as num:
                num.write(str(1)+"\n")
            creaN.close()
        escrN = open(ruta,'a')
        leeN = open(ruta,'r')
        n = int(leeN.readlines()[-1])
        leeN.close()

        nom = "demo0"+ str(n) +".txt"
        path2 = Path(nom)
        if not path2.is_file():
            creaPlano = open(nom, "x")
            creaPlano.close()    
            escrPlano = open(nom, "a")
        else:
            n += 1
            nom = "demo0"+ str(n) +".txt"
            creaPlano = open(nom, "x")
            creaPlano.close()
            escrPlano = open(nom, "a")

        dimx = int(self.numCuadX.text)
        dimy = int(self.numCuadY.text)
        espacio = float(self.numEspacio.text)
        inix = float(self.numIniX.text)
        iniy = float(self.numIniY.text)

        vx=0
        vy=0
            
        v = self.pixel_rgb(img, vx, vy)

        for ix in range(0, dimy):    
            for ix in range(0, dimx):
                if (v != (0,0,0)):
                    str_v = repr(v)
                    escrPlano.write("color_rgb"+str_v+";"+"\n")
                    escrPlano.write("rectangulo_lleno("+str(inix)+"+x,"+str(iniy)+"+y,"+str(inix+espacio)+"+x,"+str(iniy+espacio)+"+y);"+"\n")
                inix = inix + espacio
                vx += 1
                if vx < dimx:
                    v = self.pixel_rgb(img, vx, vy)            
                else:
                    if vy < (dimy - 1):
                        v = self.pixel_rgb(img, 0, vy+1)
            inix = float(self.numIniX.text)
            iniy += espacio
            vx = 0
            vy += 1

        escrPlano.close()    
                
        n +=1
        escrN.write(str(n)+"\n")
        escrN.close()
        self.confirma.text = "Archivo convertido."        
       
if __name__ == "__main__":
    pixel2Code().run()