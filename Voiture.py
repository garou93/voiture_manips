# -*- coding: utf-8 -*-


class Voiture:

    def __init__(self):     # constructeur
        self.nom = "Ferrari"   # nom attribut de classe
        
    def donne_moi_le_modele(self):
        return "250"

    def allumer(self):
        print("La voiture démarre")

#    def _get_roues(self):
#        print "Récupération du nombre de roues"
#        return self._roues

#    def _set_roues(self, v):
 #       print "Changement du nombre de roues"
#        self._roues  =  v

#    roues=property(_get_roues, _set_roues)
        
    @property
    def roues(self):
        print("Récupération du nombre de roues")
        return self._roues

    @roues.setter
    def roues(self, v):
        print("Changement du nombre de roues")
        self._roues  =  v
        
#heritage de classe
        
class VoitureSport(Voiture):

	def __init__(self):
		self.nom = "Ferrari"    

#polymorphisme
        
#ma_voiture_sport = VoitureSport()
#ma_voiture_sport.allumer()
        
class VoitureEncaps :
	
  def __init__ (self, im)  :
      self.__Compteur = 0
      self.__Immat = im
	
  def ChangerPneu (self) :
      return (self.__Compteur >= 10000)    
	
  def getCompteur (self) :
      return self.__Compteur
	
  def setCompteur (self, km) :
      self.__Compteur = km
		
  def getImmat (self) :
      return self.__Immat
	
  def setImmat (self,im) :
      self.__Immat = im
