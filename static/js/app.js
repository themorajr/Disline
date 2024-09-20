// Example file data (replace with data from the backend)
const files = [
    { name: 'file1.pdf', type: 'PDF', size: 1024 },
    { name: 'file2.jpg', type: 'JPEG', size: 2048 },
    { name: 'file3.docx', type: 'Word Document', size: 3072 },
    { name: 'file4.zip', type: 'ZIP', size: 4096 }
];

function renderFiles(fileList) {
    const tbody = document.querySelector('#fileTable tbody');
    tbody.innerHTML = '';  // Clear the table

    fileList.forEach(file => {
        const row = document.createElement('tr');

        row.innerHTML = `
            <td>${file.name}</td>
            <td>${file.type}</td>
            <td>${(file.size / 1024).toFixed(2)}</td>
            <td class="action-buttons">
                <button class="delete-btn" onclick="deleteFile('${file.name}')">Delete</button>
            </td>
        `;

        tbody.appendChild(row);
    });
}

function deleteFile(fileName) {
    if (confirm(`Are you sure you want to delete ${fileName}?`)) {
        // Make an API call to delete the file from the server
        console.log(`File ${fileName} deleted.`);
        // Add actual delete logic here with backend integration
    }
}

function filterFiles() {
    const filter = document.getElementById('filterInput').value.toLowerCase();
    const filteredFiles = files.filter(file => 
        file.name.toLowerCase().includes(filter) || 
        file.type.toLowerCase().includes(filter)
    );
    renderFiles(filteredFiles);
}

// Render files on page load
document.addEventListener('DOMContentLoaded', () => {
    renderFiles(files);
});
