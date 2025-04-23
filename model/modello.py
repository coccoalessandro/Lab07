import copy

from database.meteo_dao import MeteoDao

class Model:
    def __init__(self):
        self.n_soluzioni = 0
        self.costo_ottimo = -1
        self.soluzione_ottima = []

    def calcola_sequenza(self, mese):
        situazioni = MeteoDao.get_situazioni_meta_mese(mese)
        self.ricorsione([], situazioni)
        return self.soluzione_ottima, self.costo_ottimo

    def trova_possibili_step(self, parziale, lista_situazioni):
        giorno = len(parziale)+1
        candidati = []
        for situazione in lista_situazioni:
            if situazione.data.day == giorno:
                candidati.append(situazione)

        return candidati

    def is_admissible(self, candidate, parziale):
        # vincolo sui 6 giorni
        counter = 0
        for situazione in parziale:
            if situazione.localita == candidate.localita:
                counter += 1
        if counter >= 6:
            return False

        #vincolo sulla permanenza
            #1) Lunghezza di parziale < 3
        if len(parziale) == 0:
            return True
        if len(parziale) < 3:
            if candidate.localita != parziale[0].localita:
                return False
            #2) Le tre situazioni precedenti non sono tutte uguali
        else:
            if parziale[-3].localita != parziale[-2].localita or parziale[-3].localita != parziale[-1].localita or parziale[-1].localita != parziale[-2].localita:
                if parziale[-1].localita != candidate.localita:
                    return False
        # altrimenti OK
        return True

    def calcola_costo(self, parziale):
        costo = 0
        for situazione in parziale:
            costo += situazione.umidita

        # for i in range(len(parziale)):
        #     if i >= 2 and parziale[i-1].localita != parziale[i].localita:
        #         costo += 100

        return costo


    def ricorsione(self, parziale, lista_situazioni):
        if len(parziale) == 15:
            self.n_soluzioni += 1
            costo = self.calcola_costo(parziale)
            if self.costo_ottimo == -1 or self.costo_ottimo > costo:
                self.costo_ottimo = costo
                self.soluzione_ottima = copy.deepcopy(parziale)
        else:
            #cercare le città per il giorno che mi serve
            candidates = self.trova_possibili_step(parziale, lista_situazioni)
            #provo as aggiungere una di queste città e vado avanti
            for candidate in candidates:
                if self.is_admissible(candidate, parziale):
                    parziale.append(candidate)
                    self.ricorsione(parziale, lista_situazioni)
                    parziale.pop()

        return self.soluzione_ottima, self.costo_ottimo

if __name__ == "__main__":
    m = Model()
    print(m.calcola_sequenza(1))
