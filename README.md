# 📝 Task Manager - Full-Stack CRUD Application

A simple, beginner-friendly CRUD web application built with Flask and Supabase.

## 🎯 Features

- ✅ Add new tasks
- ✏️ Edit existing tasks
- 🗑️ Delete tasks
- 📱 Responsive design
- 🎨 Beautiful UI with smooth animations
- 🔒 Real database with Supabase (PostgreSQL)

## 📦 Project Structure

```
crud-app/
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
├── templates/
│   └── index.html        # Frontend HTML
└── static/
    ├── style.css         # Styling
    └── script.js         # JavaScript (fetch API)
```

## 🚀 Setup Instructions

### Step 1: Create Virtual Environment

**Windows (PowerShell/CMD):**
```bash
# Navigate to project directory
cd c:\Users\Varshini\ s\OneDrive\Desktop\crud-app

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

**Mac/Linux:**
```bash
cd ~/Desktop/crud-app
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set Up Supabase Database

1. Go to [supabase.com](https://supabase.com) and sign up/login
2. Create a new project
3. Create a new table named `students` with:
   - Column `id`: INT, Primary Key, Auto-increment
   - Column `name`: TEXT, Not Null
   - Column `email`: TEXT, Not Null
   - Column `created_at`: TIMESTAMP DEFAULT now()
   - Column `updated_at`: TIMESTAMP

4. Get your **Supabase URL** and **Anon Key**:
   - Go to Settings → API
   - Copy `Project URL` and `anon` key

### Step 4: Configure Environment Variables

Edit `.env` file and add your Supabase credentials:

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_anon_key_here
FLASK_ENV=development
```

### Step 5: Run the Application

```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

### Step 6: Open in Browser

Go to **http://127.0.0.1:5000** in your web browser.

## 🔌 API Endpoints

### GET /api/students
Get all students
```bash
curl http://localhost:5000/api/students
```

### POST /api/students
Add a new student
```bash
curl -X POST http://localhost:5000/api/students \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe", "email":"john@example.com"}'
```

### PUT /api/students/<id>
Update a student by ID
```bash
curl -X PUT http://localhost:5000/api/students/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"John Updated", "email":"john_updated@example.com"}'
```

### DELETE /api/students/<id>
Delete a student by ID
```bash
curl -X DELETE http://localhost:5000/api/students/1
```

## 📖 How It Works

### Backend (app.py)
- Uses **Flask** to create REST API endpoints
- Uses **Supabase Python client** to connect to PostgreSQL database
- Loads credentials from `.env` using **python-dotenv**
- Returns JSON responses for all operations

### Frontend (index.html, script.js, style.css)
- Single-page application (SPA)
- Uses **Fetch API** to call backend endpoints
- Displays tasks in a list with Edit/Delete buttons
- Modal dialog for editing tasks
- Real-time UI updates

### Database (Supabase)
- PostgreSQL database hosted on Supabase
- `tasks` table stores all task data
- Auto-incrementing ID as primary key

## 🎓 Learning Points

This project demonstrates:
- ✅ REST API design with Flask
- ✅ Database operations (CRUD)
- ✅ Environment variable management
- ✅ Fetch API for async requests
- ✅ Error handling
- ✅ Input validation
- ✅ Modal dialogs
- ✅ Responsive CSS

## 🐛 Troubleshooting

**"ModuleNotFoundError: No module named 'flask'"**
- Make sure venv is activated: `venv\Scripts\activate`
- Install requirements: `pip install -r requirements.txt`

**"Missing SUPABASE_URL or SUPABASE_KEY"**
- Check `.env` file exists in project root
- Verify you have correct URL and KEY from Supabase

**"Connection refused at http://127.0.0.1:5000"**
- Make sure Flask is running: `python app.py`
- Check if port 5000 is available

**No tasks showing**
- Check browser console (F12) for errors
- Verify `.env` credentials are correct
- Make sure `tasks` table exists in Supabase

## 🔐 Security Notes

- Never commit `.env` file to git
- This is a demo app - add authentication for production
- Use environment variables for all sensitive data
- Validate all user input

## 📝 License

Open source - feel free to use and modify!

## 🤝 Need Help?

- Check the code comments
- Review API responses in browser Network tab (F12)
- Print logs in browser console

Happy coding! 🚀
