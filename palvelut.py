import random

class Asiakas:
    """Luokka jossa syötetään asiakkaan tiedot
    :ivar __nimi: asiakkaan nimi
    :type __nimi: str
    :ivar __asiakasnro: asiakkaan numero
    :type __asiakasnro: int
    :ivar __ika: asiakkaan ikä
    :type __ika: int
     Julkiset metodit:
    set_nimi()
    set_ika()
    set_numero()

      yksityiset metodit:
    __luo_nro()
    """


    def __init__(self, nimi, ika):
        """Konstruktori"""
        self.nimi = nimi
        self.asiakasnumero = self.__luo_nro()
        self.ika = ika
  
    def __luo_nro(self):
        """
        metodi joka, valitse asiakkaan numerot
        :return: number
        :rtype: list(int)
        """

        number = []

        number.append(random.randint(0, 99))
        number.append(random.randint(0, 999))
        number.append(random.randint(0, 999))

        return number
  
    def set_nimi(self, uusinimi):
        """
        Palauttaa nimi.
        """

        if uusinimi == False:
            raise ValueError("Anna uusi nimi")
        if uusinimi == True:
            self.__nimi = uusinimi
  
    def set_ika(self):
        """
        palauttaa iän
        """
        try:
            return Asiakas.__ika
        except:
            pass

    def set_numero(self):
        """
        sijoittaa asikkaan numerot ja palauttaa niitä
        """
        return f'{Asiakas.__asiakasnumero[0]:02}-{Asiakas.__asiakasnumero[1]:03}-{Asiakas.__asiakasnumero[2]:03}'

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

    def __init__(self, tuotenimi):
        """konstruktori"""
        self.tuotenimi = tuotenimi
        self.__asiakkaat = []

    def _luo_asiakarivi(self, asiakas: Asiakas) -> str:
        return f"{asiakas.nimi} ({asiakas.asiakasnumero}) on {asiakas.ika}-vuotias."
        """lisaa asikkaan tiedot"""
    def lisaa_asiakas(self, asiakas: Asiakas):
        """lisaa asiakas asiakas listaan"""
        if(asiakas):
            self.__asiakkaat.append(asiakas)

        else:
            raise ValueError("Uusi nimi on annettava.")    

    def poista_asiakas(self, asiakas: Asiakas):
        """poistaa asikas asiakas listasta"""
        try:
            self.__asiakkaat.remove(asiakas)
        except:
            print("Asiakas on annettava.")
            pass    

    def tulosta_asiakkaat(self):
        """Tulostaa asikas"""
        print(f"\nTuotteen {self.tuotenimi} asiakkaat ovat:")
        for asiakas in self.__asiakkaat:
            print(self._luo_asiakarivi(asiakas))        

class ParempiPalvelu(Palvelu):
    """ParempiPalvelu luokka
    :ivar edut: palvelun edut
    :type edut: str, list
    Julkiset metodit
        _lisaa_etu(str)
        _poista_etu(str)
        _tulosta_edut()
    """

    def __init__(self, tuotenimi):
        """konstruktori"""
        super().__init__(tuotenimi)
        self.edut = []

    def lisaa_etu(self, d: str):
        """lisaa edut edut listaan"""
        if(d):
            self.edut.append(d)
        else:
            raise Exception("se meni ohi.")     

    def poista_etu(self, d: str):
        """poistaa edut edut listasta"""
        try:
            self.__edut.remove(d)
        except:
            print("Uusi asiakas on annettava.")
            pass     

    def tulosta_edut(self):
        """tulostaa asikkaan edut"""
        print(f"Tuotteen {self.tuotenimi} edut ovat:")
        for edut in self.edut:
            print(f"{edut}")
