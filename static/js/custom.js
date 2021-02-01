$(document).ready(function(){
    var mytable = $("#mytable").DataTable({
      /*ajax:'static/data.json',*/
      /*"processing": true,*/
      "ajax": {
        "processing": true,
        "url":"/static/data.json",
        "dataSrc": ""
      },
      "columns": [
          { "data": "pk"},
          { "data": "fields.name"},
          { "data": "fields.played_Count"},
          { "data": "fields.wins"},
          { "data": "fields.losses"},
          { "data": "fields.tie"},
          { "data": "fields.score"},
      ],
      "order":[[1,'dsc']],
      columnDefs: [
        {
          targets:0,
          checkboxes:{
            seletRow:true
          }
        }
      ],
      select:{
        style:'multi'
      },
    });
    $('#myform').on('submit',function(e){
      var form = this 
      var rowsel = mytable.column(0).checkboxes.selected();
      if (rowsel == 2) {
          $.each(rowsel,function(index,rowId){
            $(form).append(
              $('<input>').attr('type','hidden').attr('name','pk').val(rowId)
            )
          });
          $("#view-rows").text(rowsel.join(","))
          $("#view-form").text($(form).serialize())
          $('input[name="pk\[\]"]',form).remove()
      }
      else {
        alert("Cant't be more than 2");  
      }
      /*e.preventDefault()*/
    });
});
