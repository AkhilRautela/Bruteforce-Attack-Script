<?php
$username=$_GET['user'];
$password=$_GET['pass'];
if((strcmp($username,"Akhil")==0) && (strcmp($password,"1234")==0)){
    header("Location: boss");
    echo "boss"; 
}
else{
    echo $username . $password;
}
?>