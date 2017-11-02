import ply.yacc as yacc
from AnalizadorLexico import tokens
import AnalizadorLexico
import sys

VERBOSE = 1

val=False

def p_program(p):
	'program : declaration_list'
	pass

def p_declaration_list_2(p):
	'''declaration_list : declaration declaration_list
							| declaration'''
	pass

def p_declaration(p):
	'''declaration : header_declaration
						| print
						| var_declaration
						| sentencia_if
						| function_declaration
						| call_function SEMICOLON
						| E SEMICOLON
						| ciclos'''
	pass

# AQUI ESTOY DECLARANDO TODO LO QUE PUEDE IR EN LA CABEZERA TAL COMO USE, REQUIRE

def p_header_declaration_1(p):
	'header_declaration : USE ID SEMICOLON'
	pass

def p_header_declaration_2(p):
	'header_declaration : REQUIRE ID SEMICOLON'
	pass

# AQUI ESTOY DECLARANDO TODO LO QUE TENGA QUE VER CON LAS VARIABLES
def p_var_declaration_1(p):
	'''var_declaration : PESOS ID SEMICOLON
						| MY PESOS ID SEMICOLON
						| PESOS ID EQUAL E SEMICOLON
						| PESOS ID EQUAL call_function SEMICOLON
						| PESOS ID incdec SEMICOLON
						| MY PESOS ID EQUAL typevar SEMICOLON
						| PESOS ID EQUAL typevar SEMICOLON'''
	pass 

# AUI VOY A PONER TODO LO REFERENTE A ARREGLOS

def p_var_declaration_2(p):
	'''var_declaration :  ARROBA ID SEMICOLON
							| ARROBA ID EQUAL LPAREN lista RPAREN SEMICOLON
							| ARROBA ID EQUAL ARROBA ID SEMICOLON'''
	pass

# AQUI VOY A PONER TODO LO REFERENTE A DICCIONARIOS

def p_var_declaration_3(p):
	'''var_declaration :  PORCENTAJE ID SEMICOLON
							| PORCENTAJE ID EQUAL LBLOCK lista1 RBLOCK SEMICOLON
							| PORCENTAJE ID EQUAL LPAREN lista1 RPAREN SEMICOLON
							| PORCENTAJE ID EQUAL LPAREN lista2 RPAREN SEMICOLON
							| PORCENTAJE ID EQUAL PORCENTAJE ID SEMICOLON'''
	pass

def p_lista2(p):
	'''lista2 : typevar COMMA typevar COMMA lista2
				| typevar COMMA LPAREN lista RPAREN COMMA lista2
				| typevar COMMA LBRACKET lista RBRACKET COMMA lista2
				| typevar COMMA typevar
				| typevar COMMA LPAREN lista RPAREN
				| typevar COMMA LBRACKET lista RBRACKET
				| ID COMMA typevar COMMA lista2
				| ID COMMA LPAREN lista RPAREN COMMA lista2
				| ID COMMA LBRACKET lista RBRACKET COMMA lista2
				| ID COMMA typevar
				| ID COMMA LPAREN lista RPAREN
				| ID COMMA LBRACKET lista RBRACKET''' 
	pass

def p_lista1(p):
	'''lista1 : typevar EQUALGREATER typevar COMMA lista1
				| typevar EQUALGREATER LPAREN lista RPAREN COMMA lista1
				| typevar EQUALGREATER LBRACKET lista RBRACKET COMMA lista1
				| typevar EQUALGREATER typevar
				| typevar EQUALGREATER LPAREN lista RPAREN
				| typevar EQUALGREATER LBRACKET lista RBRACKET
				| ID EQUALGREATER typevar COMMA lista1
				| ID EQUALGREATER LPAREN lista RPAREN COMMA lista1
				| ID EQUALGREATER LBRACKET lista RBRACKET COMMA lista1
				| ID EQUALGREATER typevar
				| ID EQUALGREATER LPAREN lista RPAREN
				| ID EQUALGREATER LBRACKET lista RBRACKET''' 
	pass

def p_lista(p):
	'''lista : typevar COMMA lista
				| typevar''' 
	pass

