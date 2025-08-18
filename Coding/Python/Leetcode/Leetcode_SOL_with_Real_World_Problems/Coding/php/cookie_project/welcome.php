<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $name = htmlspecialchars(trim($_POST["username"]));
    setcookie("username", $name, time() + 5); // 1 hour
    header("Location: welcome.php");
    exit;
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
    <?php
    if (isset($_COOKIE["username"])) {
        echo "<h2>Welcome back, " . $_COOKIE["username"] . "!</h2>";
        echo "<p><a href='logout.php'>Logout</a></p>";
    } else {
        echo "<h2>No name found. <a href='index.php'>Enter Again</a></h2>";
    }
    ?>
</body>
</html>
