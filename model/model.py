from database.meteo_dao import MeteoDao

class Model:
    def __init__(self):
        self.dao = MeteoDao()

    def getAllSituazioni(self):
        return self.dao.get_all_situazioni()

if __name__ == "__main__":
    m = Model()
    print(m.getAllSituazioni())