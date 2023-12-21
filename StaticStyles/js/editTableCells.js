function validateForm() {//
            var form = document.getElementById('newGoodsForm');
            var inputs = form.getElementsByTagName('input');

            for (var i = 0; i < inputs.length; i++) {
                var input = inputs[i];

                // Check if the input is required and its value is empty
                if (input.hasAttribute('required') && input.value.trim() === '') {
                    alert('Please fill in all fields.');
                    return false; // Prevent form submission
                }
            }

            // Continue with form submission if all required fields are filled
            return true;
}

// pending - we  have to give user an information about the update
// if used tab - issue
function updateCell(rowId, field, value) {
            $.ajax({
                url: '/update_cell/',  // Replace with your Django view URL
                method: 'POST',
                data: {
                    'row_id': rowId,
                    'field': field,
                    'value': value,
                    'csrfmiddlewaretoken': '{{ csrf_token }}'
                },
                success: function (data) {
                    console.log(field + ' Value Updated: ' + value);
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
