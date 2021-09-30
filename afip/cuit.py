"""
This class resolve issues related with CUIT and CUIL
"""

class Cuit(object):
    def verificador(self, cuit):
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
            return False
        except ValueError:
            print("The cuit must be string")
            return False

    def calcular_cuil(self, dni, gender):
        """
            :return str of cuil from dni an gender
            gender must be M for male and F for female
        """
        try:
            if gender == "M":
                cuil = [f"20{dni}9" ,f"23{dni}9"]
                if self.verificador(cuil[0]):
                    return cuil[0]
                elif self.verificador(cuil[1]):
                    return cuil[1]
            if gender == "F":
                cuil = [f"27{dni}4",f"23{dni}4"]
                if self.verificador(cuil[0]):
                    return cuil[0]
                elif self.verificador(cuil[1]):
                    return cuil[1]
            raise ValueError
        except ValueError:
            print("The cuil do not pass verification try with another DNI or gender")
