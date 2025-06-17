<!DOCTYPE html>
<html>
<head>
    <title>Contact - My PHP Website</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Contact Us</h1>
    <form method="post" action="">
        <label>Name:</label><br>
        <input type="text" name="name" required><br><br>

        <label>Message:</label><br>
        <textarea name="message" required></textarea><br><br>

        <input type="submit" value="Send">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        echo "<h3>Thanks, " . htmlspecialchars($_POST['name']) . "! We received your message.</h3>";
    }
    ?>

    <nav>
        <a href="index.php">Home</a> |
        <a href="about.php">About</a> |
        <a href="contact.php">Contact</a>
    </nav>
</body>
</html>
