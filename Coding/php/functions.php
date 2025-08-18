<?php
function say_hello(){
    echo "Hello , Usman!";
}


say_hello();
?>

<?php
function greet($name) {
    echo "Hello, " . $name . "!";
}

greet("Usman");
greet("Ali");
?>


<?php
function add($a, $b) {
    return $a + $b;
}

$result = add(10, 5);
echo "Sum is: " . $result;
?>






<?php
function addOne(&$num) {
    $num++;
}

$x = 5;
addOne($x);
echo $x;  // Output: 6
?>

