<?php
include 'db.php';
$id = $_GET['id'];

$sql = "DELETE FROM users WHERE id = :id";
$stmt = $pdo->prepare($sql);
$stmt->execute(['id' => $id]);

header("Location: list.php");
?>
