<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>AJAX Feedback Form</title>
  <style>
    body { font-family: Arial; margin: 30px; }
    input, textarea { padding: 10px; width: 100%; margin: 10px 0; }
    #response { margin-top: 20px; background: #f0f0f0; padding: 15px; border-left: 5px solid #5cb85c; }
  </style>
</head>
<body>

<h2>Feedback Form (AJAX)</h2>

<form id="feedbackForm">
  <input type="text" name="name" placeholder="Enter your name" required>
  <input type="email" name="email" placeholder="Enter your email" required>
  <textarea name="message" placeholder="Enter your message" required></textarea>
  <button type="submit">Submit</button>
</form>

<div id="response"></div>

<script>
  document.getElementById("feedbackForm").addEventListener("submit", function(e) {
    e.preventDefault(); // Prevent full page reload

    const formData = new FormData(this);

    fetch("submit.php", {
      method: "POST",
      body: formData
    })
    .then(response => response.text())
    .then(data => {
      document.getElementById("response").innerHTML = data;
    })
    .catch(error => {
      document.getElementById("response").innerHTML = "❌ Error submitting form.";
      console.error("Error:", error);
    });
  });
</script>

</body>
</html>
