import ply.lex as lex
import sys

tokens = [
	# Symbols
    'PLUS',
    'PLUSPLUS',
    #'PLUSEQUAL',
    'MINUS',
    'MINUSMINUS',
    #'MINUSEQUAL',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSLESS',
    'LESSEQUAL',
    'GREATER',
    'GREATERGREATER',
    'GREATEREQUAL',
    'GUIONDOWN',
    'ARROW',
    'EQUALGREATER',
    'LESSEQUALGREATER',
    'EQUALPRIME',
    'EXCLAMATIONPRIME',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'ISEQUAL',
    'SEMICOLON',
    'COMMA',
    'PLUSGREATER',
   	'PLUSLESS',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'COMMENT',
    'DOT',
    # logic bitwise operators
    'ANDBW',
    'ORBW',
    'XOR',
    'COMPLEMENT',
    # logic operators
    'ORS',
    'ANDS',
    'NOTS',
    'OR',
    'AND',
    'NOT',
    # Others  
    'INTERROGATION', 
    'ID',
    'DOLLARDOLLAR',
    'ENTERO',
    'HEXADECIMAL',
    'OCTAL',
    'CADENA',
    'CADENAA',
    'REFERENCIAS',
    'REFERENCIALISTA',
    'INCREMENTO',
    'DECREMENTO',
    'PREINDEX',
    'POSTINDEX',

    #bucles and conditional
    'FOR',
	'FOREACH',
	'MY',
	'WHILE',
	'LAST', 				#LAST sirve para romper bucles
	'NEXT',					#NEXT sirve para continuaren un bucle 
	'IF',
	'ELSE',
	'ELSIF',
	'GOTO',

	#encontrado en la pagina https://www.programacionfacil.com/perl_script/palabras_reservadas.html
	'ABS', 					#devuelve el valor absoluto de la expresion pasada.
	'CHMOD', 				#cambia los permisos de los ficheros dados.
	'CHOP',				#recorta y retorna el ultimo caracter de una cadena.
	'CHOWN', 				# cambia el propietario de los ficheros dados.
	'CLOSE', 				#cierra un fichero. cos: devuelve el coseno del angulo dado en radianes.
	'DEFINED', 			#sirve para comprobar si existe una variable, formato, subrutina,etc..
	'DELETE', 			#borra un valor de un array asociativo a traves de su clave.
	'DIE', 					#imprime en la salida del error estandar un mensaje pasado como parametro cuando ocurre un error en la ejecucion de una sentencia.
	'EOF', 					#retorna verdadero si el final del fichero dado.
	'EVAL', 				#evalua la expresion pasada como si se tratase de un pequeno programa perl.
	'EXEC', 				#ejecuta lo que pasemos como parametro y sale del programa.
	'EXIT', 				#hace que salgamos del perl script devolviendo al sistema operativo el valor pasado como argumento.
	'EXP', 					#retorna el numero e elevado a la potencia pasada como parametro.
	'EACH',
	'FILENO', 			#devuelve el descriptor del manejador del fichero pasado como parametro.
	'FORK', 				#realiza una llamada fork. getc: lee el siguiente caracter del fichero especificado.
	'HEX', 					#devuelve el valor decimal del numero hexadecimal pasado como parametro.
	'INDEX', 				#devuelve la posicion de la primera ocurrencia de una cadena en otra.
	'INT', 					#devuelve la parte entera del parametro pasado.
	'JOIN', 				#une las cadenas pasadas como argumento con un separador tambien pasado como argumento.
	'KEYS', 				#devuelve todas las claves de un array asociativo.
	'LENGTH', 			#devuelve la longitud en caracteres del parametro pasado.
	'LOCAL', 				#declara como locales las variables pasadas como argumentos.
	'LOG', 					#devuelve el logaritmo del numero dado.
	'MKDIR', 				#crea un directorio en el camino dado.
	'OCT', 					#devuelve el valor decimal del numero octal pasado como parametro.
	'OPEN', 				#abre el fichero fichero dado asociandole un manejador de fichero especificado tambien como parametro.
	'POP', 					#retorna y borra el ultimo elemento del array dado.
	'PRINT', 				#muestra en la salida standard o en el fichero especificado la expresion dada.
	'PUSH', 				#anade el valor dado al final del array pasado como parametro.
	'RAND', 				#devuelve un numero aleatorio entre 0 y el valor pasado como argumento.
	'READ', 				#lee un determinado numero de caracteres desde el fichero pasado como argumento.
	'RENAME', 			#sirve para renombrar un fichero.
	'REQUIRE', 			#sirve para incluir codigo externo en nuestro guion.
	'RETURN', 			#devuelve un valor desde una subrutina.
	'REFERENCE',
	'RMDIR', 				#borra un directorio.
	'SEEK', 				#situa un puntero a fichero en un lugar determinado.
	'SELECT', 				#sirve para seleccionar el manejador de fichero que sera utilizado por defecto para la salida de los comandos o funciones que no especifiquen un determinado manejador de fichero como parametro.
	'SHIFT', 				#devuelve el primer valor del array dado borrandolo posteriormente.
	'SIN', 					#devuelve el seno del angulo pasado en radianes.
	'SLEEP', 				#causa que el perl script o guion se detenga el numero de segundos especificados.
	'SORT', 				#ordena el array dado.
	'SPLIT', 				#divide una cadena en subcadenas segun el separador especificado.
	'SQRT', 				#devuelve la raiz cuadrada del numero pasado.
	'SYSTEM', 			#igual que exec pero no se sale del perl script.
	'SUB',
	'TELL', 				#devuelve la posicion actual del puntero a fichero del manejador de fichero especificado.
	'VALUES', 			#devuelve todos los valores del array asociativo dado.
	'WRITE', 				#escribe un registro con formato en el fichero asociado a ese formato.
	'CMP',
	'RINDEX',
	'SUBSTR',
	'PACK',
	'UNSHIFT',
	'UNTIL',
	'UNLESS',
	'USE',
	'REVERSE',

	'PESOS',				#para escribir un escalar o una referencia
	'ARROBA',				#para definir un arreglo
	'PORCENTAJE'			#para definir un asociado
 ]

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_GUIONDOWN = r'_'
t_DIVIDE = r'/'
t_REFERENCE =r'\\'
t_LESS = r'<'
t_GREATER = r'>'
t_EQUAL = r'='
t_DISTINT = r'!'
t_SEMICOLON = r';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK = r'\{'
t_RBLOCK = r'\}'
t_COLON = r':'
t_DOT = r'\.'
t_PESOS = r'\$'
t_ARROBA = r'\@'
t_PORCENTAJE = r'\%'
t_NOT = r'\!'
t_INTERROGATION = r'\?'
t_COMPLEMENT = r'\~'
t_ANDBW = r'\&'
t_ORBW = r'\|'
t_XOR = r'\^'


def t_ORS(t):
	r'or'
	return t

def t_ANDS(t):
	r'and'
	return t
	
def t_NOTS(t):
	r'not'
	return t

def t_COMMENT(t):
	r'\#.*'

def t_FOR(t):
	r'for'
	return t
	
def t_FOREACH(t):
	r'foreach'
	return t

def t_MY(t):
	r'my'
	return t

def t_WHILE(t):
	r'while'
	return t

def t_LAST(t): 				#LAST sirve para romper bucles
	r'last'
	return t

def t_NEXT(t):					#NEXT sirve para continuaren un bucle 
	r'next'
	return t

def t_IF(t):
	r'if'
	return t

def t_ELSE(t):
	r'else'
	return t

def t_ELSIF(t):
	r'elsif'
	return t

def t_ABS(t):
	r'abs'
	return t

def t_CHMOD(t):
	r'hcmod' 				#cambia los permisos de los ficheros dados.
	return t

def t_CHOP(t):				#recorta y retorna el ultimo caracter de una cadena.
	r'chop'
	return t

def t_CHOW(t): 				# cambia el propietario de los ficheros dados.
	r'chow'
	return t

def t_CLOSE(t): 				#cierra un fichero. cos: devuelve el coseno del angulo dado en radianes.
	r'close'
	return t

def t_DEFINED(t): 			#sirve para comprobar si existe una variable, formato, subrutina,etc..
	r'define'
	return t

def t_DELETE(t): 			#borra un valor de un array asociativo a traves de su clave.
	r'delete'
	return t

def t_DIE(t): 					#imprime en la salida del error estandar un mensaje pasado como parametro cuando ocurre un error en la ejecucion de una sentencia.
	r'die'
	return t

def t_EOF(t): 					#retorna verdadero si el final del fichero dado.
	r'eof'
	return t

def t_EVAL(t): 				#evalua la expresion pasada como si se tratase de un pequeno programa perl.
	r'eval'
	return t

def t_EXEC(t): 				#ejecuta lo que pasemos como parametro y sale del programa.
	r'exec'

def t_EXIT(t): 				#hace que salgamos del perl script devolviendo al sistema operativo el valor pasado como argumento.
	r'exit'
	return t

def t_EXP(t): 					#retorna el numero e elevado a la potencia pasada como parametro.
	r'exp'
	return t

def t_EACH(t):
	r'each'
	return t

def t_FILENO(t): 			#devuelve el descriptor del manejador del fichero pasado como parametro.
	r'fileno'
	return t

def t_FORK(t): 				#realiza una llamada fork. getc: lee el siguiente caracter del fichero especificado.
	r'fork'
	return t

def t_GOTO(t):
	r'goto'
	return t

def t_HEX(t): 					#devuelve el valor decimal del numero hexadecimal pasado como parametro.
	r'hex'
	return t

def t_INDEX(t): 				#devuelve la posicion de la primera ocurrencia de una cadena en otra.
	r'index'
	return t

def t_RINDEX(t):
	r'rindex'
	return t

def t_SUBSTR(t):
	r'substr'
	return t

def t_SUB(t):
	r'sub'
	return t

def t_INT(t): 					#devuelve la parte entera del parametro pasado.
	r'int'
	return t

def t_JOIN(t): 				#une las cadenas pasadas como argumento con un separador tambien pasado como argumento.
	r'join'
	return t

def t_KEYS(t): 				#devuelve todas las claves de un array asociativo.
	r'keys'
	return t

def t_LENGTH(t): 			#devuelve la longitud en caracteres del parametro pasado.
	r'length'
	return t

def t_LOCAL(t): 				#declara como locales las variables pasadas como argumentos.
	r'local'
	return t

def t_LOG(t): 					#devuelve el logaritmo del numero dado.
	r'log'
	return t

def t_MKDIR(t): 				#crea un directorio en el camino dado.
	r'mkdir'
	return t

def t_OCT(t): 					#devuelve el valor decimal del numero octal pasado como parametro.
	r'oct'
	return t

def t_OPEN(t): 				#abre el fichero fichero dado asociandole un manejador de fichero especificado tambien como parametro.
	r'open'
	return t

def t_POP(t): 					#retorna y borra el ultimo elemento del array dado.
	r'pop'
	return t

def t_PRINT(t): 				#muestra en la salida standard o en el fichero especificado la expresion dada.
	r'print'
	return t

def t_PUSH(t): 				#anade el valor dado al final del array pasado como parametro.
	r'push'
	return t

def t_PACK(t):
	r'pack'
	return t

def t_PREINDEX(t):
	r'\$\['
	return t

def t_POSTINDEX(t):
	r'\$\#'
	return t

def t_PLUSGREATER(t):
	r'\+\>'
	return t

def t_PLUSLESS(t):
	r'\+\<'
	return t

def t_RAND(t): 				#devuelve un numero aleatorio entre 0 y el valor pasado como argumento.
	r'rand'
	return t

def t_READ(t): 				#lee un determinado numero de caracteres desde el fichero pasado como argumento.
	r'read'
	return t

def t_RENAME(t): 			#sirve para renombrar un fichero.
	r'rename'
	return t

def t_REQUIRE(t): 			#sirve para incluir codigo externo en nuestro guion.
	r'require'
	return t

def t_RETURN(t): 			#devuelve un valor desde una subrutina.
	r'return'
	return t

def t_REVERSE(t):
	r'reverse'
	return t

def t_RMDIR(t): 				#borra un directorio.
	r'rmdir'
	return t

def t_SEEK(t): 				#situa un puntero a fichero en un lugar determinado.
	r'seek'
	return t

def t_SELECT(t): 			#sirve para seleccionar el manejador de fichero que sera utilizado por defecto para la salida de los comandos o funciones que no especifiquen un determinado manejador de fichero como parametro.
	r'select'
	return t

def t_SHIFT(t): 				#devuelve el primer valor del array dado borrandolo posteriormente.
	r'shift'
	return t

def t_SIN(t): 					#devuelve el seno del angulo pasado en radianes.
	r'sin'
	return t

def t_SLEEP(t):				#causa que el perl script o guion se detenga el numero de segundos especificados.
	r'slepp'
	return t

def t_SORT(t): 				#ordena el array dado.
	r'sort'
	return t

def t_SPLIT(t): 				#divide una cadena en subcadenas segun el separador especificado.
	r'slipt'
	return t

def t_SQRt(t): 				#devuelve la raiz cuadrada del numero pasado.
	r'sqrt'
	return t

def t_SYSTEM(t): 			#igual que exec pero no se sale del perl script.
	r'system'
	return t

def t_TELL(t): 				#devuelve la posicion actual del puntero a fichero del manejador de fichero especificado.
	r'tell'
	return t

def t_UNSHIFT(t):
	r'unshift'
	return t

def t_UNTIL(t):
	r'until'
	return t

def t_UNLESS(t):
	r'unless'
	return t

def t_USE(t):
	r'use'
	return t

def t_VALUES(t): 			#devuelve todos los valores del array asociativo dado.
	r'values'
	return t

def t_WRITE(t):				#escribe un registro con formato en el fichero asociado a ese formato.
	r'write'
	return t

def t_ID(t):
	r'[a-zA-Z][a-zA-Z_0-9]*'
	return t

def t_DOLLARDOLLAR(t):
	r'\$\$'
	return t

def t_ENTERO(t):
	r'([1-9][0-9]*|0)'
	return t
# Aqui tambien puede ser 0X o 0x
def t_HEXADECIMAL(t):
	r'(0x|0X)[a-fA-F0-9]+'
	return t

# aqui falta poner cadenas pero con apostrofes ''
def t_CADENA(t):
	r'\"[a-zA-Z_0-9\&\.\-\_\+\*\$\%\@\!\xc2\xa1\/\\\#\?\xc2\xbf\(\)\|\=\{\}\[\]\>\<\,\: \t]*\"' 
	return t

def t_CADENAA(t):
	r'\'[a-zA-Z_0-9\&\.\-\_\+\*\$\%\@\!\xc2\xa1\/\\\#\?\xc2\xbf\(\)\|\=\{\}\[\]\>\<\,\: \t]*\'' 
	return t

def t_OCTAL(t):
	r'0\d+'
	return t

def t_ISEQUAL(t):
	r'=='
	return t

def t_LESSLESS(t):
	r'<<'
	return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATERGREATER(t):
	r'>>'
	return t

def t_EQUALGREATER(t):
	r'=>'
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_LESSEQUALGREATER(t):
	r'<=>'
	return t

def t_EQUALPRIME(t):
	r'=~'
	return t

def t_EXCLAMATIONPRIME(t):
	r'!~'
	return t

def t_AND(t):
	r'\&\&'
	return t
def t_OR(t):
	r'\|\|'
	return t

def t_ARROW(t):
	r'->'
	return t

def t_DEQUAL(t):
	r'!='
	return t

def t_MINUSMINUS(t):
	r'--'
	return t

def t_PLUSPLUS(t):
	r'\+\+'
	return t

def t_INCREMENTO(t):
	r'\+\+'
	return t

def t_DECREMENTO(t):
	r'\-\-'
	return t

def t_newline(t):
	r'\n'
	t.lexer.lineno += 1






t_ignore = ' \t'

def t_error(t):
	print("Error de compilacion '%s'" % t.value[0], t.lexer.lineno, t.lexer.lexpos)
	t.lexer.skip(1)

lexer = lex.lex()

if __name__ == "__main__":
	archivo = open("Entrada.pl", "r")
	data = archivo.read()
	lexer.input(data)
	for tok in lexer:
		print(tok)