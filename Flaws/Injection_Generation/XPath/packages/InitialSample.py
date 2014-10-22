#constante
safe = "safe"
unsafe = "unsafe"
needQuote = "needQuote"
quote = "quote"
noQuote = "noQuote"

integer = "int"


#Manages initial samples, which are created to generate final samples by combination
class InitialSample :
    def __init__(self, initialSample) :
        self.path = []
        tree_path = initialSample.find("path").findall("dir")
        for dir in tree_path :
            self.path.append(dir.text)
            
        self.comment = initialSample.find("comment").text
        self.code = initialSample.find("code").text
        self.relevancy = float(initialSample.find("relevancy").text)

class InputSample(InitialSample) :
    def __init__(self, initialSample) :
        InitialSample.__init__(self,initialSample)
        self.inputType = initialSample.find("inputType").text

class Sanitize(InitialSample) :
    def __init__(self, initialSample) :
        InitialSample.__init__(self,initialSample)
        safety = initialSample.find("isSafe")
        if safety.get("safe") == "1" :
            self.isSafe = safe
        elif safety.get("needQuote") == "1" :
            self.isSafe = needQuote
        elif safety.get("needQuote") == "-1" :
            self.isSafe = noQuote        
        else :
            self.isSafe = unsafe

        constraint = initialSample.find("constraint")
        self.constraintType = constraint.get("type")
        self.constraintField = constraint.get("field")
        

class Construction(InitialSample): 
    def __init__(self, initialSample) :
        InitialSample.__init__(self,initialSample)
        safety = initialSample.find("isSafe")

        if safety.get("safe") == "1":
            self.isSafe = safe
        elif safety.get("quote") == "1" :
            self.isSafe = quote
        else :
            self.isSafe = 0

        constraint = initialSample.find("constraint")
        self.constraintType = constraint.get("type")
        self.constraintField = constraint.get("field")
