<?php
	session_start();
	if (!$_SESSION['security_check']) {
		header('Location: login.php');
	}
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Сайт для сдачи лаб</title>
		<link rel="stylesheet" type="text/css" href="style.css">
		<script src="jquery-3.5.1.min.js"></script>
		<script src="main-script.js"></script>
	</head>
	<body>
		<header>
			<select>
				<option>Группа1</option>
				<option>Группа2</option>
			</select>
			<h1>Cайт для сдачи лаб ИТМО&#161; (I.D.E.A)</h1>
			<a id="outButton" href="out.php">Выйти</a>
		</header>
		<main>		
			<h2>Добро пожаловать, <?php echo $_SESSION['name']; ?></h2>
			<table class="mainTable">
				<thead>
					<tr>
						<th>Название</th>
						<th>Дедлайн</th>
						<th>Файл</th>
						<th>Статус</th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td><button>Лаба по цк</button></td>
						<td>32.11.2041</td>
						<td><a href="main-script.js" download>Laptubidu.txt</a></td>
						<td>Не отправлено</td>
					</tr>
					<tr>
						<td><button>Лаба по дискреточке</button></td>
						<td>32.11.2041</td>
						<td><a href="main-script.js" download>Blabla.pdf</a></td>
						<td class="complete-green">Отправлено</td>
					</tr>
					<tr>
						<td><button>Лаба по матану</button></td>
						<td>40.32.2020</td>
						<td><a href="main-script.js" download>Blabla.pdf</a></td>
						<td>Не отправлено</td>
					</tr>
				</tbody>
			</table>
			<div class="background-blackout">
				<div class="lab-view">
					<div class="space-between">
						<h4>Название:</h4>
						<p>Лаба по цк</p>
					</div>
					<div class="space-between">
						<h4>Дедлайн:</h4>
						<P>32.11.1202</P>
					</div>
					<div class="space-between">
						<h4>Файлы:</h4>
						<a href="main-script.js" download>Bla.html</a>
					</div>
					<h4>Примечание:</h4>
					<p>Текст-рыба на русском языке. Рыбатекст используется дизайнерами, проектировщиками и фронтендерами, когда нужно быстро заполнить макеты или прототипы содержимым. Это тестовый контент, который не должен нести никакого смысла, лишь показать наличие самого текста или продемонстрировать типографику в </p>
					<div class="right-float">
						<button id="go-to-add-lab">Перейти к сдаче</button>
						<button id="close-lab-view">Закрыть</button>
					</div>
				</div>
				<div class="lab-upload">
					<div class="space-between">
						<h4>Лаба по цк</h4>
						<h4>32.11.1202</h4>
					</div>
					<form method="POST" action="/">
						<div class="space-between">
							<h4>Прикрепить файл</h4>
							<input type="file" name="file[]">
						</div>
						<h4>Добавить примечание</h4>
						<textarea></textarea>
						<div class="right-float">
							<button type="button" id="cancel-upload">Отмена</button>
							<button>Отправить</button>
						</div>
					</form>
				</div>
			</div>
		</main>
	</body>
</html>