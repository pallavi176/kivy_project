import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from filefinder import FileFinder
from log import lg

# Designate Our .kv design file
Builder.load_file('style.kv')

class MyLayout(Widget):

    path = ObjectProperty(None)

    def press(self):
        try:
            path = self.path.text
            print(path) # C:\Users\pallavi.saxena\Downloads\
            lg(f'Path entered by the user: {path}')
            path=path.strip()
            file_obj = FileFinder(path)
            result = ''
            if file_obj.validate_path(path):
                file_list=file_obj.file_extractor()
                if len(file_list) > 0:
                    for f in file_list:
                        result = result + f + '\n'
                else:
                    result = f"No file found in the inputh path: {path}"
            else:
                result = f"Entered path: {path} is not valid. Kindly insert valid path..."
            #self.add_widget(Label(text=result))
            #print(result)
            self.ids.file_path.text = f'{result}'
            lg(f'Returning output to dashboard: {result}')

            # Clear the input boxes
            #self.path.text = ""
        except Exception as e:
            issue = "exception in press(): with error:"+ str(e) + "\n"
            issue = issue + "-------------------------------------------------\n"
            lg(issue)
            self.ids.file_path.text = f'{issue}'

    def merge(self):
        try:
            prior = self.ids.file_path.text
            path = self.path.text
            file_obj2 = FileFinder(path)
            f_list = prior.split('\n')
            print(f_list)
            lg(f'f_list: {f_list}')
            result2 = file_obj2.pdf_merger(f_list)
            self.ids.msg.text = f'{result2}'
            lg(f'Returning output to dashboard: {result2}')
        except Exception as e:
            issue = "exception in merge(): with error:"+ str(e) + "\n"
            issue = issue + "-------------------------------------------------\n"
            lg(issue)
            self.ids.msg.text = f"{issue}"

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()

class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()