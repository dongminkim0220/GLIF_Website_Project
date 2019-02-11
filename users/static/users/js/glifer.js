$(document).ready(function(){
    var next = 0;
    var count = 1;
    $(".add-more").click(function(e){
        e.preventDefault();
        var addto = "#id_form-" + next + '-career';
        var addRemove = "#id_form-" + next + '-career' ;
        
        next = next + 1;
        count++;
        document.getElementById('id_form-TOTAL_FORMS').setAttribute("value", count);
        
        var newIn = '<input autocomplete="off" placeholder = "enter here" class="form-control" id="id_form-' + next +'-career'+ '" name="form-' + next +'-career'+ '" type="text"><div></div>';
        var newInput = $(newIn);

        var removeBtn = '<a href = "#" style = "color:black;" id="remove' + (next - 1) + '" class="remove-me" >Delete This</button>';
        var removeButton = $(removeBtn);

        $(addto).after(newInput);
        $(addRemove).after(removeButton);

        removeButton.click(function(e){
            e.preventDefault();
            var fieldNum = this.id.charAt(this.id.length-1);
            var fieldID = "#id_form-" + fieldNum + '-career';
            $(this).remove();
            $(fieldID).remove();
        });

        removeButton.click(function(e){
            count--;
            document.getElementById('id_form-TOTAL_FORMS').setAttribute("value", count);
        });
            
    });

    
});
