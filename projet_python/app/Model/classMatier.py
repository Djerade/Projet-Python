class Matier:
    def __init__(self ) -> None:
        self.titre  = ""
        self.credit  = 0
        self.heure  = 0
        
    def __str__(self) -> str:
        return self.titre + "   " + str(self.credit) + "   " + str(self.heure)
    
    def heur_restante(self):
        return self.heure
    
    def update_time(self, hr):
        if (hr <= 3):
            self.heure -= hr
        else:
            self.heure -= 3
    