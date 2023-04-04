from app.mini_calc import Mini_Calc

class TestMiniCalcImpartire():
    def setup_method(self):
        print ('IMPARTIRE - iNSTRUCTIUNE EXECUTATA LA INCEPUT!')
        self.calc = Mini_Calc()
        # daca punem self aici, noi facem din variabila 'calc' un atribut de clasa
        # daca nu punem self aici, atunci variabila e vizibila doar in cadrul metodei de setup_method()
    def teardown_method(self):
        print('IMPARTIRE - Instructiuni executate la final!')
    '''
    !!!! TOATE METODELE DE TEST TREBUIE SA INCEAPA SI CU "TEST"
    '''
    def test_impartire(self):
        assert self.calc.impartire(6, 3) == 2, 'Eroare ...Nu functioneaza cum trebuie!'

    def test_impartire1(self):
        assert self.calc.impartire(-6, 3) == -2, 'Eroare ...Nu functioneaza cum trebuie!'

    def test_impartire2(self):
        assert self.calc.impartire(-6, -3) == 2, 'Eroare ...Nu functioneaza cum trebuie!'

    # def test_impartire3(self):
    #     assert self.calc.impartire(2, 0) == 0, 'Eroare ...Nu functioneaza cum trebuie!'
    #
    # def test_inmultire4(self):
    #     assert self.calc.inmultire(-2, 0) == 0, 'Eroare ...Nu functioneaza cum trebuie!'