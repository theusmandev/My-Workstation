<!DOCTYPE html>
<html>
<head>
  <title>Feedback Form</title>
  <script>
    window.onload = function () {
      document.getElementById("name").value = localStorage.getItem("name") || "";
      document.getElementById("email").value = localStorage.getItem("email") || "";
    }

    function saveToLocal() {
      localStorage.setItem("name", document.getElementById("name").value);
      localStorage.setItem("email", document.getElementById("email").value);
    }
  </script>
</head>
<body>
  <h2>Feedback Form</h2>
  <form action="submit.php" method="POST" onsubmit="saveToLocal()">
    <label>Name:</label>
    <input type="text" name="name" id="name" required><br><br>

    <label>Email:</label>
    <input type="email" name="email" id="email" required><br><br>

    <label>Message:</label><br>
    <textarea name="message" required></textarea><br><br>

    <input type="submit" value="Submit Feedback">
  </form>
</body>
</html>
