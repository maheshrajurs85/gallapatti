// if you modify any thing Please run command - "python manage.py collectstatic"

function validateForm(formId) {
    console.log('inside validate form 123');
    var form = document.getElementById(formId);
    var formElements = form.elements;

    for (var i = 0; i < formElements.length; i++) {
        var element = formElements[i];

        // Check if the element is required and its value is empty
        if (element.hasAttribute('required') && element.value.trim() === '') {
            alert('Please fill Field :', element.name);
            return false; // Prevent form submission
        }
    }

    // Continue with form submission if all required fields are filled
    return true;
}


function handleKeyDown(event, rowId, field, tableName) {
    console.log('inside handlekeydown');
    if (event.keyCode === 13) { // Check if Enter key is pressed
        event.preventDefault(); // Prevent new line in contenteditable
        updateCell(rowId, field, event.target.innerText, tableName);
    }
}


// pending - we  have to give user an information about the update
// if used tab - issue
function updateCell(rowId, field, value, tableName) {
            console.log("inside updateCell form 123");
            $.ajax({
                url: '/update_cell/',  // Replace with your Django view URL
                method: 'POST',
                data: {
                    'row_id': rowId,
                    'field': field,
                    'value': value,
                    'tableName': tableName,
                    'csrfmiddlewaretoken': '{{ csrf_token }}'
                },
                success: function (data) {
                    console.log(data);
                    console.log(field + ' Value Updated123: ' + value);
                    //window.alert('cell_' + rowId + '_' + field); //issue if used tab
                    // Below code is to hightlight the modified cell
                    var cellId = 'cell_' + rowId + '_' + field;
                    var modifiedCell = document.getElementById(cellId);
                    if (modifiedCell) {
                        modifiedCell.classList.add('updated-cell');
                        setTimeout(function () {
                            modifiedCell.classList.remove('updated-cell');
                        }, 2000);
                    }	

                },
                error: function (error) {
                    console.error('Error updating cell:', error);
                }
            });
}
