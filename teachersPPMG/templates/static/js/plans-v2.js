$(document).ready(function () {
    $(".months").hide();
    $("."+$('#id_terms_choices').val()+"_month").show();
    $(".apr_with_insurance").hide();
    $('#id_is_insured').prop('checked', true);
    document.getElementById("monthly_installment_"+$('#id_terms_choices').val()+"_month").innerHTML = '$' +parseFloat(parseFloat(document.getElementById("monthly_installment_"+$('#id_terms_choices').val()+"_month").innerHTML.replace('$', '')) + parseFloat($("#"+$('#id_terms_choices').val()+"_month_per_month_amount").val().split('/')[0].replace('$', ''))).toFixed(2)
    $('#btn_next').prop('disabled', true);
    if( $("#id_code").val().length >= 6)
       {
         $('#btn_next').prop('disabled', false);
       }

    $("#id_code").keyup(function(event){
    if(event.which === 8 || event.which === 13 || (event.which >= 48 && event.which <= 57) || (event.which >= 96 && event.which <= 105))
    {
       if( $("#id_code").val().length >= 6)
       {
         $('#btn_next').prop('disabled', false);
       }
       else
       {
         $('#btn_next').prop('disabled', true);
       }
    }
    else
    {
        $('#btn_next').prop('disabled', true);
        $("#id_code").val(
            function(index, value){
            return value.substr(0, value.length - 1);
        });
    }
  });

    $('#id_terms_choices').on('change', function() {
        $("#terms_dependency").show();
        $(".months").hide();

        $("."+this.value+"_month").show();
        if($('#id_is_insured').is(':checked')){
            $(".insurance").show();
            $('small').show();
            process_insurance(true);
        }
        else{
            $(".insurance").hide();
            $('small').hide();
            process_insurance(false);

        }
    });

    if($("#source_of_income").val() == '2'){
        $("#isurance_fee").hide();
        $("#insurance_checkbox").hide();
        $('#id_is_insured').prop('checked', false);

    }

    if($("#province").val() == 'QC' || $("#province").val() == 'SK'){
        $("#isurance_fee").hide();
        $("#insurance_checkbox").hide();
        $('#id_is_insured').hide();
    }

    $("#id_is_insured").on("change", function(){
        if ($('#id_is_insured').is(':checked')){
            $(".insurance").show();
            $('small').show();
            process_insurance(true);
        }
        else{
            $(".insurance").hide();
            $('small').hide();
            process_insurance(false);
        }
    });

    function process_insurance(is_active){
        if(is_active){
            $(".apr_with_insurance").show();
            $(".apr_without_insurance").hide();

            $("."+$('#id_terms_choices').val()+"_month").show();
            $("#insurance_checkbox").show();
            document.getElementById("monthly_installment_"+$('#id_terms_choices').val()+"_month").innerHTML = '$' +parseFloat(parseFloat(document.getElementById("monthly_installment_"+$('#id_terms_choices').val()+"_month").innerHTML.replace('$', '')) + parseFloat($("#"+$('#id_terms_choices').val()+"_month_per_month_amount").val().split('/')[0].replace('$', ''))).toFixed(2)
            $(".insurance_checkbox_fee_per_month_"+$('#id_terms_choices').val()+"_month").html($("#"+$('#id_terms_choices').val()+"_month_total_insurance_amount").val());
            $(".insurance_fee_per_month_"+$('#id_terms_choices').val()+"_month").html($("#"+$('#id_terms_choices').val()+"_month_per_month_amount").val());
        }
        else{
            $(".apr_with_insurance").hide();
            $(".apr_without_insurance").show();
            document.getElementById("monthly_installment_"+$('#id_terms_choices').val()+"_month").innerHTML = '$' +parseFloat(parseFloat(document.getElementById("monthly_installment_"+$('#id_terms_choices').val()+"_month").innerHTML.replace('$', '')) - parseFloat($("#"+$('#id_terms_choices').val()+"_month_per_month_amount").val().split('/')[0].replace('$', ''))).toFixed(2)
            $(".insurance_checkbox_fee_per_month_"+$('#id_terms_choices').val()+"_month").html("$0.00");
            $(".insurance_fee_per_month_"+$('#id_terms_choices').val()+"_month").html("$0.00 / month");

        }

    }
});
