$(document).ready(function(){
    var $post_form = $('.my-ajax-form');
    $post_form.submit(function(event){
        event.preventDefault();
        var $formData = $post_form.serialize();
        console.log($formData);
        var $thisURL = $post_form.attr('data-url') || window.location.href;
        console.log($thisURL);
        $.ajax({
            method:'POST',
            url:$thisURL,
            data:$formData,
            success:handleSuccess,
            error: handleError,
        });
    });
});