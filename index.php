<?php 


$test =[0, 1, 2, 3];

for ($i=0; $i<4 ; $i++){
    $total = $total + $test[$i];
}


$total = 0;
foreach ($test as $key => $value) {
    $total = $value + $total;
}
print($total);

?>