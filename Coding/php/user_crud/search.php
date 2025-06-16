<?php
include 'db.php';
?>

<!DOCTYPE html>
<html>
<head><title>Search Users</title></head>
<body>
    <h2>Search User</h2>
    <form method="post">
        <input type="text" name="search" placeholder="Search by name or email" required>
        <input type="submit" value="Search">
    </form>
    
    <?php
    if (isset($_POST['search'])) {
        $search = "%" . $_POST['search'] . "%";
        
        $sql = "SELECT * FROM users WHERE name LIKE :search OR email LIKE :search";
        $stmt = $pdo->prepare($sql);
        $stmt->execute(['search' => $search]);

        echo "<h3>Search Results</h3>";
        echo "<table border='1'>
                <tr><th>ID</th><th>Name</th><th>Email</th><th>Actions</th></tr>";

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
        echo "</table>";
    }
    ?>
</body>
</html>
