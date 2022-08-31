import gtts
from googletrans import Translator as tra
try:
    import pywhatkit as kit
except:
    print("pyWhatKit not import")
import requests
from bs4 import BeautifulSoup
from bing_image_downloader import downloader



class kit:
    
    def transe(self, Text : str, TextLang : str, cvtTo : str ):
        try :
            translator = tra()
            output : str = translator.translate(Text, src = TextLang, dest = cvtTo)
            return output
        except : 
            return "404-error"

    # def dec(self, Text : str ,To_lang : str):
    #     try :
    #         translator : Translator = Translator(to_lang = To_lang)
    #         translation : str = translator.translate(Text)
    #         return translation
    #     except :
    #         return "404-Error try again"

    def textTOVoice(self, Text : str, langu : str, FileName : str, slow : bool = False):
        print("run")
        try :
            audio_file = gtts.gTTS(text = Text, lang=langu, slow=slow)
            audio_file.save(FileName)
        except :
            return "File not process...!"
    
    def TextToHand(self, Text : str , save : str ):
        print("work")
        try : 
            kit.text_to_handwriting(Text, save_to = save)
        except:
            return "File not process...!" #image To text is also must
    
    def scrping(self, Text, paraLen):
        
        def url(query): # this function generateing a links
            links : list = []
            try:
                from googlesearch import search
            except ImportError:
                print("No module named 'google' found")
            # to search
            try:           
                for j in search(query, tld="co.in", num=10, stop=20, pause=2):
                    links.append(j)
            except:
                return "Problem occers in link generator(to search)"
            return links

        # link for extract html data
        def getdata(url):
            try:
                r = requests.get(url)
                return r.text
            except:
                return "none"
        link : list = url(Text) #total links

        try:
            output : list = []
            data : str = "" 
            for i in range(paraLen):
                htmldata = getdata(link[i])
                soup = BeautifulSoup(htmldata, 'html.parser')
                data : str = ''
                for data in soup.find_all("p"):
                    output.append(data.get_text())
            return output
        except:
            return "We are Can Not Founded....{-_-}"

    def KeyWordToPara(self, Keywords, lenPerPages): #it's also use (SA writing,letters)
        paragraph = self.scrping(Keywords,lenPerPages)
        return paragraph

    def KeyWordToAudio(self, Keywords, lenPerPages, filename):
        print("Collecting detials...")
        paragraph = self.KeyWordToPara(Keywords,lenPerPages)
        string = ""
        for i in range(8):
            string = string + str(paragraph[i])
        print(string)
        print()
        print("Audio converting....")
        self.textTOVoice(string,"en",filename)

    def KeyWordToimage(self, Keyword, limit, dir_name):
        arr = Keyword.split(",")
        for i in range(len(arr)):
            downloader.download(arr[i], limit=limit,  output_dir=dir_name, 
            adult_filter_off=True, force_replace=False, timeout=60)


a=kit()
#print(a.KeyWordToAudio("iron man",2,"iron.mp3"))
print(a.TextToHand("spider helndfbwo fwufbwf iwufbiuwefiuwu fuweef dv","/home/nagi/Desktop/group/website/ClassRoomTools/app/routes/Tools"))
