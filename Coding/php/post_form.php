<!DOCTYPE html>
<html>
<head>
    <title>POST Form</title>
</head>
<body>
    <form action="post_form.php" method="post">
        Name: <input type="text" name="name">
        <input type="submit" value="Submit via POST">
    </form>

    <?php
    if (isset($_POST['name'])) {
        $name = $_POST['name'];
        echo "Hello, " . htmlspecialchars($name);
    }
    ?>
</body>
</html>
