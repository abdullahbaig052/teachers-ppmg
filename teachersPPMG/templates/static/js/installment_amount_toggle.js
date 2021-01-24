$(".zmdi-plus").click(function () {
    $(this).parent().parent().parent().parent().find(".less_details").attr("hidden", true);
    $(this).parent().parent().parent().parent().find(".more_details").attr("hidden", false);
});
$(".zmdi-minus").click(function () {
    $(this).parent().parent().parent().parent().find(".more_details").attr("hidden", true);
    $(this).parent().parent().parent().parent().find(".less_details").attr("hidden", false);
});
