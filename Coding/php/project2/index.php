<?php
session_start();

// Initialize session variables
if (!isset($_SESSION['users'])) {
    $_SESSION['users'] = [];
    $_SESSION['count'] = 0;
}

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['age'])) {
    $age = (int)$_POST['age'];
    $eligible = $age >= 18 ? 'Eligible to Vote' : 'Not Eligible to Vote';
    $_SESSION['users'][] = ['age' => $age, 'eligible' => $eligible];
    $_SESSION['count']++;
}

if (isset($_POST['reset'])) {
    session_unset();
    session_destroy();
    session_start();
    $_SESSION['users'] = [];
    $_SESSION['count'] = 0;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Voting Eligibility Checker</title>
    <style>
        body {
            background-color: #1a1a1a;
            color: #ffffff;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
        }

        h1, h2 {
            color: #ffffff;
        }

        form {
            margin: 20px auto;
            padding: 20px;
            background-color: #333;
            border-radius: 10px;
            width: 300px;
            display: inline-block;
        }

        input[type="number"] {
            padding: 10px;
            margin-right: 10px;
            border: none;
            border-radius: 5px;
        }

        button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: #45a049;
        }

        table {
            width: 50%;
            margin: 20px auto;
            border-collapse: collapse;
            background-color: #333;
        }

        th, td {
            padding: 10px;
            border: 1px solid #555;
        }

        tr:nth-child(even) {
            background-color: #444;
        }

        @media (max-width: 600px) {
            form {
                width: 90%;
            }
            table {
                width: 90%;
            }
            input[type="number"] {
                width: 60%;
            }
        }
    </style>
</head>
<body>
    <h1>Voting Eligibility Checker</h1>
    <form method="POST" action="">
        <input type="number" name="age" placeholder="Enter Age" required min="0">
        <button type="submit">Submit</button>
    </form>
    <p><?php echo 20 - $_SESSION['count']; ?> entries remaining.</p>

    <?php
    if ($_SESSION['count'] == 20) {
        $eligibleVoters = array_filter($_SESSION['users'], fn($user) => $user['eligible'] === 'Eligible to Vote');
        $notEligibleVoters = array_filter($_SESSION['users'], fn($user) => $user['eligible'] === 'Not Eligible to Vote');
    ?>
        <h2>Eligible Voters</h2>
        <table>
            <tr><th>#</th><th>Age</th></tr>
            <?php $i = 1; foreach ($eligibleVoters as $voter) { ?>
                <tr><td><?php echo $i++; ?></td><td><?php echo $voter['age']; ?></td></tr>
            <?php } ?>
        </table>

        <h2>Not Eligible Voters</h2>
        <table>
            <tr><th>#</th><th>Age</th></tr>
            <?php $i = 1; foreach ($notEligibleVoters as $voter) { ?>
                <tr><td><?php echo $i++; ?></td><td><?php echo $voter['age']; ?></td></tr>
            <?php } ?>
        </table>
        <form method="POST" action="">
            <button type="submit" name="reset">Reset All</button>
        </form>
    <?php } ?>
</body>
</html>