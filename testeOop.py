class Artista:
    
    def __init__(self) -> None:
        self._name = []
        self.qtdeSongs = 0
        
    def addNameArtista(self):
        while True:
            # Mostra o bt de proximo, só quando o usuário já add um artista
            print('[p] => Proxima etapa')
            name = input('Nome do Artista/Banda: ').title().strip()
            if name == 'P':
                break
            self._name.append([name])
    
    def getNameArtista(self):
        return self._name
        
        
    
        
    