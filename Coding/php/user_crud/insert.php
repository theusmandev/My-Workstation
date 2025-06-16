<?php include 'db.php'; ?>
<!DOCTYPE html>
<html>
<head><title>Insert User</title></head>
<body>
    <h2>Register User</h2>
    <form method="post">
        Name: <input type="text" name="name" required><br><br>
        Email: <input type="email" name="email" required><br><br>
        <input type="submit" name="save" value="Submit">
    </form>

    <?php
    if (isset($_POST['save'])) {
        $name = $_POST['name'];
        $email = $_POST['email'];

        $sql = "INSERT INTO users (name, email) VALUES (:name, :email)";
        $stmt = $pdo->prepare($sql);
        $stmt->execute(['name' => $name, 'email' => $email]);
        echo "User added successfully!";
    }
    ?>
</body>
</html>
