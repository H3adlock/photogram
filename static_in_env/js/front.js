/*global $, document, Chart, LINECHART, data, options, window, setTimeout*/
(function () {
    $(window).on('load', function () {
        $('.loader').fadeOut();
        $('.page-loader').delay(1).fadeOut('slow');
    });
    $(document).ready(function () {

        'use strict';

        // ------------------------------------------------------- //
        // For demo purposes only
        // ------------------------------------------------------ //

        var stylesheet = $('link#theme-stylesheet');
        $("<link id='new-stylesheet' rel='stylesheet'>").insertAfter(stylesheet);
        var alternateColour = $('link#new-stylesheet');

        if ($.cookie("theme_csspath")) {
            alternateColour.attr("href", $.cookie("theme_csspath"));
        }

        $("#colour").change(function () {

            if ($(this).val() !== '') {

                var theme_csspath = 'css/style.violet.' + $(this).val() + '.css';

                alternateColour.attr("href", theme_csspath);

                $.cookie("theme_csspath", theme_csspath, { expires: 365, path: document.URL.substr(0, document.URL.lastIndexOf('/')) });

            }

            return false;
        });


        // ------------------------------------------------------- //
        // Equalixe height
        // ------------------------------------------------------ //
        function equalizeHeight(x, y) {
            var textHeight = $(x).height();
            $(y).css('min-height', textHeight);
        }
        equalizeHeight('.featured-posts .text', '.featured-posts .image');

        $(window).resize(function () {
            equalizeHeight('.featured-posts .text', '.featured-posts .image');
        });


        // ---------------------------------------------- //
        // Preventing URL update on navigation link click
        // ---------------------------------------------- //
        $('.link-scroll').bind('click', function (e) {
            var anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $(anchor.attr('href')).offset().top + 2
            }, 700);
            e.preventDefault();
        });


        // ---------------------------------------------- //
        // FancyBox
        // ---------------------------------------------- //
        $("[data-fancybox]").fancybox();


        // ---------------------------------------------- //
        // Divider Section Parallax Background
        // ---------------------------------------------- //
        $(window).on('scroll', function () {

            var scroll = $(this).scrollTop();

            if ($(window).width() > 1250) {
                $('section.divider').css({
                    'background-position': 'left -' + scroll / 8 + 'px'
                });
            } else {
                $('section.divider').css({
                    'background-position': 'center bottom'
                });
            }
        });


        // ---------------------------------------------- //
        // Search Bar
        // ---------------------------------------------- //
        $('.search-btn').on('click', function (e) {
            e.preventDefault();
            $('.search-area').fadeIn();
        });
        $('.search-area .close-btn').on('click', function () {
            $('.search-area').fadeOut();
        });



        // ---------------------------------------------- //
        // Navbar Toggle Button
        // ---------------------------------------------- //
        $('.navbar-toggler').on('click', function () {
            $('.navbar-toggler').toggleClass('active');
        });

        function navbarAnimation(navbar, homeSection, navHeight) {
            var topScroll = $(window).scrollTop();
            if (navbar.length > 0 && homeSection.length > 0) {
                if (topScroll >= navHeight) {
                    navbar.removeClass('navbar-transparent');
                } else {
                    navbar.addClass('navbar-transparent');
                }
            }
        }

        /* ---------------------------------------------- /*
         * Navbar submenu
         /* ---------------------------------------------- */

        function navbarSubmenu(width) {
            if (width > 767) {
                $('.navbar .navbar-nav > li.dropdown').hover(function () {
                    var MenuLeftOffset = $('.dropdown-menu', $(this)).offset().left;
                    var Menu1LevelWidth = $('.dropdown-menu', $(this)).width();
                    if (width - MenuLeftOffset < Menu1LevelWidth * 2) {
                        $(this).children('.dropdown-menu').addClass('leftauto');
                    } else {
                        $(this).children('.dropdown-menu').removeClass('leftauto');
                    }
                    if ($('.dropdown', $(this)).length > 0) {
                        var Menu2LevelWidth = $('.dropdown-menu', $(this)).width();
                        if (width - MenuLeftOffset - Menu1LevelWidth < Menu2LevelWidth) {
                            $(this).children('.dropdown-menu').addClass('left-side');
                        } else {
                            $(this).children('.dropdown-menu').removeClass('left-side');
                        }
                    }
                });
            }
        }

        /* ---------------------------------------------- /*
         * Navbar hover dropdown on desctop
         /* ---------------------------------------------- */

        function hoverDropdown(width, mobileTest) {
            if ((width > 767) && (mobileTest !== true)) {
                $('.navbar .navbar-nav > li.dropdown, .navbar li.dropdown > ul > li.dropdown').removeClass('open');
                var delay = 0;
                var setTimeoutConst;
                $('.navbar .navbar-nav > li.dropdown, .navbar li.dropdown > ul > li.dropdown').hover(function () {
                    var $this = $(this);
                    setTimeoutConst = setTimeout(function () {
                        $this.addClass('open');
                        $this.find('.dropdown-toggle').addClass('disabled');
                    }, delay);
                },
                    function () {
                        clearTimeout(setTimeoutConst);
                        $(this).removeClass('open');
                        $(this).find('.dropdown-toggle').removeClass('disabled');
                    });
            } else {
                $('.navbar .navbar-nav > li.dropdown, .navbar li.dropdown > ul > li.dropdown').unbind('mouseenter mouseleave');
                $('.navbar [data-toggle=dropdown]').not('.binded').addClass('binded').on('click', function (event) {
                    event.preventDefault();
                    event.stopPropagation();
                    $(this).parent().siblings().removeClass('open');
                    $(this).parent().siblings().find('[data-toggle=dropdown]').parent().removeClass('open');
                    $(this).parent().toggleClass('open');
                });
            }
        }

        /* ---------------------------------------------- /*
         * Navbar collapse on click
         /* ---------------------------------------------- */

        $(document).on('click', '.navbar-collapse.in', function (e) {
            if ($(e.target).is('a') && $(e.target).attr('class') != 'dropdown-toggle') {
                $(this).collapse('hide');
            }
        });

    });

})(jQuery);
