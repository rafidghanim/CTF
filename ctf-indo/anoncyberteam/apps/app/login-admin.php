<?php
include 'koneksi.php';

session_start();

if (isset($_COOKIE['id']) && isset($_COOKIE['key'])) {
    $id = $_COOKIE['id'];
    $key = $_COOKIE['key'];

   
    $result = mysqli_query($conn, "SELECT iduser FROM user_admin WHERE id_admin = $id");
    $row = mysqli_fetch_assoc($result);

   
    if ($key === hash('sha256', $row['iduser'])) {
        $_SESSION['loginadmin'] = true;
    }
}

if (isset($_SESSION["loginadmin"])) {
    header("Location: admin/index.php");
}


if (isset($_POST["submit"])) {

   
    $iduser = $_POST["iduser"];
    $password = $_POST["password"];

   
    $result = mysqli_query($conn, "SELECT * FROM user_admin WHERE iduser = '$iduser'");

   
    if (mysqli_num_rows($result) === 1) {

       
        $row = mysqli_fetch_assoc($result);
        $sesiiduser = $row['iduser'];
        $sesinm_admin = $row['nm_admin'];

       
        if (password_verify($password, $row["password"])) {

           
            $_SESSION["loginadmin"] = true;
            $_SESSION["iduser"] = $sesiiduser;
            $_SESSION["nm_admin"] = $sesinm_admin;

           
            if (isset($_POST['remember'])) {
               
                setcookie('id', $row['id_admin'], time() + 60);
                setcookie('key', hash('sha256', $row['iduser']), time() + 60);
            }

           
            header("Location: admin/index.php");
            exid;
        }
    }

   
    $error = true;
}
?>
<!DOCTYPE html>
<html lang="en" class="h-100">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Login Admin</title>
    <!-- Favicon icon -->
    <link rel="icon" type="image/png" sizes="16x16" href="images/logo.ico">
    <link href="css/style.css" rel="stylesheet">

</head>

<body class="h-100" style="background:url(images/bg4.jpg) repeat center center">
    <div class="authincation h-100">
        <div class="container h-100">
            <div class="row justify-content-center h-100 align-items-center">
                <div class="col-md-6">
                    <div class="authincation-content">
                        <div class="row no-gutters">
                            <div class="col-xl-12">
                                <div class="auth-form">
                                    <p class="text-center"><a href="https
                                    <h4 class="text-center mb-4">Sistem Admin</h4>
                                    <h4 class="text-center mb-4 text-primary">Login Admin</h4>
                                    <form action="" method="post">
                                        <div class="form-group">
                                            <label class="mb-1" for="iduser"><strong>iduser :</strong></label>
                                            <input type="iduser" class="form-control" name="iduser" id="iduser" placeholder="iduser" required>
                                        </div>
                                        <div class="form-group">
                                            <label class="mb-1" for="password"><strong>Password</strong></label>
                                            <input type="password" class="form-control" name="password" id="password" placeholder="Password" required>
                                        </div>
                                        <div class="form-row d-flex justify-content-between mt-4 mb-2">
                                            <div class="form-group">
                                                <div class="custom-control custom-checkbox ml-1">
                                                    <input type="checkbox" class="custom-control-input" id="remember" name="remember">
                                                    <label class="custom-control-label" for="remember">Remember Me</label>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="text-center">
                                            <button type="submit" class="btn btn-primary btn-block" name="submit">Masuk</button>
                                        </div>
                                    </form>
                                    <?php if (isset($error)) { ?>
                                        <br>
                                        <div class="alert alert-danger alert-dismissible fade show">
                                            <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" class="mr-2">
                                                <polygon points="7.86 2 16.14 2 22 7.86 22 16.14 16.14 22 7.86 22 2 16.14 2 7.86 7.86 2"></polygon>
                                                <line x1="15" y1="9" x2="9" y2="15"></line>
                                                <line x1="9" y1="9" x2="15" y2="15"></line>
                                            </svg>
                                            <strong>Error!</strong> Username/Password salah...!
                                            <button type="button" class="close h-100" data-dismiss="alert" aria-label="Close"><span><i class="mdi mdi-close"></i></span>
                                            </button>
                                        </div>
                                    <?php } ?>
                                    <div class="new-account mt-3 text-center">
                                    <p>Copyright &copy; <a href="https</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>


    <!--**********************************
        Scripts
    ***********************************-->
    <!-- Required vendors -->
    <script src="vendor/global/global.min.js"></script>
    <script src="vendor/bootstrap-select/dist/js/bootstrap-select.min.js"></script>
    <script src="js/custom.min.js"></script>
    <script src="js/deznav-init.js"></script>

</body>

</html>