def p_typevar(p):
	'''typevar : CADENA
					| CADENAA
					| ENTERO
					| OCTAL
					| HEXADECIMAL'''
	pass

# AQUI VAMOS A DECLARAR TODAS LAS OPERACION TALES COMO +, -, *, /

def p_E(p):
	'''E : E PLUS T 
			| E MINUS T
			| T '''
	pass

def p_T(p):
	'''T : T TIMES F
			| T DIVIDE F
			| F '''
	pass

def p_F(p):
	'''F : PESOS ID
			| PESOS ID LBRACKET ENTERO RBRACKET
			| ENTERO
			| PESOS ID LBLOCK typevar RBLOCK
			| LPAREN E RPAREN'''
	pass

# AQUI VAMOS A DECLARAR TODOS LOS CICLOS

def p_ciclos(p):
	'''ciclos : FOR LPAREN sent_for SEMICOLON cond SEMICOLON PESOS ID incdec  RPAREN LBLOCK declaration_list RBLOCK
					| FOREACH PESOS ID LPAREN ARROBA ID RPAREN LBLOCK declaration_list RBLOCK
					| WHILE LPAREN cond RPAREN LBLOCK declaration_list RBLOCK''' 
	pass	

def p_sent_for(p):
	'''sent_for : PESOS ID
					| PESOS ID EQUAL ENTERO
					| MY PESOS ID EQUAL ENTERO
					| MY PESOS ID EQUAL ENTERO COMMA sent_for
					| PESOS ID EQUAL ENTERO COMMA sent_for''' 
	pass

# AQUI ESTA LA PARTE DE CONDICIONALES

def p_log(p):
	'''log : LESS
			| GREATER
			| ISEQUAL
			| LESSEQUAL
			| GREATEREQUAL
			| DEQUAL
			| AND
			| ANDS
			| ORS
			| OR'''
	pass

def p_type(p):
	'''type : typevar
				| var_declaration_gen'''
	pass

def p_cond(p):
	'''cond : type
				| cond log cond
				| NOT cond
				| LPAREN type RPAREN
				| LPAREN cond RPAREN'''
	pass

# AQUI ACEPTAMOS INCREMENTO Y DECREMENTO

def p_incdec(p):
	'''incdec : PLUSPLUS
					| MINUSMINUS'''
	pass

# AQUI VAMOS A DECLARAR LA SALIDA EN PANTALLA

def p_print(p):
	'''print : PRINT arg SEMICOLON
				| PRINT LPAREN arg RPAREN SEMICOLON'''
	pass

# VARIABLE SIN SEMICOLON PARA ARGUMENTOS A FUNCIONES Y PRINT

def p_var_declaration_gen(p):
	'''var_declaration_gen : PESOS ID
								| PESOS ID LBRACKET ENTERO RBRACKET
								| PESOS ID LBLOCK 	typevar RBLOCK	
								| PESOS ID LBLOCK	ID RBLOCK'''
	pass

def p_arg(p):
	'''arg : var_declaration_gen
			| type
			| type COMMA arg  
			| CADENA
			| var_declaration_gen COMMA arg
			| CADENA COMMA arg'''
	pass

# AQUI VAMOS A PONER TODO LO REFRENTE A SALTOS

def p_sentencia_if(p):
	''' sentencia_if : IF LPAREN cond RPAREN LBLOCK declaration_list RBLOCK
						| IF LPAREN cond RPAREN LBLOCK declaration_list RBLOCK ELSE LBLOCK declaration_list RBLOCK
						| IF LPAREN cond RPAREN LBLOCK declaration_list RBLOCK ELSIF LPAREN cond RPAREN LBLOCK declaration_list RBLOCK
	'''
	pass

# AQUI VAMOS A PONER TODO LO REFERENTE A FUNCIONES

def p_function_declaration(p):
	'''function_declaration : SUB ID LBLOCK declaration_list RBLOCK'''
	pass

def p_call_function(p):
	'''call_function : ANDBW ID
						| ANDBW ID LPAREN arg RPAREN'''
	pass

def p_error(p):
	global val
	if VERBOSE:
		val=True
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(cminus_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')



parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'example.pl'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	if not val :
		print("Tu parser reconocio correctamente todo")
	#input()
