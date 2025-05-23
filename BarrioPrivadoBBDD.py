import sqlite3

def menu(op,titulo):
	print(titulo)
	i=0
	while True:
		while True:
			print(op[i])
			i+=1
			if i==len(op):
				break

		opc=int(input("Ingrese su opcion: "))
		while opc<0 or opc>len(op):
			opc=int(input("Ingrese su opcion: "))
		break
		
	return opc

BP=sqlite3.connect("Barrio_Privado.db")

cursor=BP.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS LOTES (LOTE INTEGER,MANZANA INTEGER,MFT INTEGER,MFO INTEGER,LP VARCHAR(2),AL VARCHAR(2),AGUA VARCHAR(2),ESQ VARCHAR(2),ESTADO VARCHAR(2))")
cursor.execute("CREATE TABLE IF NOT EXISTS PROPIETARIOS (LOTEP INTEGER,MANZANAP INTEGER,NOMAPE VARCHAR(40),DDC INTEGER,MDC INTEGER,ADC INTEGER,SC INTEGER,HABITANTES INTEGER,VEHICULOS INTEGER,CL INTEGER,CA INTEGER,CG INTEGER,DV INTEGER,MV INTEGER,AV INTEGER)")
while True:
	a=menu(["1-Lotes","2-Propietarios","3-Liquidacion","4-Salir"],"Menu Principal")

	if a==1:
		while True:
			a=menu(["1-Alta","2-Consulta","3-Modificar","0-Volver"],"Menu Lotes")
			if a==0:
				break
			#Alta
			if a==1:
				while True:
					nl=int(input("Ingrese el numero de lote: "))
					nm=int(input("Ingrese el numero de manzana: "))

					cursor.execute("SELECT * FROM LOTES WHERE LOTE=? and MANZANA=?",(nl,nm))

					val=cursor.fetchall()

					if len(val)!=0:
						print("El lote ya existe")
					else:
						break

				mft=int(input("Ingrese los metros de frente: "))
				mfo=int(input("Ingrese los metros de fondo: "))
				lp=input("Ingrese si tiene luz publica(S/N): ")
				al=input("Ingrese si tiene asfalto(S/N): ")
				agua=input("Ingrese si tiene agua publica(S/N): ")
				esq=input("Ingrese si tiene esquina(S/N): ")
				estado="N"


				datos=[(nl),(nm),(mft),(mfo),(lp),(al),(agua),(esq),(estado)]

				cursor.execute("INSERT INTO LOTES VALUES(?,?,?,?,?,?,?,?,?)",datos)

				BP.commit()
			#Consulta
			if a==2:
				while True:
					a=menu(["1-Por manzana","2-Por manzana y lote","0-Volver"],"Consulta Lotes")

					if a==0:
						break
					if a==1:
						nm=int(input("Ingrese el numero de manzana: "))
						cursor.execute("SELECT * FROM LOTES WHERE MANZANA=?",(nm,))
						consulta=cursor.fetchall()
						if len(consulta)==0:
							print("La manzana nro:",nm,"no existe")
						else:	
							print("-"*50)
							print("Listado de lotes por manzana")
							print("-"*50)
							for i in consulta:
								print("Lote:",i[0],"Manzana:",i[1],"Metros de Frente:",i[2],"Metros de Fondo:",i[3],"Luz Publica:",i[4],"Asfalto:",i[5],"Agua Publica:",i[6],"Esquina:",i[7],"Estado:",i[8])
								print("-"*50)

					if a==2:
						nm=int(input("Ingrese el numero de manzana: "))
						nl=int(input("Ingrese el numero de lote: "))
						cursor.execute("SELECT * FROM LOTES WHERE LOTE=? and MANZANA=?",(nl,nm))
						consulta=cursor.fetchall()
						if len(consulta)==0:
							print("El lote nro:",nl,"de la manzana nro:",nm,"no existe")
						else:	
							print("-"*50)
							print("Datos lote Nro:",nl,"Manzana Nro:",nm)
							print("-"*50)
							for i in consulta:
								print("Metros de Frente:",i[2],"Metros de Fondo:",i[3],"Luz Publica:",i[4],"Asfalto:",i[5],"Agua Publica:",i[6],"Esquina:",i[7],"Estado:",i[8])
								print("-"*50)
			#Modificacion
			if a==3:
				nl=int(input("Ingrese el numero de lote: "))
				nm=int(input("Ingrese el numero de manzana: "))
				cursor.execute("SELECT * FROM LOTES WHERE MANZANA=? AND LOTE=?",(nm,nl))
				man=cursor.fetchall()
				print("==================\n1-Metros de frente: ",man[0][2],"\n2-Metros de fondo: ",man[0][3],"\n3-Tiene luz publica?: ",man[0][4],"\n4-Tiene Asfalto?: ",man[0][5],"\n5-Tiene agua publica?: ",man[0][6],"\n6-Tiene Esquina?: ",man[0][7],"\n====================")
				z=int(input("Ingrese la opcion a modificar: "))
				while z<1 or z>6:
					print("Debe ingresar una opcion valida")
				if z<3:
					modi=int(input("Ingrese la modificacion: "))
				else:
					modi=input("Ingrese la modificacion: ")
				if z==1:
					cursor.execute("UPDATE LOTES SET MFT=? WHERE MANZANA=? AND LOTE=?",(modi,nm,nl))
					BP.commit()
				if z==2:
					cursor.execute("UPDATE LOTES SET MFO=? WHERE MANZANA=? AND LOTE=?",(modi,nm,nl))
					BP.commit()
				if z==3:
					cursor.execute("UPDATE LOTES SET LP=? WHERE MANZANA=? AND LOTE=?",(modi,nm,nl))
					BP.commit()
				if z==4:
					cursor.execute("UPDATE LOTES SET AGUA=? WHERE MANZANA=? AND LOTE=?",(modi,nm,nl))
					BP.commit()
				if z==5:
					cursor.execute("UPDATE LOTES SET AL=? WHERE MANZANA=? AND LOTE=?",(modi,nm,nl))
					BP.commit()
				if z==6:
					cursor.execute("UPDATE LOTES SET ESQ=? WHERE MANZANA=? AND LOTE=?",(modi,nm,nl))
					BP.commit()
