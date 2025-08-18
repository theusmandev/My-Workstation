<?php
include 'db.php';
$id = $_GET['id'];

if (isset($_POST['update'])) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $sql = "UPDATE users SET name=:name, email=:email WHERE id=:id";
    $stmt = $pdo->prepare($sql);
    $stmt->execute(['name' => $name, 'email' => $email, 'id' => $id]);
    header("Location: list.php");
}

$stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id");
$stmt->execute(['id' => $id]);
$user = $stmt->fetch();
?>
<h2>Update User</h2>
<form method="post">
    Name: <input type="text" name="name" value="<?= $user['name'] ?>"><br><br>
    Email: <input type="email" name="email" value="<?= $user['email'] ?>"><br><br>
    <input type="submit" name="update" value="Update">
</form>
