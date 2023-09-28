$(document).ready(function(){
    $("output").css("display","none");

    $("#input-separate").on("input", function(){

        const input_val = $("form input").val();

        if(input_val.trim() !== ""){
            $("button").prop("disabled",false).removeClass("btn-secondary").addClass("btn-primary");
        } else {
            $("button").prop("disabled",true).removeClass("btn-primary").addClass("btn-secondary");
        }
    })

    $("#input-separate").submit(function(event){
        event.preventDefault();

        const input_chars = $("form input").val().trim().replace(/ /g, "").toLowerCase();

        const char_analyzed = [];
        const result_arrange = [];

        for ( let char of input_chars){
            if(!char_analyzed.includes(char)){
                
                const regex = new RegExp(`${char}`,"ig");
                const char_quantity = input_chars.match(regex).length;

                char_analyzed.push(char);
                result_arrange.push([char, char_quantity]);
            }
            
        }

        $("#chars").html("[<br>"+"["+result_arrange.join("],<br>[")+"]<br>]");
        $("output").css("display","block");
        
    })

})
