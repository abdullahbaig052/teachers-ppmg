$(document).ready(function () {

    $("#loans").DataTable({
        "order": [[ 0, "desc" ]],
        "pageLength": 50,
    });

    $('#downloads').on('change', function() {
      if (this.selectedIndex !== 0) {
        window.location.href = this.value;
      }
    });

});

