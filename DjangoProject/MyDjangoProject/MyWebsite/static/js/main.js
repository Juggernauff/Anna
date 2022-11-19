$(document).ready(function () {
	
	//top navigation smooth scroll settings
	$('.navigation').onePageNav({
		currentClass: 'active',
		scrollThreshold: 0.2, // Adjust if Navigation highlights too early or too late
		filter: ':not(.external)',
		changeHash: true
	});
	
});
