from ..cuit import Cuit 

def test_cuit_true():
    c = "20337196439"
    assert Cuit().verificador(c) == True
    
def test_cuit_false():
    c = ["33719643", "11337196439"]
    assert Cuit().verificador(c[0]) == False

def test_cuit_int():
    with pytest.raises(ValueError):
        Cuit().verificador(20337196439)
