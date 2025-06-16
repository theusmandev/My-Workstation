<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SweetAlert Example</title>
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
</head>
<body>
    <button onclick="showAlert()">Click Me</button>

    <script>
        function showAlert() {
            Swal.fire({
                title: 'Hello!',
                text: 'This is a non-blocking custom alert.',
                icon: 'success',
                confirmButtonText: 'OK'
            });
        }
    </script>
</body>
</html>
