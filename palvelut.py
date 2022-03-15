class Asiakas:
    """Luokka jossa syötetään asiakkaan tiedot
    :ivar __nimi: asiakkaan nimi
    :type __nimi: str
    :ivar __asiakasnro: asiakkaan numero
    :type __asiakasnro: int
    :ivar __ika: asiakkaan ikä
    :type __ika: int
    Julkiset metodit
        __luo_nro()
    """

    def __init__(self):
        """konstruktori"""
        self.__nimi = ""
        self.__asiakasnro = self.__luo_nro()
        self.__ika = ""

class Palvelu:
    """Palvelu luokka
    :ivar tuotenimi: tuotteen nimi
    :type tuotenimi: str
    :ivar __asiakkaat: lista asiakkasita
    :type __asiakkaat: list
    Julkiset metodit
        _luo_asiakasrivi(Asiakas)
        lisaa_asiakas(Asiakas)
        poista_asiakas(Asiakas)
        tulosta_asiakkaat()
    """

    def __init__(self):
        """konstruktori"""
        self.tuotenimi = tuotenimi
        self.__asiakkaat = asiakkaat()

    def _luo_asiakarivi(self, asiakas: Asiakas) -> str:
        return f"{asiakas.nimi} ({asiakas.asiakasnro}) on {asiakas.ika}-vuotias."

    def lisaa_asiakas(self, asiakas: Asiakas):
        if(asiakas):
            self.__asiakkaat.append(asiakas)

        else:
            raise Exception("Se meni ohi.")    

    def poista_asiakas(self, asiakas: Asiakas):
        try:
            self.__asiakkaat.remove(asiakas)
        except:
            print("Ei lyötynyt.")
            pass    

    def tulosta_asiakkaat(self):
        print(f"Tuotteen {self.__asiakkaat[-1]} asiakkaat ovat:")
        print(self._luo_asiakarivi)        

class ParempiPalvelu:
    """ParempiPalvelu luokka
    :ivar edut: palvelun edut
    :type edut: str, list
    Julkiset metodit
        _lisaa_etu(str)
        _poista_etu(str)
        _tulosta_edut()
    """

    def __init__(self):
        """konstruktori"""
       super(ParempiPalvelu, self).__init__(tuotenimi)
        self.edut = edut[]

    def lisaa_etu(self, d: str):
        if(d):
            self.__edut.append(d)
        else:
            raise Exception("se meni ohi.")     

    def poista_etu(self, d: str):
        try:
            self.__edut.remove(d)
        except:
            print("Ei lyötynyt.")
            pass     

    def tulosta_edut(self):
        print(f"Tuotteen {self.__asiakkaat} edut ovat:")
        print(f"Jauhaa {self.__edut}.")               
