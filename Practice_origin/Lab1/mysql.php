<?php
$servername = "localhost";
$username = "user1";
$password = "user1234";

// Show ID - Name
echo "Ma so sinh vien - Ho ten";

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
echo "Connected successfully";
?>