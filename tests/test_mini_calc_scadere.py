from app.mini_calc import Mini_Calc


class TestMiniCalcScadere():
    def setup_method(self):
        print('SCADERE - iNSTRUCTIUNE EXECUTATA LA INCEPUT!')
        self.calc = Mini_Calc()
        # daca punem self aici, noi facem din variabila 'calc' un atribut de clasa
        # daca nu punem self aici, atunci variabila e vizibila doar in cadrul metodei de setup_method()

    def teardown_method(self):
        print('SCADERE - Instructiuni executate la final!')

    '''
    !!!! TOATE METODELE DE TEST TREBUIE SA INCEAPA SI CU "TEST"
    '''

    def test_scadere(self):
        assert self.calc.scadere(8, 4) == 4, 'Eroare ...Nu functioneaza cum trebuie!'

    def test_scadere1(self):
        assert self.calc.scadere(8, -4) == 12, 'Eroare ...Nu functioneaza cum trebuie!'

    def test_scadere2(self):
        assert self.calc.scadere(-8, -4) == -4, 'Eroare ...Nu functioneaza cum trebuie!'