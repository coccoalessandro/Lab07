import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0

    def handle_umidita_media(self, e):

        self._view.lst_result.controls.clear()

        myModel = Model()

        mediaGenova = []
        mediaTorino = []
        mediaMilano = []

        for situazione in myModel.getAllSituazioni():
            if situazione.data.month == int(self._view.dd_mese.value):
                if situazione.localita == "Genova":
                    mediaGenova.append(int(situazione.umidita))
                elif situazione.localita == "Torino":
                    mediaTorino.append(int(situazione.umidita))
                else:
                    mediaMilano.append(int(situazione.umidita))


        self._view.lst_result.controls.append(ft.Text("L'umidità media nel mese selezionato è:"))
        self._view.lst_result.controls.append(ft.Text(f"Genova: {round(sum(mediaGenova)/len(mediaGenova), 4)}"))
        self._view.lst_result.controls.append(ft.Text(f"Milano: {round(sum(mediaMilano) / len(mediaMilano), 4)}"))
        self._view.lst_result.controls.append(ft.Text(f"Torino: {round(sum(mediaTorino) / len(mediaTorino), 4)}"))
        self._view.update_page()

    def handle_sequenza(self, e):
        pass

    def read_mese(self, e):
        self._mese = int(e.control.value)

