$(document).ready(function(){
    $("fieldset").addClass("border border-dark rounded p-2").children("legend").addClass("w-auto mx-2");
    $("fieldset[id$='values']").css("display","none").addClass("px-4");
    $("#figure-values fieldset").addClass("h-100").parent("div").addClass("col col-12 px-1").parent("div").addClass("mb-4");
    $("fieldset[id^='operation-']").css("display","none");

    const input_template = `<div class="form-group row">
                        <label for="" class="col-5 "></label>
                        <input type="number" class="form-control col-7" name="" id="" placeholder="00" step="any">
                    </div>`;
    let figures = {};

    $("#figure-options input:checkbox").change(function(){
        
        const figure = $(this).val();

        if ($(this).is(":checked")) {
            figures[figure] = {};
        } else {
            delete figures[figure];
        }

        showOperations(figure);
    });

    $("fieldset[id^='operation-']").change(function(){
        
        const operations = $(this).find(`input:checkbox:checked`).map((index,input)=>{
            return $(input).val();
        }).get();
        
        const figure = $(this).attr("id").split("-")[1];
        const previous_figure_length = figures[figure].length ? figures[figure].length:0;

        figures[figure] = operations;
        showValueParam(figure,previous_figure_length);  
        enableSubmit();   
    })

    const showValueParam = (figure, prevLength) => {
        if(prevLength == 0 && figures[figure].length > 0){
            figuresOperations[figure].createInputs();
        } else if(!figures[figure] || figures[figure].length == 0) {
            figuresOperations[figure].deleteInputs();
        }

        if(figures['poligon'] && figures[`poligon`].length > 0 && figures['poligon']?.includes('area') && !$('input#apothem').length>0){
            $('#poligon_values>div').append(createInput("Apotema","apothem"));

        } else  if(!figures['poligon'] || (figures[`poligon`].length > 0 && !figures['poligon'].includes('area'))){
            $('input#apothem').parent("div").remove();
        }
    }

    const showOperations = (figure) => {
        const figureFieldOpts = $(`fieldset#operation-${figure}`);

        if(!figures[`${figure}`]){    
            figureFieldOpts.find("input:checkbox").prop("checked",false);
            figuresOperations[`${figure}`].deleteInputs();   
        }
        figureFieldOpts.css("display", figures[`${figure}`] ? "block":"none");

        enableSubmit();    
    }

    const enableSubmit = () => {
        if(Object.keys(figures).length && Object.values(figures).some(figure => figure.length >0)){
            $("button").attr("disabled",false).removeClass("btn-secondary").addClass("btn-primary");
            
        } else {
            $("button").attr("disabled",true).removeClass("btn-primary").addClass("btn-secondary");
        }
    }

    const validate_figure_values = () => {
        const figure_values = $("fieldset[id$='values'] input").map((index, input)=>{
            return $(input).val();
    
        }).get();

        return figure_values.every(function(value){
            return value > 0;
        })
    }

    const createInput = (label,property) => {
        const new_input = $(input_template).clone()

        new_input.find("label").prop("for", property).text(label);
        new_input.find("input").prop("id", property).prop("name", property);
        return new_input;
    }

    $("#figures_calculations").submit(function(event){
        event.preventDefault();
        $("#results").empty();
        
        if(validate_figure_values()){
            for (let figure in figures){

                const variables = figuresOperations[figure].getVariables();
                choose_figure_operation(variables, figure);
            }



        } else {
            alert(`No se pueden enviar datos menores o iguales a 0`);
        }
    })

    const choose_figure_operation = (figureVariables, figure) => {
        for (let operation of figures[`${figure}`]){
            let value = figuresOperations[figure][operation](figureVariables);
            let label = ""

            value = value%1 === 0 ? value : value.toFixed(2);

            if(operation === "area"){
                label = "Área";
            } else if (operation === "perimeter"){
                label = "Perímetro";
            }
            
            addResult(value, label, figure);
        }
    }
    const addResult = (value, operation, figure) => {
        if($(`div#${figure}-result`).length==0){
            let spanishLabel;

            switch (figure) {
                case "triangle":
                    spanishLabel="Triángulo"
                    break;
                case "rectangle":
                    spanishLabel="Rectángulo"
                    break;
                case "poligon":
                    spanishLabel="Polígono"
                    break;
                default:
                    break;
            }
            

            $(`#results`).append(`<div id="${figure}-result"><h3>${spanishLabel}:</h3></div>`)
        }

        $(`div#${figure}-result`).append(`<p>${operation}: ${value}</p>`);
    }

    const figuresOperations = {
        triangle: {
            createInputs(){
                const input_template = $(`<div>`); 
                input_template.append(createInput("Base","base")) ;
                input_template.append(createInput("Altura","height"));
                
                
                $('#triangle_values div').html(input_template);
                $('#triangle_values').css("display","block");
            },
            deleteInputs(){
                $('#triangle_values div').empty();
                $('#triangle_values').css("display","none");
            },
            getVariables(){
                let base = $("input#base").val();
                let height = $("input#height").val();
                base = parseFloat(base);
                height = parseFloat(height);

                return {base: base, height: height};                        
            },
            area(variables){
                return (variables.base*variables.height)/2;
            },
            perimeter(variables){
                const side = Math.sqrt(Math.pow(variables.height, 2) + Math.pow(variables.base, 2));
                return (variables.base + side + variables.height);
            }
        },
        rectangle:{
            createInputs(){
                const input_template = $(`<div>`); 
                input_template.append(createInput("Lado 1","side_1")) ;
                input_template.append(createInput("Lado 2","side_2"));
                

                $('#rectangle_values div').html(input_template);
                $('#rectangle_values').css("display","block");
            },
            deleteInputs(){
                $('#rectangle_values div').empty();
                $('#rectangle_values').css("display","none");
            },
            getVariables(){
                let side_1 = $("input#side_1").val();
                let side_2 = $("input#side_2").val();
                side_1 = parseFloat(side_1);
                side_2 = parseFloat(side_2);

                return {side_1: side_1, side_2:side_2}
            },
            area(variables){
                return variables.side_1 * variables.side_2;
            },
            perimeter(variables){
                return variables.side_1*2 + variables.side_2*2;
            }
        },
        poligon:{
            createInputs(){
                const input_template = $(`<div>`); 
                input_template.append(createInput("N. De Lados","n_sides")) ;
                input_template.append(createInput("Medida de Lado","size"));
                
                $('#poligon_values div').html(input_template);
                $('#poligon_values').css("display","block");
            },
            deleteInputs(){
                $('#poligon_values div').empty();
                $('#poligon_values').css("display","none");
            },
            getVariables(){
                let n_sides = $("input#n_sides").val();
                let size = $("input#size").val();
                n_sides = parseFloat(n_sides);
                size = parseFloat(size);
                let apothem = undefined;

                if(figures.poligon.includes("area")){
                    apothem = $("input#apothem").val();
                    apothem = parseFloat(apothem);
                }

                return {n_sides: n_sides, size: size, apothem: apothem};
                
            },
            area(variables){
                const perimeter = figuresOperations.poligon.perimeter(variables);
                return (perimeter*variables.apothem)/2;
            },
            perimeter(variables) { return variables.n_sides*variables.size; }
        }
    }   
})