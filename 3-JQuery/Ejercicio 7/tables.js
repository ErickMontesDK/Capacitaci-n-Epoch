$(document).ready(function () {
    $("form").addClass("border border-dark rounded p-1");
    $("legend").addClass("w-auto");
    $("form label").addClass("form-label col-sm-5");
    $("form input").addClass("form-control col-sm-7");
    $("button[id^='insert']").addClass("btn btn-success p-1 w-100 mb-1")
    $("button[id^='delete']").addClass("btn btn-danger p-1 w-100 mb-1");
    $("#edit-table button").attr("disabled",true);
    $('#edit-table').hide();
    $('#edit-cell').hide();
    $(`#cell-menu`).hide();

    const table_template = `<table></table>`
    let cell_active_location = {col:-1, row:-1};
    let cell_active_element;
    let actualCellValue;




    const validateTableSize = () => {
        const table_size = $("#create-table input").map(function(index, value){
            return $(value).val();
        }).get();
    
        return table_size.every(function(value){
            return value > 0;
        })
    }

    const createTable = (columns, rows) => {
        const table = $(table_template).addClass("table table-dark text-center");
        

        for (let i=0; i < rows; i++){
            const row = $("<tr>");

            for(let j=0; j < columns; j++){
                const column = $("<td>").addClass("border border-light").append($(`<p>${j+1}-${i+1}</p>`));

                $(row).append(column);
            }
            $(table).append(row);
        }
        $("#table-container").html(table);
        $('#edit-table').show();
        $('#edit-cell').show();
    }
    
    $("#create-table").submit(function(event){
        event.preventDefault();
    
        if(validateTableSize()){
            $("#edit-table button").attr("disabled",false);
            const columns = $("#columns").val();
            const rows = $("#rows").val();

            createTable(columns, rows);

        } else {
            alert(`No se pueden enviar datos menores o iguales a cero`)
        }
    })

    $("#deleteAll").click(function () {
        $("#table-container table").remove();
        $("#edit-table button").attr("disabled",true);
        $('#edit-table').hide();
        availableEditMenu();
    })

    $("#delete-1nlast-row").click(function () {
        $("#table-container table tr:first").remove();
        $("#table-container table tr:last").remove();

        availableEditMenu();
    })

    $("#delete-1nlast-col").click(function () {
        $("#table-container table tr td:first-child").remove();
        $("#table-container table tr td:last-child").remove();

        availableEditMenu();
    })

    const validateCellInput = (column, row) => {
        const tableInDisplay = $("#table-container > table");
        let state = "";
        let cell;

        if( column > 0 && row > 0){
            const selectedRow = tableInDisplay.find(`tr:nth-child(${row})`);
            const selectedColumn = selectedRow.find(`td:nth-child(${column})`);
            if(selectedRow.length > 0 && selectedColumn.length > 0){
                state = "Valid";
                cell = selectedColumn;
            } else {
                state = "Not cell"
            }
        } else {
            state = "Not values";
        }

        return {state: state, cell:cell}
    }

    const availableEditMenu = () =>{
        if($(`#table-container tr`).length==0 || $(`#table-container td`).length==0){ 
            $(`#table-container table`).remove();
            $('#edit-table').hide(); 
            $('#edit-cell').hide(); 
        }
    }

    $("#edit-cell").submit(function (event) {
        event.preventDefault();

        let cell_col = $("#cell_col").val();
        cell_col = parseInt(cell_col);
        let cell_row = $("#cell_row").val(); 
        cell_row = parseInt(cell_row);
        console.log($(`#cell_text`).parent().html())
        let cell_text = $("#cell_text").val(); 
        cell_text = String(cell_text);

        const cellState = validateCellInput(cell_col,cell_row);
        
        if(cellState.state === "Valid"){
            console.log(cellState.cell.html())
            console.log(cell_text)
            cellState.cell.children("p").text(`${cell_text}`);

        } else if(cellState.state === "Not cell"){
            alert("La celda ingresada no existe");

        } else {
            alert("Los datos no pueden ser igual o menores a cero");
        }
    })

    $("#table-container").on("click","td",function(){
        const col = $(this).index();
        const row = $(this).parent().index();
        const cell_selected = {col:col, row:row};

        if(JSON.stringify(cell_active_location) !== JSON.stringify(cell_selected)){

            cell_active_location = cell_selected;
            $("#cell-menu").show();
            $("#table-container td").removeClass("bg-warning");
            $(this).addClass("bg-warning");

            cell_active_element? cell_active_element.html(`<p>${actualCellValue}</p>`):undefined;
            cell_active_element = $(this)
            actualCellValue = $(this).children("p").text();

            const inputElement = $(`<input type:"text">`).val(actualCellValue? actualCellValue:"").attr("id","cell_input");
            $(this).html(inputElement.clone());


        } else {
            cell_active_location = {col:-1, row:-1};
            $("#cell-menu").hide();
            $(this).removeClass("bg-warning");
            $(this).html(`<p>${actualCellValue}</p>`);
        }
    })

    $('#table-container').on("click","input",function(event){
        event.stopPropagation();
    })

    $('#table-container').on("keyup","input",function(event){
        if(event.which === 13){

            actualCellValue = $(this).val();
            $(this).replaceWith(`<p>${actualCellValue}</p>`);
        }
    })

    const createRowForSelectedCell = () => {
        const row = cell_active_element.parent();
        const cell_number = row.find("td").length;
        const new_row = $(`<tr></tr>`);

        for(let i=0; i < cell_number; i++){
            const column = $("<td>").addClass("border border-light").append($(`<p></p>`));
            new_row.append(column);
        }

        return new_row;
    }

    $("#insert-row-up").click(function(){
        const new_row = createRowForSelectedCell();
        
        new_row.insertBefore(cell_active_element.parent());
        cell_active_location = {col:cell_active_location.col, row:cell_active_location.row+1};
    })

    $("#insert-row-down").click(function(){
        const new_row = createRowForSelectedCell();
        
        new_row.insertAfter(cell_active_element.parent());
    })

    $("#insert-col-left").click(function(){
        const cell_index = cell_active_element.index();
        const n_rows = cell_active_element.parent("tr").parent("table").find("tr").length;
        const cel = $("<td>").addClass("border border-light").append($(`<p></p>`));

        cel.insertBefore($(`#table-container table td:nth-child(${cell_index+1})`));
        cell_active_location = {col:cell_active_location.col+1, row:cell_active_location.row};
    });

    $("#insert-col-right").click(function(){
        const cell_index = cell_active_element.index();
        const n_rows = cell_active_element.parent("tr").parent("table").find("tr").length;
        const cel = $("<td>").addClass("border border-light").append($(`<p></p>`));

        cel.insertAfter($(`#table-container table td:nth-child(${cell_index+1})`));
    });
    $("#delete-row-actual").click(function(){
        const row = cell_active_element.parent();
        
        $("#cell-menu").hide();
        row.remove();
        availableEditMenu();
        cell_active_location = {col:-1, row:-1};
    });

    $("#delete-col-actual").click(function(){
        const cell_index = cell_active_element.index();
        
        $("#cell-menu").hide();
        $(`#table-container table td:nth-child(${cell_index+1})`).remove();
        availableEditMenu();
        cell_active_location = {col:-1, row:-1};
    });


})

    

