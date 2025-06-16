<!DOCTYPE html>
<html>
<head><title>Regex Form</title></head>
<body>
    <h2>User Input Validator & Analyzer</h2>
    <form action="process.php" method="post">
        Name: <input type="text" name="name" required><br><br>
        Email: <input type="text" name="email" required><br><br>
        Phone (e.g., 0300-1234567): <input type="text" name="phone" required><br><br>
        Message: <textarea name="message" rows="5" cols="30" required></textarea><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
