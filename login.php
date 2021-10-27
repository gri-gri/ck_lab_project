<?php
	$badLogin = '';
	if ($_POST['login']) {
		if ($_POST['login']=='admin' and $_POST['password']=='admin') {
			session_start();
			$_SESSION['security_check'] = true;
			$_SESSION['name'] = 'Тестовое Имя';
			header('Location: index.php');
		}
		else {
			$badLogin = '<p id="redAlert">Не правильный логин или пароль</p>';
		}
	}
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Авторизация</title>
		<style type="text/css">
			body {
				height: 100vh;
				margin:0;
				display: flex;
				align-items: center;
				justify-content: space-around;
			}
			p {
				margin: 7px 0;
			}
			form input {
				display: block;
				margin:0 auto;
			}
			form p {
				text-align: center;
			}
			form button {
				display: block;
				margin:7px auto 0 auto;
			}
			h1 {
				text-align: center;
			}
			#redAlert {
				color: red;
				margin-bottom: 0;
			}
		</style>
	</head>
	<body>
		<form method="POST" action="login.php">
			<h1>Авторизация</h1>
			<p>Логин</p>
			<input type="text" name="login">
			<p>Пароль</p>
			<input type="password" name="password">
			<?php echo $badLogin; ?>
			<button>Жми меня!</button>
		</form>
	</body>
</html>