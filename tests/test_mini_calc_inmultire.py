from app.mini_calc import Mini_Calc

class TestMiniCalcInmultire():
    def setup_method(self):
        print ('INMULTIRE - iNSTRUCTIUNE EXECUTATA LA INCEPUT!')
        self.calc = Mini_Calc()
        # daca punem self aici, noi facem din variabila 'calc' un atribut de clasa
        # daca nu punem self aici, atunci variabila e vizibila doar in cadrul metodei de setup_method()
    def teardown_method(self):
        print('INMULTIRE - Instructiuni executate la final!')
    '''
    !!!! TOATE METODELE DE TEST TREBUIE SA INCEAPA SI CU "TEST"
    '''
    def test_inmultire(self):
        assert self.calc.inmultire(2, 3) == 6, 'Eroare ...Nu functioneaza cum trebuie!'

    def test_inmultire1(self):
        assert self.calc.inmultire(-2, 3) == -6, 'Eroare ...Nu functioneaza cum trebuie!'

    def test_inmultire2(self):
        assert self.calc.inmultire(-2, -3) == 6, 'Eroare ...Nu functioneaza cum trebuie!'

    def test_inmultire3(self):
        assert self.calc.inmultire(2, 0) == 0, 'Eroare ...Nu functioneaza cum trebuie!'

    def test_inmultire4(self):
        assert self.calc.inmultire(-2, 0) == 0, 'Eroare ...Nu functioneaza cum trebuie!'