#Propietarios
	if a==2:			
		while True:
			a=menu(["1-Alta","2-Baja","3-Consulta","4-Modificar","0-Volver"],"Menu Propietarios")
			if a==0:
				break
			#Alta
			if a==1:
				cursor.execute("SELECT * FROM LOTES")
				val=cursor.fetchall()
				if len(val)==0:
					print("Debe ingresar un lote para cargar un propietario")
					break

				nl=int(input("Ingrese el numero de lote: "))
				nm=int(input("Ingrese el numero de manzana: "))
				cursor.execute("SELECT ESTADO FROM LOTES WHERE MANZANA=? AND LOTE=?",(nm,nl))
				val=cursor.fetchall()
				if val[0][0]=="S":
					print("El lote ya esta ocupado")
				else:
					nomape=input("Ingrese el nombre y apellido del propietario: ")
					ddc=int(input("Ingrese el dia de compra: "))
					mdc=int(input("Ingrese el mes de compra: "))
					adc=int(input("Ingrese el año de compra: "))
					sc=int(input("Ingrese la superficie cubierta: "))
					hc=int(input("Ingrese los habitantes en casa: "))
					cv=int(input("Ingrese la cantidad de vehiculos: "))
					cl=int(input("Ingrese el consumo de luz: "))
					ca=int(input("Ingrese el consumo de agua: "))
					cg=int(input("Ingrese el consumo de gas: "))
					dv="-"
					mv="-"
					av="-"
					datos=[(nl),(nm),(nomape),(ddc),(mdc),(adc),(sc),(hc),(cv),(cl),(ca),(cg),(dv),(mv),(av)]
					cursor.execute("INSERT INTO PROPIETARIOS VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",datos)
					cursor.execute("UPDATE LOTES SET ESTADO='S' WHERE MANZANA=? AND LOTE=?",(nm,nl))
					BP.commit()
			#Baja Propietarios
			if a==2:
				nomape=input("Ingrese el nombre y apellido del propietario: ")
				nm=int(input("Ingrese el numero de manzana: "))
				nl=int(input("Ingrese el numero de lote: "))
				dv=int(input("Ingrese el dia de venta: "))
				mv=int(input("Ingrese el mes de venta: "))
				av=int(input("Ingrese el año de venta: "))
				cursor.execute("UPDATE LOTES SET ESTADO='N' WHERE MANZANA=? AND LOTE=?",(nm,nl))
				cursor.execute("UPDATE PROPIETARIOS SET DV=? WHERE NOMAPE=?",(dv,nomape))
				cursor.execute("UPDATE PROPIETARIOS SET MV=? WHERE NOMAPE=?",(mv,nomape))
				cursor.execute("UPDATE PROPIETARIOS SET AV=? WHERE NOMAPE=?",(av,nomape))
				cursor.execute("UPDATE PROPIETARIOS SET DDC='-' WHERE NOMAPE=?",(nomape,))
				cursor.execute("UPDATE PROPIETARIOS SET MDC='-' WHERE NOMAPE=?",(nomape,))
				cursor.execute("UPDATE PROPIETARIOS SET ADC='-' WHERE NOMAPE=?",(nomape,))
				BP.commit()

			#Consulta Propietarios
			if a==3:
				while True:
					a=menu(["1-Por nombre y apellido","2-Por manzana","3-Por manzana y lote","0-Volver"],"Consulta Propietarios")
					if a==0:
						break
					if a==1:
						na=input("Ingrese el nombre y apellido: ")
						cursor.execute("SELECT * FROM PROPIETARIOS WHERE NOMAPE=?",(na,))
						consulta=cursor.fetchall()
						if len(consulta)==0:
							print("El propietario",na,"no existe")
						else:
							print("-"*50)
							print("Datos del propietario:",na)
							print("-"*50)
							for i in consulta:
								print("Lote:",consulta[0][0],"Manzana:",consulta[0][1],"Dia de compra:",consulta[0][3],"Mes de compra:",consulta[0][4],"Año de compra:",consulta[0][5],"Superficie Cubierta:",consulta[0][6],"Habitantes en casa:",consulta[0][7],"Cantidad de Vehiculos:",consulta[0][8],"Consumo de luz:",consulta[0][9],"Consumo de agua:",consulta[0][10],"Consumo de gas:",consulta[0][11],"Dia de venta:",consulta[0][12],"Mes de venta:",consulta[0][13],"Año de venta:",consulta[0][14])
								print("-"*50)
					if a==2:
						nm=int(input("Ingrese el numero de manzana: "))
						cursor.execute("SELECT * FROM PROPIETARIOS WHERE MANZANAP=?",(nm,))
						consulta=cursor.fetchall()
						if len(consulta)==0:
							print("La manzana nro:",nm,"no existe")
						else:	
							print("-"*50)
							print("Listado de propietarios por manzana")
							print("-"*50)
							for i in consulta:
								print("Lote:",consulta[0][0],"Manzana:",consulta[0][1],"Propietario:",consulta[0][2],"Dia de compra:",consulta[0][3],"Mes de compra:",consulta[0][4],"Año de compra:",consulta[0][5],"Superficie Cubierta:",consulta[0][6],"Habitantes en casa:",consulta[0][7],"Cantidad de Vehiculos:",consulta[0][8],"Consumo de luz:",consulta[0][9],"Consumo de agua:",consulta[0][10],"Consumo de gas:",consulta[0][11],"Dia de venta:",consulta[0][12],"Mes de venta:",consulta[0][13],"Año de venta:",consulta[0][14])
								print("-"*50)
					if a==3:
						nm=int(input("Ingrese el numero de manzana: "))
						nl=int(input("Ingrese el numero de lote: "))
						cursor.execute("SELECT * FROM PROPIETARIOS WHERE LOTEP=? and MANZANAP=?",(nl,nm))
						consulta=cursor.fetchall()
						if len(consulta)==0:
							print("El lote nro:",nl,"de la manzana nro:",nm,"no existe")
						else:	
							print("-"*50)
							print("Datos del propietario del lote Nro:",nl,"Manzana Nro:",nm)
							print("-"*50)
							for i in consulta:
								print("Lote:",consulta[0][0],"Manzana:",consulta[0][1],"Propietario:",consulta[0][2],"Dia de compra:",consulta[0][3],"Mes de compra:",consulta[0][4],"Año de compra:",consulta[0][5],"Superficie Cubierta:",consulta[0][6],"Habitantes en casa:",consulta[0][7],"Cantidad de Vehiculos:",consulta[0][8],"Consumo de luz:",consulta[0][9],"Consumo de agua:",consulta[0][10],"Consumo de gas:",consulta[0][11],"Dia de venta:",consulta[0][12],"Mes de venta:",consulta[0][13],"Año de venta:",consulta[0][14])
								print("-"*50)
			#Modificacion Propietarios
			if a==4:
				nomape=input("Ingrese el Propietario: ")
				cursor.execute("SELECT * FROM PROPIETARIOS WHERE NOMAPE=?",(nomape,))
				man=cursor.fetchall()
				print("==================\nLote: ",man[0][0],"\nManzana: ",man[0][1],"\nNombre y apellido: ",man[0][2],"\n1-Dia de compra: ",man[0][3],"\n2-Mes de compra: ",man[0][4],"\n3-Año de compra: ",man[0][5],"\n4-Superficie cubierta: ",man[0][6],"\n5-Cantidad de habitantes: ",man[0][7],"\n6-Cantidad de vehiculos: ",man[0][8],"\n7-Consumo de luz: ",man[0][9],"\n8-Consumo de agua: ",man[0][10],"\n9-Consumo de gas: ",man[0][11],"\n10-Dia de venta",man[0][12],"\n11-Mes de venta",man[0][13],"\n12-Año de venta",man[0][14],"\n====================")
				x=int(input("Ingrese la opcion a modificar: "))
				m=int(input("Ingrese la modificacion: "))
				if x==1:
					cursor.execute("UPDATE PROPIETARIOS SET DDC=? WHERE NOMAPE=?",(m,nomape))
					BP.commit()
				if x==2:
					cursor.execute("UPDATE PROPIETARIOS SET MDC=? WHERE NOMAPE=?",(m,nomape))
					BP.commit()
				if x==3:
					cursor.execute("UPDATE PROPIETARIOS SET ADC=? WHERE NOMAPE=?",(m,nomape))
					BP.commit()
				if x==4:
					cursor.execute("UPDATE PROPIETARIOS SET SC=? WHERE NOMAPE=?",(m,nomape))
					BP.commit()
				if x==5:
					cursor.execute("UPDATE PROPIETARIOS SET HABITANTES=? WHERE NOMAPE=?",(m,nomape))
					BP.commit()
				if x==6:
					cursor.execute("UPDATE PROPIETARIOS SET VEHICULOS=? WHERE NOMAPE=?",(m,nomape))
					BP.commit()
				if x==7:
					cursor.execute("UPDATE PROPIETARIOS SET CL=? WHERE NOMAPE=?",(m,nomape))
					BP.commit()
				if x==8:
					cursor.execute("UPDATE PROPIETARIOS SET CA=? WHERE NOMAPE=?",(m,nomape))
					BP.commit()
				if x==9:
					cursor.execute("UPDATE PROPIETARIOS SET CG=? WHERE NOMAPE=?",(m,nomape))
					BP.commit()
				if x==10:
					cursor.execute("UPDATE PROPIETARIOS SET DV=? WHERE NOMAPE=?",(m,nomape))
					BP.commit()
				if x==11:
					cursor.execute("UPDATE PROPIETARIOS SET MV=? WHERE NOMAPE=?",(m,nomape))
					BP.commit()
				if x==12:
					cursor.execute("UPDATE PROPIETARIOS SET AV=? WHERE NOMAPE=?",(m,nomape))
					BP.commit()
					
	if a==3:
		while True:
			a=menu(["1-Calcular","2-Mostrar","0-Volver"],"Menu Liquidacion")
			

	if a==4:
		BP.close()
		break