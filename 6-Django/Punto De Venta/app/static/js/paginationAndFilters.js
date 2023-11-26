$(document).ready(function(){
    let page = 1
    let orderParameter = 'id'
    let pageParam = ""
    let orderParam = ""
    let filterParams = ""
    let accion = ""
    let excel_url = ""

    if (typeof excel_download_url !== 'undefined') {
        // Usar la variable excel_download_url como quieras
        excel_url = excel_download_url
      } 
        
    const createPagination = (total_records) =>{
        const records_per_page = 10
        const n_pages = total_records/records_per_page
        let pages_container = ""

        let i=0;
        while( i < n_pages){
            pages_container += `<li class="page-item"><a class="page-link" href="#">${i+1}</a></li>`
            i++
        }
        pages_container = $(pages_container)
        $('#list_table_pagination').find('li:not(:first-child):not(:last-child)').remove();
        $('#list_table_pagination').children('li').first().after(pages_container)
        $('#total_records').text(total_records)
    }
    
    createPagination(total_records)

    const createUrl = (baseUrl)=>{
        return baseUrl+'?'+orderParam+pageParam+filterParams
    }
    
    updateExcelUrl = ()=>{
        let url = createUrl(excel_url)
        $('#excel_import').attr('href', url)
    }
    updateExcelUrl()

    const chargeData = ()=>{
        const urlWithParams = createUrl(baseUrl)
        updateExcelUrl()
        
        history.pushState({}, '', urlWithParams);
        
        $.ajax({
            url: urlWithParams,
            type: "GET",
            dataType: 'json'
        }).done(function(data){  
            $('#query_body').html(data.html)
            createPagination(data.query_size)
            showSelectedPage(page)

        }).fail(function(data){
            alert("Error: no se proceso correctamente la solicitud")
        })
    }

    const showSelectedPage =(pageSelected)=>{
        $('#list_table_pagination').find('a').removeClass('disabled').removeClass('bg-secondary');

        if(pageSelected == '«'){
            page -= 1
        } else if(pageSelected == '»'){
            page += 1
        } else {
            page = Number(pageSelected)
        }

        $('#list_table_pagination').find('li:contains(' + page + ') a').addClass('disabled').addClass('bg-secondary');
    }
    

    const viewPageControls = () => {
        let lastPage = $('#list_table_pagination').children('li').length;
        $('#previous-page').css("display", page == 1 ? "none" : "block");
        $('#next-page').css("display", page == lastPage - 2 ? "none" : "block");
    }

    $('#list_table_pagination').on('click', '.page-link',function(event){
        event.preventDefault()
        let optionClicked = $(this).text()
        
        showSelectedPage(optionClicked)
        pageParam = `page=${encodeURIComponent(page)}`+"&"
        chargeData()
        viewPageControls()
    })
    $('#order_trigger .dropdown-menu .dropdown-item').click(function () {
        orderParameter = $(this).val()
        page = 1

        orderParam = `orderBy=${encodeURIComponent(orderParameter)}`+"&"
        showSelectedPage(page);
        chargeData(page, orderParameter)
        viewPageControls()
    })

    $('form').submit(function (event) {
        
        event.preventDefault()
        const filtersInputs = $(this).children('#filters').children()
        let queryParams = []
        
        $.each(filtersInputs, function(index, fieldFilter){
            const checkbox_Value = $(fieldFilter).find("input[id^='filter_checkbox_']").prop("checked")

            if (checkbox_Value){
                const filter_input =  $(fieldFilter).find("[id^='filter_input_']")
                const filter_value = filter_input.val()
                const field_name = filter_input.prop("id").slice(13,)
                queryParams.push(`${field_name}=${encodeURIComponent(filter_value)}`)
            }
        })
        filterParams = `${queryParams.join('&')}`+'&'
        pageParam = `page=${encodeURIComponent(1)}`+"&"
        
        showSelectedPage(page);
        chargeData(page, orderParameter)
        viewPageControls()
    })

    showSelectedPage(page);
    chargeData(page, orderParameter)
    viewPageControls()

})