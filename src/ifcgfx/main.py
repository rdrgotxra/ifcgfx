import ifcopenshell as ifc
import pygfx as gfx

class View:
    """Viewport associada a um modelo IFC."""
    def __init__(self, ifc: ifc.file) -> None:
        # na verdade aqui ele já deve configurar a viewport, só n vai gerar
        # não vai configurar a geometria ainda, apenas em show
        self.ifc = ifc
        self.geom = None

    def show(self):
        # trata os dados de self.ifc, extrai geometria => geom
        # cria uma viewport pygfx configurada com geom
        # geom fica salvo em self.geom, representa apenas a geometria em si
        # essa função recarrega a vista, o modelo do zero
        pass

    def update(self):
        # essa função deve verificar a geom atual
        # vai comparar com a nova, algo como diff da propria geometria
        # vai enviar para o pygfx apenas os dados que foram alterados
        #
        pass


def get_geom(ifc.file):
    pass
