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
	</head>
	<body>
		<header>
			<select>
				<option>Группа1</option>
				<option>Группа2</option>
			</select>
			<h1>Cайт для сдачи лаб ИТМО</h1>
			<button>Выйти</button>
		</header>
		<h2>Добро пожаловать, <?php echo $_SESSION['name']; ?></h2>
		<img src="https://yandex-images.clstorage.net/a5A31RD79/6ec70afEW/TmCWvrhk5rudT1dl48QdKqr31ndzJEumC61QWKhOMT6lEK7GpvaldoO_lwjOI-zp4LEZ3pykpXxr82zG1YmNfx9p34uICJ-HtUtXadfgcQ622_ZLUzQbugLMDDX8dnRCpDT3qodXGK4Obi-4H8olBBzRFLaEqYkNZ6rFZuBIBC7OWN7WgExPSwVrppmPBBn-ZsImE1O9U0t7LYERPOa9NhzwimcDJ4A2Nrp_gNO62aSoufDu1IWwOYsiWaOgxHSS9gAORnC4Zwcd835ZH0h5egL2vu9rsU-rM1l5-TCq_ZpY7AJ3Uwt0CuJ2czizOunkzOnYgtRxLJWnsvmrrEiUAgak3gqQxC_XgYfy1Ssgub4GQrrLK6nbP1OpKRnIhqG2qIj2c_s_0ELiqnuAW_rp5GidzFY8ldSp6xalEzRkROYWBCLOZIQfL00XJkXXnBmilkbOK3tFt4tjvXWhHBLdInhQJptTA-CGLrJftL8yJbQUnTwWdJ248U8qtYfcYNjOhlwKerScn4dlu77Z06gNmip2LscD_TcXrzX5NdgW7faokHrrZ-sAvp7iX8QbdmW0gB1MIowB8Pm3cqUT2IgcmvrclqaUvH9nHVfyaYvgIe7inipLV8mzo9OB0enMzuUO8JxiH9N7LOJqxh84s_It6CixzKoYceS5z1IRk0xEgL7uUFLCFCivn41Xnr3PYO0S7k6-l8_h48_TYSFlpCJtmgwY-v_fZ9geKuoLqHf2nXTo8UCyNOFEvWNmEY_w1AQu1qC-wthg_4-RB7L9w1TpjpJO-o-_FRMvH71ZCRwejYqMHPYT76cocqJ-CwB3No2UdF3AAth98CG3JlHfQIAEmnosevqAODNLhe_eaVPEHWKuxkZ7O-l_6zvp7eHMijkGBGDuBwcPTGJCggsYH_bdgED90OqYAVC5ZxplNzTsiBbiXLryYJh_o4XjznWDHBECYnImD6vtMyO7BY2poAqw">
	</body>
</html>