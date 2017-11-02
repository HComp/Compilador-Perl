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