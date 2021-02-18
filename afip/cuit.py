""" 
This class resolve issues related with CUIT and CUIL
"""

class Cuit:
    
    def verificador(self, cuit: str):
        """
            Check if the cuit it is ok
            :return True

            Else
            :return False
            
            When the cuit is an int
            :raise ValueError 
        """

        try:
            
            if len(cuit) == 11:
                if cuit[:2] in ["20","27","30"]:
                    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
                    aux = 0
                    for i in range(10):
                        aux += int(cuit[i]) * base[i]
                    aux = 11 - (aux % 11)
                    if aux == 11:
                        aux = 0
                    elif aux == 10:
                        aux = 9
                    if int(cuit[10]) == aux:
                        return True
                    else:
                        return False
            else:
                return False
        except ValueError:
            print("El cuit debe ser string")
            raise 
    
    def calcular_cuil(self, dni):
        pass
