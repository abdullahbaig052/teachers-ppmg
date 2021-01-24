function set_doc_type(){
    if ($("#id_doc_type").val() === "passport") {
        $("#passport").attr("hidden", false);
        $("#drivers_license").attr("hidden", true);
        $("#other_id").attr("hidden", true);
        $("#common").attr("hidden", false);
        $(".passport").attr("required", true);
        $(".license").attr("required", false);
        $(".other_id").attr("required", false);
    } else if ($("#id_doc_type").val() === "drivers_license") {
        $("#passport").attr("hidden", true);
        $("#drivers_license").attr("hidden", false);
        $("#other_id").attr("hidden", true);
        $("#common").attr("hidden", false);
        $(".passport").attr("required", false);
        $(".license").attr("required", true);
        $(".other_id").attr("required", false);
    } else if ($("#id_doc_type").val() === "other_id") {
        $("#passport").attr("hidden", true);
        $("#drivers_license").attr("hidden", true);
        $("#other_id").attr("hidden", false);
        $("#common").attr("hidden", false);
        $(".passport").attr("required", false);
        $(".license").attr("required", false);
        $(".other_id").attr("required", true);
    } else {
        $("#passport").attr("hidden", true);
        $("#drivers_license").attr("hidden", true);
        $("#other_id").attr("hidden", true);
        $("#common").attr("hidden", true);
        $(".passport").attr("required", true);
        $(".license").attr("required", true);
        $(".other_id").attr("required", true);
    }

}

function submit_button_validation(){
    if ($("#id_doc_type").val() == "passport" && $(':file[required=required]').filter(function () {
        return $.trim(this.value) != '';
    }).length == 3) {
        $("#id_submit_button").attr("disabled", false);
    } else if ($("#id_doc_type").val() != "passport" && $(':file[required=required]').filter(function () {
        return $.trim(this.value) != '';
    }).length==4) {
        $("#id_submit_button").attr("disabled", false);
    } else {
        $("#id_submit_button").attr("disabled", true);
    }
}

$(document).ready(function () {
    set_doc_type();
    submit_button_validation();
});

$(".custom-file-input").on("change", function () {
    const fileName = $(this).val().split("\\").pop();
    if (fileName !== "") {
        $(this).siblings(".custom-file-label").addClass("selected").html(fileName.slice(0, 46));
    } else {
        $(this).siblings(".custom-file-label").removeClass("selected").html($(this).attr("name"));
    }
    submit_button_validation();
});

$("#id_doc_type").on("change", function () {
    set_doc_type();
    submit_button_validation();
});