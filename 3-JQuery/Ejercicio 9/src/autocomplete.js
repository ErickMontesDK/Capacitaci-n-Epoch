$( function() {
    $( "#country" ).autocomplete({
        
        source: function(request, response) {
            $.getJSON("src/countries.json", function(data) {

                const filteredData = $.grep(data, function(item) {
                    return item.name.toLowerCase().indexOf(request.term.toLowerCase()) > -1;
                });

                const availableTags = $.map(filteredData, function(item) {
                    return {
                    label: item.name,
                    value: item.name
                    };
                });
                
                response(availableTags);
            });
        },
        minLength:2

    });
} );