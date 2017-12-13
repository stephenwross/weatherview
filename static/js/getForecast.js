     $(function() {
       $('a#process_input').bind('click', function() {
          $.getJSON('/show_forecast', {
            inputLoc: $('input[name="inputLoc"]').val(),
              }, function(data) {
                 $("#result").text(data.result);
                 });
             return false;
           });
      });

