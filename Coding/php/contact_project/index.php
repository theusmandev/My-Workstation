<!DOCTYPE html>
<html>
<head>
    <title>Contact Form</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h2>Contact Us</h2>

    <?php
    $name = $email = $phone = $message = "";
    $errors = [];

    if ($_SERVER["REQUEST_METHOD"] === "POST") {
        // Sanitize inputs
        $name = htmlspecialchars(trim($_POST["name"]));
        $email = filter_input(INPUT_POST, "email", FILTER_SANITIZE_EMAIL);
        $phone = filter_input(INPUT_POST, "phone", FILTER_SANITIZE_NUMBER_INT);
        $message = htmlspecialchars($_POST["message"]);

        // Validate inputs
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $errors[] = "Invalid email format";
        }

        if (!preg_match("/^[A-Za-z ]+$/", $name)) {
            $errors[] = "Only letters and spaces allowed in name";
        }

        if (!preg_match("/^03\d{2}-\d{7}$/", $phone)) {
            $errors[] = "Phone must be like 0301-1234567";
        }

        // Output
        if (empty($errors)) {
            echo "<div class='success'>";
            echo "<h3>Thank You!</h3>";
            echo "<p><strong>Name:</strong> $name</p>";
            echo "<p><strong>Email:</strong> $email</p>";
            echo "<p><strong>Phone:</strong> $phone</p>";
            echo "<p><strong>Message:</strong><br>" . nl2br($message) . "</p>";
            echo "</div>";
        } else {
            echo "<div class='error'>";
            foreach ($errors as $error) {
                echo "<p>❌ $error</p>";
            }
            echo "</div>";
        }
    }
    ?>

    <form method="POST" action="">
        <input type="text" name="name" placeholder="Full Name" required>
        <input type="email" name="email" placeholder="Email Address" required>
        <input type="text" name="phone" placeholder="Phone (e.g. 0301-1234567)" required>
        <textarea name="message" placeholder="Your Message" rows="5" required></textarea>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
