#!/usr/bin/perl

use strict;
use warnings;

# Testの数
my $num = <STDIN>;

for (my $i = 1; $i <= $num; ++$i) {
    my $line = <STDIN>;
    chomp($line);
    my $answer = 0;

    my ($smax, $str) = split / /, $line;
    my @audience = split //, $str;

    my $stands = 0;
    for (my $shyness = 0; $shyness <= $smax; ++$shyness) {
        if ($shyness <= $stands) {
            $stands += $audience[$shyness];
        } else {
            $answer += $shyness - $stands;
            $stands += $shyness - $stands + $audience[$shyness];
        }
    }

    print "Case #$i: $answer\n";
}

#sub somemethod {
#}
