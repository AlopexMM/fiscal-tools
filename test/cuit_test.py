from afip.cuit import Cuit

def test_verificador():
    assert True == Cuit().verificador("20337196439")

def test_calcular_cuit():
    assert "20337196439" == Cuit().calcular_cuil(dni="33719643",gender="M")


