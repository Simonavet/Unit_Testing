from app.mini_calc import Mini_Calc

class TestMiniCalcAdunare():
    def setup_method(self):
        print ('ADUNARE - iNSTRUCTIUNE EXECUTATA LA INCEPUT!')
        self.calc = Mini_Calc()
        # daca punem self aici, noi facem din variabila 'calc' un atribut de clasa
        # daca nu punem self aici, atunci variabila e vizibila doar in cadrul metodei de setup_method()
    def teardown_method(self):
        print('ADUNARE - Instructiuni executate la final!')
    '''
    !!!! TOATE METODELE DE TEST TREBUIE SA INCEAPA SI CU "TEST"
    '''
    def test_adunare(self):
        assert self.calc.adunare(8, 4) == 12, 'Eroare ...Nu functioneaza cum trebuie!'

    def test_adunare1(self):
        assert self.calc.adunare(8, -4) == 4, 'Eroare ...Nu functioneaza cum trebuie!'

    def test_adunare2(self):
        assert self.calc.adunare(-8, -4) == -12, 'Eroare ...Nu functioneaza cum trebuie!'