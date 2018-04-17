var files;
function prepareUpload(event) {

    files = event.target.files;
    var file = files[0];

    console.log(file['name'] );

}

function uploadFiles(event) {
    if (files == null)
        return;
    var data = new FormData();
    var file = files[0];
    data.append('sketch', file, file.name);
    // $("#loader").attr('class', 'show_loader');
    $.ajax({
        url: uploadUrl,
        type: 'POST',
        data: data,
        cache: false,
        enctype: 'multipart/form-data',
        dataType: 'json',
        processData: false,
        contentType: false,
        success: function(data, textStatus, jqXHR) {

            if (data["success"] === "true") {


            //




                    $('#dashboard').append('<div>Upload Success<br/></div>');


            }
            else {

            //
                    $('#dashboard').append('<div>Upload Failure But Got Response</div>');


            }


                    },
        failure: function(data) {
                            $('#dashboard').append('<div>Upload Failure</div>');


        }
    });

}


function execute(event) {


    $.ajax({
        url: executeUrl,
        type: 'POST',
        cache: false,
        dataType: 'json',
        processData: false,
        contentType: false,
        success: function(data, textStatus, jqXHR) {

            if (data["success"] === "true") {
                files = null;
                $('#dashboard').append('<div>Execute Success<br/>'+data['images_list']+'</div>');



        

        }
        else {

                $('#dashboard').append('<div>Execute Failure But Got Response</div>');

            }
        // $("#log").append(data["message"] + "<br />");

    },
        failure: function(data) {
                $('#dashboard').append('<div>Execute Failure</div>');


        }
    });
}

$(function() {
    $('input[id^="sketch"]').on('change', prepareUpload);

});