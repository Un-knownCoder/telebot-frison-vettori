from random import randint
class handler:
  def __init__(self):
    tmp = open('./data/data.txt').read().split('\n')
    self.pazienti = []
    self.dati = {}

    for t in tmp:
      t = t.split('#')
      idp = t[0]
      nome = t[1]
      cognome = t[2]
      indirizzo = t[3]

      self.pazienti.append({'id': idp, 'nome': nome, 'cognome': cognome, 'indirizzo': indirizzo})

  def genData(self):
    for p in self.pazienti:
      SpO2 = randint(85, 100)
      FC = randint(60, 130)
      Pi = randint(80, 90)
      FR = randint(10, 20)
      self.dati[p['id']] = {'SpO2': SpO2, 'FC': FC, 'Pi': Pi, 'FR': FR}

  def getPatientById(self, pid):
    for p in self.pazienti:
      if (p['id'] == pid):
        return p

    return None


  def getCritical(self):
    critici = []
    for k in self.dati:
      if (self.dati[k]['SpO2'] <= 92):
        p = self.getPatientById(k)
        if (not p == None):
          critici.append({'paziente': p, 'valore': self.dati[k]['SpO2']})

    return critici
