import ply.yacc as yacc
from AnalizadorLexico import tokens
import AnalizadorLexico
import sys

VERBOSE = 1

def p_program(p):
	'program : declaration_list'
	pass

def p_declaration_list_2(p):
	'''declaration_list : declaration declaration_list
							| declaration'''
	pass

def p_declaration(p):
	'''declaration : header_declaration
						| var_declaration
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
						| PESOS ID EQUAL E SEMICOLON
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
							| PORCENTAJE ID EQUAL LPAREN lista2 RPAREN SEMICOLON
							| PORCENTAJE ID EQUAL PORCENTAJE ID SEMICOLON'''
	pass

def p_lista2(p):
	'''lista2 : typevar COMMA typevar COMMA lista2
				| typevar COMMA LPAREN lista RPAREN COMMA lista2
				| typevar COMMA LBRACKET lista RBRACKET COMMA lista2
				| typevar COMMA typevar
				| typevar COMMA LPAREN lista RPAREN
				| typevar COMMA LBRACKET lista RBRACKET''' 
	pass

def p_lista1(p):
	'''lista1 : typevar EQUALGREATER typevar COMMA lista1
				| typevar EQUALGREATER LPAREN lista RPAREN COMMA lista1
				| typevar EQUALGREATER LBRACKET lista RBRACKET COMMA lista1
				| typevar EQUALGREATER typevar
				| typevar EQUALGREATER LPAREN lista RPAREN
				| typevar EQUALGREATER LBRACKET lista RBRACKET''' 
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
	'''ciclos : FOR LPAREN sent_for SEMICOLON cond SEMICOLON PESOS ID incdec  RPAREN LBLOCK sentencias_ciclos RBLOCK
					| FOREACH PESOS ID LPAREN ARROBA ID RPAREN LBLOCK sentencias_ciclos RBLOCK
					| WHILE LPAREN cond RPAREN LBLOCK sentencias_ciclos RBLOCK''' 
	pass

def p_sentencias_ciclos(p):
	''' sentencias_ciclos : var_declaration sentencias_ciclos
								| ciclos sentencias_ciclos
								| var_declaration
								| ciclos'''
	pass

def p_sent_for(p):
	'''sent_for : PESOS ID
						| PESOS ID EQUAL ENTERO''' 
	pass

def p_cond(p):
	'''cond : typevar LESS typevar
				| typevar GREATER typevar
				| typevar ISEQUAL typevar
				| typevar LESSEQUAL typevar
				| typevar GREATEREQUAL typevar
				| typevar DEQUAL typevar
				| typevar AND typevar'''
	pass

def p_incdec(p):
	'''incdec : PLUSPLUS
					| MINUSMINUS'''
	pass

def p_error(p):
	if VERBOSE:
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
		fin = 'Entrada.pl'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("Tu parser reconocio correctamente todo")
	#input()
