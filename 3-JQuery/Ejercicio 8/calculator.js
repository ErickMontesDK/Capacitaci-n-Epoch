$(document).ready(function(){

    $(`#display`).css("opacity",0.15);
    $(`button[id!='on-off']`).attr("disabled",true);
    const display = $('#display');
    let calcState = false;

    let value1=0;
    let value2=0;
    let gateValue = "value1"
    let gateDecimal = false;


    $(`#on-off`).click(function(){
        calcState = !calcState;

        if(calcState){
            $(`button[id!='on-off']`).attr("disabled",false);  
            $(`#on-off`).text('OFF');
            display.text('0').css("opacity",1);
        } else {
            $(`button[id!='on-off']`).attr("disabled",true);
            $(`#on-off`).text('ON');
            display.text('000000000').css("opacity",0.15);
        }
    })

    $(`button.number`).click(function(){
        const newNumber = $(this).text();
        // console.log(valInDisplay);
        
        if((display.text()==0 || display.text().length==0) && gateValue == "value1"){
            display.text(`${newNumber}`);
            value1 = parseFloat(newNumber);

        } else if(gateValue == "value1"){
            value1 = (value1*10)+parseFloat(newNumber);
            display.text(function(){
                return newNumber+display.text();
            })
            console.log(value1)

        } else if(gateValue == "value2"){

            if(value2==0){
                value2=parseFloat(newNumber);
            } else {
                value2 = (value2*10)+parseFloat(newNumber);
            }
            
            console.log(value2)

            display.text(function(){
                return newNumber+display.text();
            })
        }
    })

    $(`button.operation`).click(function(){
        const operation = $(this).text();
        $(`button.operation`).attr("disabled",true); 
        
        gateValue == "value1"? gateValue = "value2": gateValue;

        if(display.text()==0 || !display.text()){
            display.text(`${operation}0`);
        } else {
            display.text(function(){
                return `${operation+display.text()}`;
            })
        }
        
    })

    $(`#decimal`).click(function(){ 
        display.text(function(){
            return `.`+display.text();
        })
    })

    $(`#reset`).click(function(){
        display.text('0');
        value1 = 0;
        value2 = 0;
        gateValue = "value1";
        $(`button.operation`).attr("disabled",false); 
    })

})
