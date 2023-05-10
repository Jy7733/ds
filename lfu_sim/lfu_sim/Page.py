from heap import Heap

h = Heap
class Page :
    def __init__(self,number) :
        self.number = number
        self.count = 0

    def __lt__ (self,other) :
        return self.count < other.count
    
    def __eq__(self,other) :
        return self.number == other.number
    

class LFUSimunl :a
    def __init__(self,capacity) :
        self.capacity = capacity
        self.pages = []
        self.page_map = {}

    def get_page(self,page_num) :
        if page_num in self.page_map :
            page = self.page_map[page_num]
            page.count+=1
            for i in page :
                h.insert(i)
            return page
        return None
    
    def add_page(self,page_num) :
        if len(self.pages) >= self.capacity :
            page = h.deleteMin(self.pages)
        page = Page(page_num)
        for i in page :
            h.insert(i)
        self.page_map[page_num] = page


            
         

            




