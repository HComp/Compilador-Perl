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