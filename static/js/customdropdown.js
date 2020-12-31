$("#exampleFormControlInput1").on('change', function(e){
    var seasons = $("#exampleFormControlInput1").find('option:selected').text(); 
    $("#option-container").children().appendTo("#exampleFormControlInput2");
    $("#exampleFormControlInput2").children().removeAttr('disabled');
    var selectSeason = $("#exampleFormControlInput2").children("[data-group!='"+seasons+"']"); 
    $(selectSeason).attr('disabled','disabled');
    $("#exampleFormControlInput2").val($("#exampleFormControlInput2 optgroup[data-group='"+ seasons +"'] option:eq(0)").val());
    selectSeason.appendTo("#option-container");
    $("#exampleFormControlInput2").removeAttr("disabled"); 
});