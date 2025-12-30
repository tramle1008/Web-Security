<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

session_start();
include('db.php');

$message = "";

if ($_SERVER["REQUEST_METHOD"] == "GET") {
    $username = $_GET['username'];
    $password = md5($_GET['password']); // mã hóa md5

    $sql = "SELECT * FROM SV WHERE username='$username' AND password='$password'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // Đăng nhập thành công
        $_SESSION['username'] = $username;
        $message = "<p style='color:green;'>Đăng nhập thành công!</p>";
    } else {
        // Sai tài khoản hoặc mật khẩu
        $message = "<p style='color:red;'>Sai tên đăng nhập hoặc mật khẩu!</p>";
    }
}
?>

<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Trang đăng nhập</title>
</head>
<body>
    <h2>Đăng nhập</h2>
    <form method="GET" action="">
        <label>Tên đăng nhập:</label>
        <input type="text" name="username" required><br><br>
        <label>Mật khẩu:</label>
        <input type="password" name="password" required><br><br>
        <input type="submit" value="Đăng nhập">
    </form>
    <?php echo $message; ?>
</body>
</html>
