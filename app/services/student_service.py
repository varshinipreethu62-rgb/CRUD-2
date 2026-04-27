from app.services.supabase_service import supabase


class StudentService:
    @staticmethod
    def get_all_students():
        response = supabase.table('tasks').select(
            '*').order('id', desc=False).execute()
        return response.data

    @staticmethod
    def add_student(data):
        response = supabase.table('tasks').insert(data).execute()
        return response.data

    @staticmethod
    def update_student(student_id, data):
        response = supabase.table('tasks').update(
            data).eq('id', student_id).execute()
        return response.data

    @staticmethod
    def delete_student(student_id):
        response = supabase.table('tasks').delete().eq(
            'id', student_id).execute()
        return response.data
