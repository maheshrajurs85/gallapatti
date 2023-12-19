// static/admin/js/custom_admin.js
document.addEventListener('DOMContentLoaded', function () {
    const table = document.getElementById('result_list');
    const newRow = table.insertRow(-1);  // Insert at the end

    // Adjust the number of cells based on your list_display
    const numCells = table.rows[0].cells.length;
    for (let i = 0; i < numCells; i++) {
        newRow.insertCell(i).innerHTML = '';
    }

    const saveButton = document.createElement('button');
    saveButton.innerText = 'Save';
    saveButton.addEventListener('click', function () {
        // Implement logic to save the data (e.g., AJAX request or form submission)
    });

    const cell = newRow.insertCell(numCells);
    cell.appendChild(saveButton);
});
