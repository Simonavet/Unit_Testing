class Mini_Calc:
    #Tipuri de constructori:
    # * constructor implicit = atunci cand nu defineste utilizatorul un constructor si se foloseste automat din pyton
    # * constructoe explicit = cand utilizatorul defineste un constructor pt a controla initializarea unor atribute
    # * constructor explicit
    # def __init__(self, a, b):
    #     self.a = a
    #     self.b = b

    # 1.ADUNARE
    def adunare(self, a, b):
        return a+b

    # def adunare(self, a, b):
        #return self.a+self.b

    # 2. SCADERE
    def scadere(self, a, b):
        return a-b

    # 3. INMULTIRE
    def inmultire(self, a, b):
        return a*b

    # 4. IMPARTIRE
    def impartire(self, a, b):
        return a/b