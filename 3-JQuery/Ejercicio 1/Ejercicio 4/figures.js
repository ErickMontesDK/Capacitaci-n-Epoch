
        $(document).ready(function(){
            $("fieldset").addClass("m-3 border border-dark rounded p-2 h-100").children("legend").addClass("w-auto mx-2 px-2");
            $("div#figure-values").css("display","none");

            const input_template = `<div class="form-group row">
                        <label for="" class="col-5 "></label>
                        <input type="number" class="form-control col-7" name="" id="" placeholder="00" step="any">
                    </div>`;
            let figure = "";
            let operation_selected = []

            $("#figure-options input:radio").change(function(){
                figure = $("input:radio:checked").val();

                inputs_required();
            })

            $("#operation-options input:checkbox").change(function(){
                operation_selected = $("input:checkbox:checked").map((index,input)=>{
                    return $(input).val();
                }).get();
                                
                inputs_required();
            })

            const createInput = (label,property) => {
                const new_input = $(input_template).clone()

                new_input.find("label").prop("for", property).text(label);
                new_input.find("input").prop("id", property).prop("name", property);
                return new_input;
            }

            const inputs_required = () =>{
                const previous_inputs = $("#figure_values_inputs").clone().children("div");
                
                if(figure !== "" && operation_selected.length > 0 ){
                    $("div#figure-values").css("display","block");
                    $("button").attr("disabled",false).removeClass("btn-secondary").addClass("btn-primary");

                    let new_inputs = figuresOperations[figure].createInputs();

                    if(previous_inputs.html() !== new_inputs.html()){
                        $("#figure_values_inputs").html(new_inputs);
                    } 
                } else {
                    $("#figure_values_inputs").empty();
                    $("button").attr("disabled",true).removeClass("btn-primary").addClass("btn-secondary");
                    $("div#figure-values").css("display","none");
                }
            }

            $("#figures_calculations").submit(function(event){
                event.preventDefault();
                $("#results").empty();

                if(figure !== "" && operation_selected.length > 0){
                    if(validate_figure_values()){
                        const variables = figuresOperations[figure].getVariables();
                        choose_figure_operation(variables, figure);

                    } else {
                        alert(`No se pueden enviar datos menores o iguales a 0`);
                    }
                    
                } else {
                    alert(`No se ha seleccionado ninguna operación`);
                }
            })

            const addResult = (value, operation) => {
                $("#results").append(`<p>${operation}: ${value}</p>`);
            }

            const validate_figure_values = () => {
                const figure_values = $("#figure_values_inputs input").map((index, input)=>{
                    return $(input).val();
                }).get();

                return figure_values.every(function(value){
                    return value > 0;
                })
            }

            const choose_figure_operation = (figureVariables, figure) => {
                for (let operation of operation_selected){
                    let value = figuresOperations[figure][operation](figureVariables);
                    let label = ""

                    value = value%1 === 0 ? value : value.toFixed(2);

                    if(operation === "area"){
                        label = "Área";
                    } else if (operation === "perimeter"){
                        label = "Perímetro";
                    }
                    addResult(value, label)
                }
            }


            const figuresOperations = {
                triangle: {
                    createInputs(){
                        let new_inputs = $("#figure_values_inputs").clone().empty();
                        new_inputs.append(createInput("Base","base")) ;
                        new_inputs.append(createInput("Altura","height"));
                        return new_inputs;
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
                        let new_inputs = $("#figure_values_inputs").clone().empty();
                        new_inputs.append(createInput("Lado 1","side_1")) ;
                        new_inputs.append(createInput("Lado2","side_2"));
                        return new_inputs;
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
                        let new_inputs = $("#figure_values_inputs").clone().empty();
                        new_inputs.append(createInput("N. De Lados","n_sides")) ;
                        new_inputs.append(createInput("Medida de Lado","size"));
                        
                        if(operation_selected.includes("area")){
                            new_inputs.append(createInput("Apotema","apothem")) ;
                        } 
                        return new_inputs;
                    },
                    getVariables(){
                        let n_sides = $("input#n_sides").val();
                        let size = $("input#size").val();
                        n_sides = parseFloat(n_sides);
                        size = parseFloat(size);
                        let apothem = undefined;

                        if(operation_selected.includes("area")){
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
