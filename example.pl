$constant_1=25;
$constant_2=33;
@array=(1,2,3,5);
%dicionario = (1 => "hola", "hola" => 5);
$a = 5;
while($a > 0) {
    print $a," ";
    $a--;
}

for ($i=0,$j=2; $i <= 9; $i++) {
   print "$i,$j\n";
}


@b=(0,1,2);

foreach $i (@b) {
  print "$i\n";
}

print "\n";
print ($constant_1," ",$constant_2," ",$array[2]," ",$dicionario{"hola"},"\n");
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
$a=4;
$b=3;
if ($a > 3){
	if($b < 2){
		print "holi\n";
	}elsif($b==1){
		print "jajajaja\n";
	}
	if($b>2){
		print "el mehoyo del asunto\n";
	}
}else{
	print "funciona por favor\n";
}