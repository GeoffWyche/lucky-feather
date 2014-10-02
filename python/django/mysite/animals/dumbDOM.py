# base class for all gDOMObj objects
class gDOMObj:
    pass

class gTitle(gDOMObj):
    title_str = "(Empty Title)"
    def __init__(self):
        self.title_str = "(Default Title)"
    def __init__(self,title="(Default Title)"):
        self.title_str = title
    def __str__(self):
        output = "<title>" + self.title_str + "</title>"
        return output
    
class gHead(gDOMObj):
    title = gTitle()
    def __init__(self):
        self.title = gTitle()
    def __init__(self,title="(gHead default title)"):
        self.title = gTitle(title)
    def __str__(self):
        output = "<head>" + self.title.__str__() + "</head>"
        return output

class gText(gDOMObj):
    text = ""
    def __init__(self, text=""):
        self.text = text
    def __str__(self):
        return self.text
    
class gBodyText(gText):
    pass

class gButton(gBodyText):
    def __init__(self,label='Button',nodeid='1'):
        self.label = label
        self.nodeid = nodeid
        print("creating button with label: " + self.label +
              "and nodeid: " + self.nodeid)
        self.text = '<a href="/animals/' + self.nodeid + '"/>'
        self.text += self.label
        self.text += '</a>'
    def __str__(self):
        return self.text

class gBody(gDOMObj):
    def __init__(self,contents=[]):
        self.contents = contents
    def __str__(self):
        output = "<body>"
        print("gBody has " + len(self.contents).__str__() +" objects")
        for i in range(len(self.contents)):
            print("adding: " + self.contents[i].__str__())
            output = output + self.contents[i].__str__()
        output = output + "</body>"
        return output
    
class gDOM(gDOMObj):
    head = gHead()
    body = gBody("plain contents")
#    def __init__(self):
#        pass
    def __init__(self,head=gHead(),body=gBody("default plain contents")):
        self.head = head
        self.body = body
    def render(self):
        return self.__str__()
    def __str__(self):
        output = "<html>" + self.head.__str__() + self.body.__str__() + "</html>"
        return output

def gDOMTest():
#    print("gDOMTest")
    dom = gDOM(head=gHead("Animals Game"),
               body=gBody([gBodyText("bodytext1"),
                           gBodyText("bodytext2"),
                           gButton(),
                       ]))
    print(dom.__str__())

# module test
#print("calling gDOMTest")
gDOMTest()
#print("gDOMTest complete")


