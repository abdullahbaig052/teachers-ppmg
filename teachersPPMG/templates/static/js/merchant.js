$(document).ready(function () {

    $("#loans").DataTable({
        "order": [[ 0, "desc" ]],
        "pageLength": 50,
        "columnDefs": [{
            "targets": 1,
            "orderable": false
        },
        {
            "targets": 4,
            "visible": false
        },
        {
            "targets": 5,
            "visible": false
        },
        {
            "targets": 6,
            "visible": false
        }
        ]
    });


    $("#date_picker").daterangepicker({
        locale: {
            format: "YYYY-MM-DD"
        }
    });

    $('#date_picker').on('apply.daterangepicker', function(ev, picker) {
        date_start = picker.startDate.format('YYYY-MM-DD');
        date_end = picker.endDate.format('YYYY-MM-DD');
        window.location.href = window.location.pathname + "?date_start=" + date_start + "&date_end=" + date_end;
    });



    $('#downloads').on('change', function() {
      if (this.selectedIndex !== 0) {
        window.location.href = this.value;
      }
    });

});

