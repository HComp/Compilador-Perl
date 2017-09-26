$Hola = 1231234;
$$rHola = $Hola;
$prueba = " cancion";
$pos = $prueba++;
$pre = ++$prueba;
print "hola"
select
0x1234
0X12442
$rescalar="hola&.-_+*$%@!/\#?()|={}[]><,:"; #referencia a la cadena anónima "hola"
$rarray=[1,2,3];   #referencia al array anónimo (1,2,3)
$rlista={"llave1" => "dato1","llave2" => "dato2"};
$array3d->[0]->[0]->[0]=1;
# Forma abreviada: 
$array3d[0][0][0]=1; 
# También se puede usar 
$array3d->[0][0][0]=1;
$x = 4.1;            # un real
$y = "11";           # una cadena de caracteres
$z = $x + $y;        # adición de dos valores numéricos
$t = $x . $y;        # concatenación de dos cadenas 
print $z, "\n", "$t \n";
$msg = <<SALUDO; 
hola, 
buenos dias, 
adios, 
SALUDO
$x = 0377;           # equivale a 255
$y = 0xff;           # equivale a 255
$str = '¡Hola $wld!';
$wld = "mundo"; 
$str = "¡Hola $wld!";
if ($ristra =~ /str/) { 
   print $ristra; 
} 
else { 
   print "No se encuentra el patron"; 
} 
if ($ristra !~ /str/) { 
   print "No se encuentra el patron"; 
} 
else { 
   print $ristra; 
}
# verifica si 'str' se esta en $ristra
if (($alfa>4) && ($beta<3)) { 
   print $alfa * $beta; 
   # Solo entra si se cumplen ambas expresiones.
}
if (($pal1 eq "N") || ($pal1 eq "n") { 
   print "La operacion no se efectua"; 
   &salida(); 
   # Entra si se cumple alguna de las dos expresiones
}
if (!($num < 5)) { 
   print "$num es mayor que 5"; 
   # Entra si la expresion no se cumple 
}
i = (x<y? 6:k+1);
# Lee argumentos de la línea de comando y los lista.

$NumArg = $#ARGV; # Almacena el numero de argumentos
$Cuenta = 0;
while ($Cuenta < $NumArg) {
  print "Argumento0 ",$Cuenta,"-->",$ARGV[$Cuenta], "\n";
  $Cuenta++; 
}
sub nombre_de_funcion { 
   instrucciones; 
   [return Variable o expresion;] 
}
sub diferencia { 
   if ($x < $y) { 
     print "$x es inferior a $y\n"; 
     $y-$x; 
   } 
   else { 
     print "$x es superior o igual a $y\n"; 
     $x-$y; 
   } 
} 
$x = 2; $y = 3; 
$abs = &diferencia; # $abs = 1
@P=split//,".URRUU\c8R";@d=split//,"\nrekcah xinU / lreP rehtona tsuJ";sub p{
@p{"r$p","u$p"}=(P,P);pipe"r$p","u$p";++$p;($q*=2)+=$f=!fork;map{$P=$P[$f^ord
($p{$_})&6];$p{$_}=/ ^$P/ix?$P:close$_}keys%p}p;p;p;p;p;map{$p{$_}=~/^[P.]/&&
close$_}%p;wait until$?;map{/^r/&&<$_>}%p;$_=$d[$q];sleep rand(2)if/\S/;print
use strict;
use warnings;
use IO::Handle;

my ( $remaining, $total );

$remaining = $total = shift(@ARGV);

STDOUT->autoflush(1);

while ( $remaining ) {
    printf ( "Remaining %s/%s \r", $remaining--, $total );
    sleep 1;
}

print "\n";
#
# This uses the Unix /etc/passwd file to map from a 
# userid to a numerical uid.  It accpets a list of
# userids on the command line, and maps each one.
#

use strict;

# The location of the password file.
my $pwd = "/etc/passwd";

#
# This function maps the indicated userid,
# and prints out the result.  The file
# itself is already opened with the global
# handle PWD
#
sub getuid {
    my ($userid) = @_;

    # Rewind the file, and read until 
    # the userid is found. 
    my($line);
    seek PWD, 0, 0;
    while($line = <PWD>) {
        # Split the line to get the fields we're interested in.
        my($puserid, $ppwd, $puid) = split(/:/, $line);

        # If we found it, print and return. 
        if($puserid eq $userid) {
            print "UID for $userid is $puid.\n";
            return;
        }
    }

    # If we got here, it didn't work.
    print "No such user $userid.\n";
}

# Open the passwd file and scan through
# the argument list.
open (PWD, $pwd) or die "Cannot open $pwd: $!.\n";

while(my $userid = shift @ARGV) {
    getuid($userid);
}

close PWD;