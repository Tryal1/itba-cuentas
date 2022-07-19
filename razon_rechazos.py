import json

parametros_classic = {
        "tarjeta_debito" : 1,
        "cuenta_corriente" : 0,
        "caja_ahorro_peso" : 1,
        "caja_ahorro_dolar" : 0,
        "compra_venta_dolar" : False,
        "retiro_maximo" : 10_000,
        "tarjeta_credito" : 0,
        "chequera" : 0,
        "comision_transaccion" : 0.01,
        "limite_transferencia" : 150_000,
        "monto_descubierto" : 0
}

paramtetros_gold = {
        "tarjeta_debito" : 1,
        "cuenta_corriente" : 1,
        "caja_ahorro_peso" : 1,
        "caja_ahorro_dolar" : 1,
        "compra_venta_dolar" : True,
        "retiro_maximo" : 20_000,
        "tarjeta_credito" : 1,
        "chequera" : 1,
        "comision_transaccion" : 0.005,
        "limite_transferencia" : 500_000,
        "monto_descubierto" : 10_000,
}

parametros_black = {
        "cuenta_corriente" : 1,
        "caja_ahorro_peso" : 1,
        "caja_ahorro_dolar" : 1,
        "compra_venta_dolar" : True,
        "retiro_maximo" : 100_000,
        "tarjeta_credito" : 5,
        "chequera" : 2,
        "comision_transaccion" : 0,
        "limite_transferencia" : 100_000_000,
        "monto_descubierto" : 10_000,
}

def razon_rechazos(estado, tipo_operacion, cupo_diario_restante, monto, saldo_cuenta, total_tarjetas_activas, total_chequeras_activas, parametros):

    retiro_maximo = parametros["retiro_maximo"]
    limite_transferencia = parametros["limite_transferencia"]
    monto_descubierto = parametros["monto_descubierto"]
    cantidad_chequeras_disponibles = parametros["chequera"]
    cantidad_tarjetas_disponibles = parametros["tarjeta_credito"]

    if estado == "RECHAZADA":
        
        if tipo_operacion ==  "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":

            if monto > retiro_maximo:

                return "El monto excede el limite de retiro"

            elif monto > cupo_diario_restante:

                return "El monto excede el cupo diario restante"

            elif monto > saldo_cuenta + monto_descubierto:

                return "El monto excede el saldo de la cuenta más el monto descubierto" 

        elif tipo_operacion == "ALTA_TARJETA_CREDITO":

            if total_tarjetas_activas >= cantidad_tarjetas_disponibles:

                return "Ya se cuenta con el limite de tarjetas de credito"

        elif tipo_operacion == "ALTA_CHEQUERA":

            if total_chequeras_activas >= cantidad_chequeras_disponibles:

                return "Ya se cuenta con el limite de chequeras"

        elif tipo_operacion == "COMPRA_DOLAR":

                if saldo_cuenta + monto_descubierto:

                    return "El monto excede el saldo de la cuenta"

        elif tipo_operacion == "TRANSFERENCIA_ENVIADA":
            
            if monto >= 150_000:

                return "El monto excede el limite de transferencia del destinatario"

        elif tipo_operacion == "TRANSFERENCIA_RECIBIDA":

            if monto >= limite_transferencia:

                return "El monto excede el limite de transferencia"

        else:

            return "Error no reconocido por el sistema"

def chequear_razon(data, usuario):

    for transaccion in data["transacciones"]:
        
        estado = transaccion["estado"]
        tipo_operacion = transaccion["tipo"]
        cupo_diario_restante = transaccion["cupoDiarioRestante"]
        monto = transaccion["monto"]
        saldo_cuenta = transaccion["saldoEnCuenta"]
        total_tarjetas_activas = transaccion["totalTarjetasDeCreditoActualmente"]
        total_chequeras_activas = transaccion["totalChequerasActualmente"]
        cupo_diario_restante = transaccion["cupoDiarioRestante"]

        if usuario == "classic":

            parametros = parametros_classic

        elif usuario == "gold":

            parametros = paramtetros_gold

        elif usuario == "black":

            parametros = parametros_black


        razon = razon_rechazos(estado, tipo_operacion, cupo_diario_restante, monto, saldo_cuenta, total_tarjetas_activas, total_chequeras_activas, parametros) 
        transaccion["razon_de_rechazo"] = razon
    
    with open(f"static/output/json/output_{usuario}.json", "w") as file:
        json.dump(data, file)

def obtener_razones():

    tipo_usuarios = ["classic", "gold", "black"]

    for usuario in tipo_usuarios:
    
        with open(f'static/input/eventos_{usuario}.json') as f:

                data = json.load(f)   

        chequear_razon(data, usuario)

obtener_razones()