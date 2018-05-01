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

                    $('#dashboard').append('<div>Upload Success<br/></div>');
                    var img = $('<img id='+'\'uploadImage\''+' height="128" width="128">'); //Equivalent: $(document.createElement('img'))
                    img.attr('src', 'img/ip/'+data['input_image']);
                    img.appendTo('#inputimagediv');

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
                $('#dashboard').append('<div>Execute Success<br/></div>');
                for (i=0;i<data['target_images_list'].length;i++) {
                    console.log(data['target_images_list'][i]);
                    var img = $('<img id="image_target"+i height="128" width="128">'); //Equivalent: $(document.createElement('img'))
                    img.attr('src', 'img/target/'+data['target_images_list'][i]);
                    img.appendTo('#targetimagediv');
                }

                for (i=0;i<data['output_images_list'].length;i++) {
                    var img = $('<img id="image_output"+i height="128" width="128">'); //Equivalent: $(document.createElement('img'))
                    img.attr('src', 'img/gen/'+data['output_images_list'][i]);
                    img.appendTo('#outputimagediv');
                }

        

        }
        else {
                 files = null;
                $('#dashboard').append('<div>Comparision failed. Sent Generated</div>');
                for (i=0;i<data['target_images_list'].length;i++) {
                    var img = $('<img id="image_target"+i height="128" width="128">'); //Equivalent: $(document.createElement('img'))
                    img.attr('src', 'img/target/'+data['target_images_list'][i]);
                    img.appendTo('#targetimagediv');
                }

                for (i=0;i<data['output_images_list'].length;i++) {
                    var img = $('<img id="image_output"+i height="128" width="128">'); //Equivalent: $(document.createElement('img'))
                    img.attr('src', 'img/gen/'+data['output_images_list'][i]);
                    img.appendTo('#outputimagediv');
                }


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