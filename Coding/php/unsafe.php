<?php
if (isset($_POST['name'])) {
    $name = $_POST['name'];
    echo "Hello, " . $name;
}
?>

<form action="" method="post">
    Name: <input type="text" name="name">
    <input type="submit" value="Submit">
</form>





<!-- 

If a user enters the following script into the form:

html
Copy
Edit
<script>alert('XSS Attack!');</script> -->