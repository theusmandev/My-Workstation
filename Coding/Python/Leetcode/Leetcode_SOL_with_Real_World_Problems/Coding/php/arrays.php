<?php

$fruits = array('apple', 'banana', 'mango');
echo $fruits[0];

echo "<br>"; // Correct HTML line break

$person = array('Name' => 'Usman', 'age' => '25', 'Gender' => 'Male');
echo $person["Name"];
echo "<br>"; 

$students = array(
  array("Ali", 22, "Computer Science"),
  array("Sara", 21, "Math"),
  array("Usman", 23, "Physics")
);

echo $students[0][0]; // Output: Ali





$fruits = array('apple', 'banana', 'mango');
$person = array('Name' => 'Usman', 'age' => '25', 'Gender' => 'Male');

echo "<h3>Using print_r()</h3>";
echo "<pre>";
print_r($fruits);
print_r($person);
echo "</pre>";

echo "<h3>Using foreach loop</h3>";

// Loop through $fruits
echo "<strong>Fruits:</strong><br>";
foreach ($fruits as $fruit) {
    echo $fruit . "<br>";
}

// Loop through $person
echo "<br><strong>Person Info:</strong><br>";
foreach ($person as $key => $value) {
    echo "$key: $value<br>";
}




?>
