<!DOCTYPE html>
<html>
<head>
    <title>GET Form</title>
</head>
<body>
    <form action="get_form.php" method="get">
        Name: <input type="text" name="name">
        <input type="submit" value="Submit via GET">
    </form>

    <?php
    if (isset($_GET['name'])) {
        $name = $_GET['name'];
        echo "Hello, " . htmlspecialchars($name);
    }
    ?>
</body>
</html>
