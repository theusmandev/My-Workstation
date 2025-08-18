<?php

function validateName($name) {
    return preg_match("/^[A-Za-z ]+$/", $name);
}

function validateEmail($email) {
    return preg_match("/^[\w.-]+@[\w.-]+\.\w{2,}$/", $email);
}

function validatePhone($phone) {
    return preg_match("/^03\d{2}-\d{7}$/", $phone);
}

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $name    = $_POST["name"];
    $email   = $_POST["email"];
    $phone   = $_POST["phone"];
    $message = $_POST["message"];

    echo "<h3>Validation Results:</h3>";

    echo "Name: " . ($validName = validateName($name) ? "✅ Valid" : "❌ Invalid") . "<br>";
    echo "Email: " . ($validEmail = validateEmail($email) ? "✅ Valid" : "❌ Invalid") . "<br>";
    echo "Phone: " . ($validPhone = validatePhone($phone) ? "✅ Valid" : "❌ Invalid") . "<br><br>";

    echo "<h3>Message Processing:</h3>";

    // 🔹 1. Replace bad words
    $badWords = ['stupid', 'idiot'];
    $cleanedMessage = preg_replace("/\b(" . implode("|", $badWords) . ")\b/i", "****", $message);
    echo "Cleaned Message: <br><i>$cleanedMessage</i><br><br>";

    // 🔹 2. Count all numbers
    preg_match_all("/\d+/", $message, $matches);
    echo "Numbers found: " . implode(", ", $matches[0]) . "<br>";
    echo "Total Numbers: " . count($matches[0]) . "<br><br>";

    // 🔹 3. Split message into words
    $words = preg_split("/[\s,!.?]+/", $message);
    echo "Words in Message:<br>";
    foreach ($words as $word) {
        if (!empty($word)) echo $word . "<br>";
    }

    echo "<br><a href='index.php'>Go Back</a>";
}
?>
