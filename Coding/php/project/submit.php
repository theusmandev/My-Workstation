<?php
$cacheFile = "cache/feedback.html";
$cacheTime = 60; // seconds (1 minute)

// 🔹 Check if cache is valid and show it
if (file_exists($cacheFile)) {
    $age = time() - filemtime($cacheFile);
    if ($age < $cacheTime) {
        echo "<div style='background: #f0f0f0; padding: 10px; border: 1px solid #ccc;'>
                ⚡ This page is cached.<br>
                🕒 Cache will refresh in: <strong>" . ($cacheTime - $age) . " seconds</strong>
              </div><br>";
        readfile($cacheFile);
        exit;
    }
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // 🔹 Sanitize inputs
    $name = filter_input(INPUT_POST, "name", FILTER_SANITIZE_FULL_SPECIAL_CHARS);
    $email = filter_input(INPUT_POST, "email", FILTER_VALIDATE_EMAIL);
    $message = htmlspecialchars($_POST["message"]);

    // 🔹 Validate inputs
    if (!$name || !$email || !$message) {
        die("❌ Invalid input. Please go back and try again.");
    }

    // 🔹 Serialize and save to file
    $data = [
        "name" => $name,
        "email" => $email,
        "message" => $message,
        "time" => date("Y-m-d H:i:s")
    ];
    file_put_contents("data.txt", serialize($data) . PHP_EOL, FILE_APPEND);

    // 🔹 Set cookie
    setcookie("last_user", $name, time() + 3600);

    // 🔹 Auto-create cache folder
    if (!is_dir("cache")) {
        mkdir("cache", 0777, true);
    }

    // 🔹 Start capturing output to cache
    ob_start();
    echo "<h3>✅ Feedback Submitted</h3>";
    echo "<b>Name:</b> $name<br>";
    echo "<b>Email:</b> $email<br>";
    echo "<b>Message:</b> $message<br>";
    echo "<b>Time:</b> {$data['time']}<br><br>";
    echo "<a href='index.php'>Submit Another</a>";

    // 🔹 Save to cache and show output
    $html = ob_get_contents();
    file_put_contents($cacheFile, $html);
    ob_end_flush();
} else {
    echo "Invalid request method.";
}
?>
