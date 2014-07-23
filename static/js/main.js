$(document).ready(function(){
	$(window).scroll(function(e){
    	if( $('.header').is_on_screen() > 0 ) {
			var scrolled = $(window).scrollTop();
    		$('.header').css({'background-position-y': -Math.abs((scrolled * 0.6)) + 'px'});
		}
	});

	$('.header-title').animate({
		'opacity': 1
	}, 150, function(){
		$('.header-buttons').animate({
			'opacity': 1,
			'top': '20px'
		}, 200);

		$('.books').mixItUp({
			selectors: {
				target: '.books-one'
			},
			animation: {
				duration: 400,
				effects: 'fade translateZ(-360px) stagger(34ms)',
				easing: 'ease'
			},
			controls: {
				enable: false
			}
		});
	});
	
	$('.header-button__fav').on('click', function(){
		if(!$(this).hasClass('header-button__active')) {
			$('.books').mixItUp('filter', '.books-fav');
			$(this).addClass('header-button__active');
		} else {
			$('.books').mixItUp('filter', 'all');
			$(this).removeClass('header-button__active');
		}
	});

	$('.books-one').on('click', function(){
		window.location.hash = "#/" + $(this).data('id');
		checkLocation();

		return false;
	});

	checkLocation();
	
});

function checkLocation() {
	if(window.location.hash != '') {
		$modalOverlay = $('.md-overlay');
		$modal = $('.md-modal');
		$closeButton = $('.md-close');

		var bookId = window.location.hash;
		bookId = bookId.substr(2, bookId.length);

		$.ajax({
			type: "GET",
			url: "/ajax/" + bookId,
			dataType: "json",
			success: function(result){
				
				if(result.status == 'ok') {
					$modal.find('.md-bookImg').css('backgroundImage', 'url('+result.pic+')');
					$modal.find('.md-bookInfo-date').html(result.date);
					$modal.find('.md-bookInfo-title').html(result.title);
					$modal.find('.md-bookInfo-author').html(result.author);
					$modal.find('.md-bookInfo-text').html(result.text);

					if(result.favorite) {
						$modal.find('.md-bookInfo-title').append(' <span class="md-bookInfo-star"></span>');
					}

					if(! $modal.hasClass('md-show')) {
						$modal.addClass('md-show');
						$('body').addClass('modal-on');
					}
				} else {
					alert("Нет такой записи");

					var scr = document.body.scrollTop; // Sorry for this dirty fix :-(
					window.location.href = '#';
					document.body.scrollTop = scr;
				}
				
			}
		});

		$($modalOverlay).on('click', function(){
			var scr = document.body.scrollTop; // Sorry for this dirty fix :-(
			window.location.href = '#';
			document.body.scrollTop = scr;

			$modal.removeClass('md-show');
			$('body').removeClass('modal-on');
		});

		$closeButton.on('click', function(){
			var scr = document.body.scrollTop; // Sorry for this dirty fix :-(
			window.location.href = '#';
			document.body.scrollTop = scr;

			$modal.removeClass('md-show');
			$('body').removeClass('modal-on');
		});
	}
}

$.fn.is_on_screen = function(){
    var win = $(window);
    var viewport = {
        top : win.scrollTop(),
        left : win.scrollLeft()
    };
    viewport.right = viewport.left + win.width();
    viewport.bottom = viewport.top + win.height();

    var bounds = this.offset();
    bounds.right = bounds.left + this.outerWidth();
    bounds.bottom = bounds.top + this.outerHeight();

    return (!(viewport.right < bounds.left || viewport.left > bounds.right ||    viewport.bottom < bounds.top || viewport.top > bounds.bottom));
 };