import requests
from flask import Blueprint, request, jsonify

from app.services.student_service import StudentService
from app.services.ollama_service import OllamaService

api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/students', methods=['GET'])
def get_all_students():
    try:
        data = StudentService.get_all_students()
        return jsonify({'success': True, 'data': data}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@api_bp.route('/students', methods=['POST'])
def add_student():
    try:
        data = request.get_json()
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()

        if not name or not email:
            return jsonify({'success': False, 'error': 'Name and Email are required'}), 400

        student = {'name': name, 'email': email}
        result = StudentService.add_student(student)
        return jsonify({'success': True, 'data': result}), 201
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@api_bp.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    try:
        data = request.get_json()
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()

        if not name or not email:
            return jsonify({'success': False, 'error': 'Name and Email cannot be empty'}), 400

        update_data = {'name': name, 'email': email}
        result = StudentService.update_student(student_id, update_data)

        if not result:
            return jsonify({'success': False, 'error': 'Student not found'}), 404

        return jsonify({'success': True, 'data': result}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@api_bp.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        result = StudentService.delete_student(student_id)
        if not result:
            return jsonify({'success': False, 'error': 'Student not found'}), 404
        return jsonify({'success': True, 'message': 'Student deleted successfully'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@api_bp.route('/chat', methods=['POST'])
def chat():
    try:
        user_query = request.get_json().get('query', '').strip()
        if not user_query:
            return jsonify({'success': False, 'error': 'No query provided'}), 400

        students = StudentService.get_all_students()
        total_count = len(students)

        if students:
            table_header = "| ID  | Name                     | Email                          |"
            table_sep = "|-----|--------------------------|--------------------------------|"
            table_rows = "\\n".join(
                f"| {s.get('id', ''): <3} | {s.get('name', ''): <24} | {s.get('email', ''): <30} |"
                for s in students
            )
            db_table = f"{table_header}\\n{table_sep}\\n{table_rows}"
        else:
            db_table = "(No students in the database yet)"

        prompt = f"""You are a helpful database assistant for a Student Management System.
You have LIVE access to the following student database records. Use ONLY this data to answer questions.

=== STUDENT DATABASE (Live Data) ===
Total Students: {total_count}

{db_table}

=== INSTRUCTIONS ===
- Answer based SOLELY on the data above.
- For count questions (e.g. "how many"), return the exact number: {total_count}.
- For name/email lookups, reference the table above.
- If a student is not found, say "No student found matching that criteria."
- Be concise, factual, and friendly.
- Do NOT make up any student data.

=== USER QUESTION ===
{user_query}

=== YOUR ANSWER ==="""

        ollama_response = OllamaService.generate_chat_response(prompt)

        if ollama_response.status_code == 200:
            ai_answer = ollama_response.json().get(
                'response', 'No response from AI.').strip()
            return jsonify({'success': True, 'answer': ai_answer, 'students_count': total_count}), 200

        return jsonify({'success': False, 'error': "Ollama is not running or returned an error."}), 500

    except requests.exceptions.ConnectionError:
        return jsonify({'success': False, 'error': "Cannot connect to Ollama. Please start Ollama."}), 503
    except requests.exceptions.ReadTimeout:
        return jsonify({'success': False, 'error': "Ollama request timed out. The model may still be loading."}), 504
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@api_bp.route('/db-status', methods=['GET'])
def db_status():
    try:
        students = StudentService.get_all_students()
        return jsonify({'success': True, 'total': len(students), 'students': students}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
