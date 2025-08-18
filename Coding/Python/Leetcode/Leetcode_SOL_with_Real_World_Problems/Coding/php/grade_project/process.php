<?php

function calculateGrade($marks) {
    if ($marks < 0 || $marks > 100) {
        throw new Exception("Marks must be between 0 and 100.");
    }

    if ($marks >= 90) return "A+";
    elseif ($marks >= 80) return "A";
    elseif ($marks >= 70) return "B";
    elseif ($marks >= 60) return "C";
    elseif ($marks >= 50) return "D";
    else return "Fail";
}

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $name = trim($_POST["name"]);
    $marks = $_POST["marks"];

    try {
        $grade = calculateGrade($marks);
        echo "<h2>Result</h2>";
        echo "Student: <strong>$name</strong><br>";
        echo "Marks: <strong>$marks</strong><br>";
        echo "Grade: <strong>$grade</strong>";
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage();
    } finally {
        echo "<br><br><a href='index.php'>Go Back</a>";
    }
}
?>
