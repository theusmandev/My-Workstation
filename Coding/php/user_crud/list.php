<?php include 'db.php'; ?>
<!DOCTYPE html>
<html>
<head><title>User List</title></head>
<body>
    <h2>All Users</h2>
    <a href="insert.php">Add New</a><br><br>
    <table border="1" cellpadding="5">
        <tr><th>ID</th><th>Name</th><th>Email</th><th>Actions</th></tr>
        <?php
        $stmt = $pdo->query("SELECT * FROM users");
        while ($row = $stmt->fetch()) {
            echo "<tr>
                <td>{$row['id']}</td>
                <td>{$row['name']}</td>
                <td>{$row['email']}</td>
                <td>
                    <a href='update.php?id={$row['id']}'>Edit</a> | 
                    <a href='delete.php?id={$row['id']}'>Delete</a>
                </td>
            </tr>";
        }
        ?>
    </table>
</body>
</html>
