  
    document.addEventListener('DOMContentLoaded', () => {
        const medicineSelect = document.getElementById('medicineSelect');
        const modeField = document.getElementById('modeField');
        const daysField = document.getElementById('daysField');
        const dosagesField = document.getElementById('dosagesField');
        const languageSelect = document.getElementById('languageSelect');
        const instructionsSelect = document.getElementById('instructionsSelect');
        const addMedicineBtn = document.getElementById('addMedicineBtn');
        const medicineTableBody = document.getElementById('medicineTableBody');
        const Medicine_input = document.getElementById('Medicine_input');
        const Mode_input = document.getElementById('Mode_input');
        const Days_input = document.getElementById('Days_input');
        const Dosage_input = document.getElementById('Dosage_input');
        const Language_input = document.getElementById('Language_input');
        const Instructions_input = document.getElementById('Instructions_input');

        // Initialize hidden fields with existing medicine list data
        updateHiddenInputValues();

        // Event listener for when a medicine is selected
        $('#medicineSelect').on('change', function() {
            const selectedOption = this.options[this.selectedIndex];
            const form = selectedOption.getAttribute('data-form');
            const duration = selectedOption.getAttribute('data-duration');
            const dosages = selectedOption.getAttribute('data-dosages');

            // Update fields in the form based on selected medicine
            modeField.value = getModeLabel(form);
            daysField.value = duration;
            dosagesField.value = dosages;
        });

        // Event listener for adding medicine
        addMedicineBtn.addEventListener('click', (event) => {
            event.preventDefault(); // Prevent default form submission behavior

            const selectedMedicine = medicineSelect.value;
            const selectedOption = medicineSelect.options[medicineSelect.selectedIndex];
            const mode = selectedOption.getAttribute('data-form'); // Get mode from selected option
            const days = daysField.value;
            const dosage = dosagesField.value;
            const instructions = instructionsSelect.value;
            const instructionsText = instructionsSelect.options[instructionsSelect.selectedIndex].text;
            const language = languageSelect.value;

            // Add row to the medicine table
            const newRow = medicineTableBody.insertRow();
            newRow.innerHTML = `
                <td>${selectedMedicine}</td>
                <td>${getModeLabel(mode)}</td>
                <td>${days}</td>
                <td>${dosage}</td>
                <td data-instruction-id="${instructions}">${instructionsText}</td>
                <td><button class="btn btn-danger btn-sm removeBtn">Remove</button></td>
            `;

            // Update hidden input values after adding medicine
            updateHiddenInputValues();

            // Clear the form fields after adding medicine
            resetForm();
        });

        // Event delegation to handle remove button clicks
        medicineTableBody.addEventListener('click', (event) => {
            if (event.target.classList.contains('removeBtn')) {
                const row = event.target.closest('tr');
                medicineTableBody.removeChild(row);

                // Update hidden input values after removal
                updateHiddenInputValues();
            }
        });

        // Function to update hidden input values after adding/removing a row
        function updateHiddenInputValues() {
            const medicineRows = Array.from(medicineTableBody.getElementsByTagName('tr'));
            const medicines = [];
            const modes = [];
            const days = [];
            const dosages = [];
            const instructions = [];

            medicineRows.forEach(row => {
                const cells = row.cells;
                medicines.push(cells[0].textContent);
                modes.push(getModeValue(cells[1].textContent));
                days.push(cells[2].textContent);
                dosages.push(cells[3].textContent);
                instructions.push(cells[4].getAttribute('data-instruction-id')); // Get instruction ID from the 5th cell
            });

            // Join arrays into comma-separated strings for hidden input values
            Medicine_input.value = medicines.join(',');
            Mode_input.value = modes.join(',');
            Days_input.value = days.join(',');
            Dosage_input.value = dosages.join(',');
            Instructions_input.value = instructions.join(',');
            Language_input.value = ''; // Since we're no longer tracking languages
        }

        // Function to get mode label based on mode value
        function getModeLabel(value) {
            switch (value) {
                case '1':
                    return 'Tab';
                case '2':
                    return 'Syp';
                case '3':
                    return 'Pwd';
                default:
                    return 'Unknown';
            }
        }

        // Function to get mode value based on mode label
        function getModeValue(label) {
            label = label.trim(); // Trim whitespace from the label
            switch (label) {
                case 'Tab':
                    return 1;
                case 'Syp':
                    return 2;
                case 'Pwd':
                    return 3;
                default:
                    return 0;
            }
        }

        // Function to reset the form fields
        function resetForm() {
            medicineSelect.selectedIndex = 0;
            modeField.value = '';
            daysField.value = '';
            dosagesField.value = '';
            languageSelect.selectedIndex = 0;
            instructionsSelect.selectedIndex = 0;
        }
    });

