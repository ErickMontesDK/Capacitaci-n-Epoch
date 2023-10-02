$(document).ready(function(){

    $(`#display`).css("opacity",0.15);
    $(`button[id!='on-off']`).attr("disabled",true);
    const display = $('#display');
    let calcState = false;
    let gateOperation = false;    
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

        if(display.text() ==="0" || display.text().length==0){
            display.text(`${newNumber}`);
        } else {
            display.text(()=>{  return newNumber+display.text();   })
        }
        gateOperation = false;

    })

    $(`button.operation`).click(function(){
        if(!gateOperation){
            const operation = $(this).text();
            gateOperation = true;
            gateDecimal = false;

            if(display.text()==0 || !display.text()){
                display.text(`${operation}0`);
            } else {
                display.text(function(){
                    return `${operation+display.text()}`;
                })
            }
        }
    })

    $(`#decimal`).click(function(){ 
        if(display.text()==0 || display.text().length==0){
            display.text(`.0`);
            gateDecimal = true;

        } else if(!gateDecimal){
            display.text(()=>{    return `.`+display.text();  })
            gateDecimal = true;

        }
        gateOperation = false;
    })

    $(`#reset`).click(function(){
        display.text('0');
        gateDecimal = false;

        $(`button.operation`).attr("disabled",false); 
    })

    $(`#delete`).click(function(){
        let inDisplay = display.text();
        const regexOperation = /[-x÷\+]/
        const deleteElement = inDisplay.slice(0,1);
        const beforeElement = inDisplay.slice(1,2);
        inDisplay = inDisplay.slice(1);
        display.text(inDisplay);

        if(regexOperation.test(beforeElement)){ gateOperation = true;   }

        if(inDisplay.length <= 1){
            display.text("0");

        } else if(deleteElement === "."){
            gateDecimal = false;

        } else if(regexOperation.test(deleteElement)){
            gateOperation = false;
            const lastOperationIndex =inDisplay.search(regexOperation);
            const lastDecimal = inDisplay.indexOf(".");

            if((lastOperationIndex<lastDecimal && lastOperationIndex>0) || lastDecimal<0){
                gateDecimal = false;
            } else {
                gateDecimal = true;
            }
        }
    });

    $(`#solve`).click(function(){
        const lastElement = display.text().slice(0,1);
        const mathRegex = /[0-9.]/;

        if(mathRegex.test(lastElement)){
            let mathExpression = display.text().split("").reverse().join("");
            mathExpression = mathExpression.replace(/x/g,'*');
            mathExpression = mathExpression.replace(/÷/g,'/');
            console.log(mathExpression);

            let Result = eval(mathExpression);
            console.log(Result)
            Result = Result%1 == 0? Result:Result.toFixed(3);
            display.text(String(Result).split("").reverse().join(""));

            const lastDecimal = display.text().indexOf(".");
            gateDecimal = lastDecimal == -1? false: true;
            console.log(lastDecimal)

        } else {
            console.log("Error")
        }
    })

    $(document).on("keydown",function(event){
        if(event.which == 37){
            display.scrollLeft((display.scrollLeft()-10));
        } else if(event.which==39){
            display.scrollLeft((display.scrollLeft()+10));
        }
    })

    $("#decimal, .operation, #solve ").on("mousedown", function() {
        $(this).removeClass("btn-secondary");

        if($(this).attr("id")=="decimal"){
            gateDecimal? $(this).addClass("btn-danger"):$(this).addClass("btn-success");

        } else if($(this).attr("class").includes("operation")){
            gateOperation? $(this).addClass("btn-danger"):$(this).addClass("btn-success");

        } else {
            const lastElement = display.text().slice(0,1);
            const mathRegex = /[0-9]/;

            !mathRegex.test(lastElement)? $(this).addClass("btn-danger"):$(this).addClass("btn-success");
        }
    });

    $("#decimal, .operation, #solve ").on("mouseup", function() {
        $(this).addClass("btn-secondary");
        $(this).removeClass("btn-success");
        $(this).removeClass("btn-danger");
    });

})
