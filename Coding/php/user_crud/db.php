<?php
$host = "localhost";
$user = "root";
$pass = "";
$dbname = "user_db";

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    // echo "Connected";
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}
?>
