def calcularsalario (horas, tarifas):
    horas_extra = horas - max_horas_semanales
    if (horas_extra > 0):
        pago = (max_horas_semanales * tarifa) + (horas_extra * (tarifa * 1.5))
    else: 
        pago = (horas * tarifa)
    return pago

try : 
        max_horas_semanales = 40
        horas = int (input ("ingrese numero de horas?"))
        tarifa = float(input ("Ingrese tarifa por hora?"))
        salario = calcularsalario (horas,tarifa)
        print( salario )

except:
        print:("Error, debe ingresar valor numerico")
