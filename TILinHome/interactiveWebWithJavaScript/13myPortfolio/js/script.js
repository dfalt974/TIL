function scrollHandler() {
    $(window).scrollTop() >= $(".about").position().top ? ($(".menu-right button").css("color", "#4a4a4a"), $(".skill").each(function () {
        var t = $(this),
            o = t.find(".percentage").text();
        t.find(".inner-bar").animate({
            width: o
        }, 1200)
    })) : $(".menu-right button").css("color", "white"), $("section").each(function () {
        $(window).scrollTop() >= $(this).position().top && $(this).find(".vertical-center").animate({
            top: "0",
            opacity: "1"
        }, 800)
    })
}
$(window).on("scroll", scrollHandler), scrollHandler(), $(".menu-right button").on("click", function () {
    var t = $(this).attr("id");
    "about-btn" == t ? $("html, body").animate({
        scrollTop: $(".about").position().top
    }, 1e3) : "contact-btn" == t && $("html, body").animate({
        scrollTop: $(".contact").position().top
    }, 1e3)
});