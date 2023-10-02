$(`document`).ready(function(){

    $(`#states`).change(function(){
        let state = $(this).val();
        state = state.toLowerCase();

        $.ajax({
            type: "GET",
            url: "src/EstadosYCiudades.json",
            data: "data",
            dataType: "json",
            success: function (response) {            
                const citys = response[`${state}`];
                const cityOptions = $(`<optgroup></optgroup>`);

                $(citys).each(function (index, city) { 
                    let capitalizeCity;

                    $(city.split(" ")).each(function(index, word){
                        const capitalizeWord = word.charAt(0).toUpperCase() + word.slice(1);
                        
                        capitalizeCity = index==0? capitalizeWord:capitalizeCity+" "+capitalizeWord;
                    })

                    cityOptions.append(`<option value="${city.toUpperCase()}">${capitalizeCity}</option>`)
                });

                $(`#city`).html(cityOptions);
            }
        });
        
    })

    $(`#name`).blur(function(){
        let name = $(this).val();
        name = name.toUpperCase();
    
        $(this).val(`${name}`);
    })
    
    $(`#date`).change(function(){
        let birthDate = $(this).val();
        birthDate = new Date(birthDate);
        
        const todayDate = new Date();
    
        const timeDifference = todayDate.getTime() - birthDate.getTime();
        const years = (timeDifference)/(1000 * 60 * 60 * 24 * 365.25);
    
        $(`#age`).val(years.toFixed())
    })

    $(`#phone`).inputmask({"mask":"(999)-999-99-99"});
    
})

