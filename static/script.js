// ==================== VARIABLES ====================
const studentName = document.getElementById('studentName');
const studentEmail = document.getElementById('studentEmail');
const addBtn = document.getElementById('addBtn');
const studentList = document.getElementById('studentList');
const errorMsg = document.getElementById('errorMsg');

const editModal = document.getElementById('editModal');
const editName = document.getElementById('editName');
const editEmail = document.getElementById('editEmail');
const saveBtn = document.getElementById('saveBtn');
const cancelBtn = document.getElementById('cancelBtn');
const closeBtn = document.querySelector('.close');

// AI Widget Variables
const aiChatScreen = document.getElementById('aiChatScreen');
const aiToggleBtn = document.getElementById('aiToggleBtn');
const closeChat = document.getElementById('closeChat');
const chatInput = document.getElementById('chatInput');
const askBtn = document.getElementById('askBtn');
const chatHistory = document.getElementById('chatHistory');

let currentEditId = null;

// ==================== EVENT LISTENERS ====================

addBtn.addEventListener('click', addStudent);
[studentName, studentEmail].forEach(input => {
    input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') addStudent();
    });
});

saveBtn.addEventListener('click', saveEditedStudent);
cancelBtn.addEventListener('click', closeEditModal);
closeBtn.addEventListener('click', closeEditModal);

// AI Widget Events
aiToggleBtn.addEventListener('click', () => {
    aiChatScreen.classList.toggle('show');
    if(aiChatScreen.classList.contains('show')) chatInput.focus();
});

closeChat.addEventListener('click', () => {
    aiChatScreen.classList.remove('show');
});

askBtn.addEventListener('click', askAI);
chatInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') askAI();
});

window.addEventListener('load', loadStudents);

// ==================== CRUD FUNCTIONS ====================

async function loadStudents() {
    try {
        const response = await fetch('/api/students');
        const result = await response.json();

        if (result.success) {
            renderStudents(result.data);
        } else {
            showError('Failed to load students');
        }
    } catch (error) {
        console.error('Error loading students:', error);
        showError('Error loading students. Please check your connection.');
    }
}


async function addStudent() {
    const name = studentName.value.trim();
    const email = studentEmail.value.trim();

    if (!name || !email) {
        showError('Please enter both name and email');
        return;
    }

    try {
        const response = await fetch('/api/students', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, email })
        });

        const result = await response.json();

        if (result.success) {
            studentName.value = '';
            studentEmail.value = '';
            clearError();
            loadStudents();
        } else {
            showError(result.error || 'Failed to add student');
        }
    } catch (error) {
        console.error('Error adding student:', error);
        showError('Error adding student. Please try again.');
    }
}


async function deleteStudent(id) {
    console.log('Attempting to delete student with ID:', id);

    try {
        const response = await fetch(`/api/students/${id}`, {
            method: 'DELETE'
        });

        const result = await response.json();

        if (result.success) {
            loadStudents();
        } else {
            showError(result.error || 'Failed to delete student');
        }
    } catch (error) {
        console.error('Error deleting student:', error);
        showError('Error deleting student. Please try again.');
    }
}


function openEditModal(id, name, email) {
    currentEditId = id;
    editName.value = name;
    editEmail.value = email;
    editModal.classList.add('show');
    editName.focus();
}


function closeEditModal() {
    editModal.classList.remove('show');
    currentEditId = null;
    editName.value = '';
    editEmail.value = '';
}


async function saveEditedStudent() {
    const name = editName.value.trim();
    const email = editEmail.value.trim();

    if (!name || !email) {
        showError('Name and Email cannot be empty');
        return;
    }

    try {
        const response = await fetch(`/api/students/${currentEditId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, email })
        });

        const result = await response.json();

        if (result.success) {
            closeEditModal();
            clearError();
            loadStudents();
        } else {
            showError(result.error || 'Failed to update student');
        }
    } catch (error) {
        console.error('Error updating student:', error);
        showError('Error updating student. Please try again.');
    }
}

// ==================== AI CHAT FUNCTIONS ====================

async function askAI() {
    const query = chatInput.value.trim();
    if (!query) return;

    // Add user message to UI
    addChatMessage(query, 'user');
    chatInput.value = '';

    // Add loading message
    const loadingId = 'loading-' + Date.now();
    const loadingMsg = document.createElement('div');
    loadingMsg.id = loadingId;
    loadingMsg.className = 'ai-msg loading-dots';
    loadingMsg.textContent = 'Thinking';
    chatHistory.appendChild(loadingMsg);
    chatHistory.scrollTop = chatHistory.scrollHeight;

    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query })
        });

        const result = await response.json();
        const loadingEl = document.getElementById(loadingId);
        if(loadingEl) loadingEl.remove();

        if (result.success) {
            addChatMessage(result.answer, 'ai');
        } else {
            addChatMessage('Error: ' + result.error, 'ai');
        }
    } catch (error) {
        const loadingEl = document.getElementById(loadingId);
        if(loadingEl) loadingEl.remove();
        addChatMessage('Error: Failed to connect to AI server.', 'ai');
    }
}

function addChatMessage(text, sender) {
    const msgDiv = document.createElement('div');
    msgDiv.className = sender === 'user' ? 'user-msg' : 'ai-msg';
    msgDiv.textContent = text;
    chatHistory.appendChild(msgDiv);
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

// ==================== UI FUNCTIONS ====================

function renderStudents(students) {
    if (students.length === 0) {
        studentList.innerHTML = `
            <div class="empty-state">
                <p>✨ No students found!</p>
            </div>
        `;
        return;
    }

    studentList.innerHTML = students.map(student => `
        <div class="task-item">
            <div class="student-info">
                <span class="student-name">${escapeHtml(student.name)}</span>
                <span class="student-email">${escapeHtml(student.email)}</span>
            </div>
            <div class="task-actions">
                <button 
                    class="btn btn-edit btn-small" 
                    onclick="openEditModal(${student.id}, '${escapeHtml(student.name).replace(/'/g, "\\'")}', '${escapeHtml(student.email).replace(/'/g, "\\'")}')">
                    Edit
                </button>
                <button 
                    class="btn btn-danger btn-small" 
                    onclick="deleteStudent(${student.id})">
                    Delete
                </button>
            </div>
        </div>
    `).join('');
}


function showError(message) {
    errorMsg.textContent = message;
    errorMsg.classList.add('show');
    setTimeout(() => {
        errorMsg.classList.remove('show');
    }, 4000);
}


function clearError() {
    errorMsg.textContent = '';
    errorMsg.classList.remove('show');
}


function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
