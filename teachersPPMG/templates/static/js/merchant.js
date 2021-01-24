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

    $('#downloads').on('change', function() {
      if (this.selectedIndex !== 0) {
        window.location.href = this.value;
      }
    });

});

