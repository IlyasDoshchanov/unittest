import view
import model

class Presenter:
    def __init__(self):
        self._model = model.Model()
        self._view = view.View(self)

    def GetCoverImage(self, name):
        return self._model.getImage(name)

    def getAlbums(self):
        return self._model.getAlbumsSQL()

    def getTrackList(self, album_title):
        return self._model.getTrackListSQL(album_title)

