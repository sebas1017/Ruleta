import random
def spins():
    global slots
    slots = { '0': 'green', '1': 'red', '2': 'black',
             '3': 'red', '4': 'black', '5': 'red', '6': 'black', '7': 'red',
             '8': 'black', '9': 'red', '10': 'black', '11': 'red',
             '12': 'black', '13': 'red', '14': 'black', '15': 'red',
             '16': 'black', '17': 'red', '18': 'black', '19': 'red',
             '20': 'black', '21': 'red', '22': 'black', '23': 'red',
             '24': 'black', '25': 'red', '26': 'black', '27': 'red',
             '28': 'black', '29': 'red', '30': 'black', '31': 'red',
             '32': 'black', '33': 'red', '34': 'black', '35': 'red',
             '36': 'black'}
    result = random.choice(list(slots.keys()))
    return result


def jugar_ruleta(cantidad_jugadores,nombre_jugador,monto_jugador):
    jugadores_tuplas =[]
    resultados ={"RONDAS":[]}
    rondas = 1
    for k in range(cantidad_jugadores):
        jugadores_tuplas.append((nombre_jugador,[monto_jugador]))
    
    jugadores =    dict(jugadores_tuplas)
    for llave,valor in jugadores.items():
        valor.append([])
        valor.append([])
        valor.append([])
        valor.append([])
        valor.append([])
    
    print(jugadores)
    print("MODOS DE JUEGO")
    print("1:Negro o Rojo \n"
          "2: Numero en especifico")
    opcion = int(input("INGRESE EL MODO DE JUEGO: "))
    ronda_actual = 0
    if opcion == 1:
       while(rondas!=0):
            print(20*"*____*")
            for llave, valor in jugadores.items():
                print(f"EL MONTO DE DINERO ACTUAL DEL JUGADOR :{llave} ES: {valor[0]}")
            print(f"RONDA... {ronda_actual}")
            for llave,valor in list(jugadores.items()):
                print(f"EL MONTO DE DINERO ACTUAL DEL JUGADOR :{llave} ES: {valor[0]}")
                print("FAVOR INGRESE LA OPCION DE APUESTA DE ESTE JUGADOR ¿PAR(2) O IMPAR(1)?\n")
                opcion_subjuego = int(input(" "))
                valor[1].append(opcion_subjuego)
                
            for llave, valor in jugadores.items():
                  if valor[0] <= 1000:
                         valor[3].append(int(1000))      
                  if valor[0] > 1000:
                    porcentaje11 = (valor[0]*11)/100
                    porcentaje19 = (valor[0]*19)/100
                    valor[4].append((int(porcentaje11),int(porcentaje19)))
                    print("RECUERDE QUE AL TENER UN MONTO MAYOR A 1000 DEBE APOSTAR ENTRE EL 11% Y EL 19% DE SU MONTO TOTAL")
                    print(f"O PUEDE APOSTAR TODO SU DINERO QUE ACTUALMENTE ES : {valor[0]}")
                    print(f"EL MONTO MINIMO Y MAXIMO QUE PUEDE APOSTAR EL JUGADOR {llave}, SON {valor[4][-1]}")
                    
                    print(f"CUANTO DESEA APOSTAR JUGADOR {llave}")
                    valor_apuesta = input(" ")
                    if valor_apuesta  =='':
                        print("favor ingresar un monto para apostar: ")
                    valor_apuesta = int(valor_apuesta)
                    valor[3].append(valor_apuesta)
                   
                        
            resultado =int(spins())
            for llave , valor in list(resultados.items()):
                valor.append(resultado)
                
            print(f"EL RESULTADO DE LA RULETA ES {resultado}")
            for llave, valor in list(jugadores.items()):
                if resultado %2 ==0 :
                    ultima_apuesta_jugador = valor[1][-1]
                    ultimo_valor_apuesta = valor[3][-1]
                    if ultima_apuesta_jugador == 2:
                        valor[5].append(1)
                        print(f"EL JUGADOR {llave} HA GANADO {ultimo_valor_apuesta}")
                        valor[0]+=ultimo_valor_apuesta
                    else:
                        print(f"EL JUGADOR {llave} HA PERDIDO  {ultimo_valor_apuesta}")
                        valor[5].append(-1)
                        valor[0]-=ultimo_valor_apuesta
                if resultado %2 !=0:
                    ultimo_valor_apuesta = valor[3][-1]
                    ultima_apuesta_jugador = valor[1][-1]
                    if ultima_apuesta_jugador == 1:
                        valor[5].append(1)
                        print(f"EL JUGADOR {llave} HA GANADO {ultimo_valor_apuesta}")
                        valor[0]+=ultimo_valor_apuesta
                    else:
                        valor[5].append(-1)
                        print(f"EL JUGADOR {llave} HA PERDIDO {ultimo_valor_apuesta}")
                        valor[0]-= ultimo_valor_apuesta
                 
                     
              
            for llave,valor in list(jugadores.items()):
                if valor[0] ==0:
                    print(f"EL JUGADOR {llave} HA SIDO ELIMINADO PORQUE NO TIENE DINERO")
                    del jugadores[llave]
            rondas-= 1
            ronda_actual+=1
        
    print(jugadores)
    print("RESULTADOS")
    print(resultados)
    if jugadores == {}:
        print("NO QUEDARON JUGADORES TODOS FUERON ELIMINADOS PORQUE PERDIERON SU DINERO")
    else:    
        for llave , valor in jugadores.items():
            cantidad_rondas_ganadas = valor[5].count(1)
            cantidad_rondas_perdidas = valor[5].count(-1)
            print(f"JUGADOR {llave} GANO {cantidad_rondas_ganadas} RONDAS")
            print(f"JUGADOR {llave} PERDIO {cantidad_rondas_perdidas} RONDAS")
            
jugar_ruleta()    

    
    