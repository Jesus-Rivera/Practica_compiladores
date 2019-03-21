def recorres2(nodos,simbolos,indice,cadena,camino,total):
	temp = camino
	if nodos[indice].numero != -1:
		if len(cadena) == 0:
			if nodos[indice].final == True:
				mostrar(temp,total)
		else:
			if (cadena[0] in simbolos) == False:
				temp.append(-2)
				recorres2(nodos,simbolos,indice,cadena[1:0],temp,total)
			else:
				i = 0
				cad_temp = cadena
				for i in range(0,len(nodos[indice].transiciones)):
					if nodos[indice].transiciones[i][0] == cadena[0]:
						temp.append(indice)
						recorres2(nodos,simbolos,nodos[indice].transiciones[i][1],cad_temp[1:],temp,total)


def recorrer(nodos,simbolos,indice,cadena):
	estados = []
	if nodos[indice].numero == -1:
		error = [-1]
		return error
	else:
		if len(cadena) == 0:
			estados.append(indice)
			if nodos[indice].final == True:
				return estados
			else:
				return estados+[-1]
		else:
			i = 0
			if (cadena[0] in simbolos) == False:
				return estados+[-2]+recorrer(nodos,simbolos,indice,cadena[1:])
			estados.append(indice)
			return estados+recorrer(nodos,simbolos,nodos[indice].siguiente(cadena[0]),cadena[1:])

def mostrar(recorrido,cadena):
	if recorrido[len(recorrido) - 1] != -1:
		print("\033[1;32m"+"Cadena valida"+"\033[0;m"+"\nRecorrido:")
		camino = ""
		for j in range(0,len(recorrido)):
			if recorrido[j] == -2:
				camino += ("\033[1;34m ("+cadena[j]+")\033[0;m -> ")
			else:
				if (j + 1) <= len(cadena):
					camino += (str(recorrido[j])+"("+(cadena[j])+") -> ")
		camino += str(recorrido[j])
		print(camino)
	else:
		print("\033[1;31m"+"Cadena no valida"+"\033[0;m")