class EmpploieMois():
    def __init__(self) -> None:
      self.list = []
    
    def add_matier(self, item):
        self.list.append(item)
        
    def get_list(self):
      return self.list
    
    def printEmpoi(self):
      for ue in self.list:
        print (ue)
        
    def size_list(self):
      return len(self.list)