<?php
setcookie("username", "", time() - 3600); // Delete cookie
header("Location: index.php");
exit;
