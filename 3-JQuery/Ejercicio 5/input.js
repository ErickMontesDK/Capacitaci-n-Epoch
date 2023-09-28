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

        const input_chars = $("form input").val().split("").filter((char)=>{
            return char !== " ";
        })
        const vocalRegex = /[aeiouáéíóú]/i;
        const numberRegex = /[0-9]/;
        const consonantRegex = /[bcdfghjklmnpqrstvwxyz]/i;

        const vocals = input_chars.filter((char)=>{
            return char.match(vocalRegex);
        })
        const numbers = input_chars.filter((char)=>{
            return char.match(numberRegex);
        })
        const consonants = input_chars.filter((char)=>{
            return char.match(consonantRegex);
        })
        
        $("#vocals").text("["+"'"+vocals.join("', '")+"'"+"]");
        $("#numbers").text("["+numbers.join(", ")+"]");
        $("#consonants").text("["+"'"+consonants.join("', '")+"'"+"]");

        $("output").css("display","block");
    })

})
