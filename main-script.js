$(function () {
	$('.mainTable td').children('button').click(function () {
		$('.background-blackout').css('display', 'flex');
	});
	$("#close-lab-view").click(function () {
		$('.background-blackout').css('display', 'none');
	});
	$("#go-to-add-lab").click(function () {
		$('.lab-view').css('display', 'none');
		$('.lab-upload').css('display', 'flex');
	});
	$("#cancel-upload").click(function () {
		$('.lab-upload').css('display', 'none');
		$('.lab-view').css('display', 'flex');
	});
});