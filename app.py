from flask import Flask, render_template, request, send_file
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

app = Flask(__name__)

# Download NLTK resources (only run once)
nltk.download('punkt')
nltk.download('stopwords')

# Sample skills database (you can expand this as needed)
skills_database = [
    'python', 'java', 'javascript', 'html', 'css', 'sql', 'machine learning',
    'data analysis', 'project management', 'communication', 'problem solving'
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    job_description = request.form['job_description']
    
    # Example NLP processing (tokenization and stopwords removal)
    tokens = word_tokenize(job_description.lower())
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if not w in stop_words]
    
    # Match tokens with skills database
    matched_skills = [token for token in filtered_tokens if token in skills_database]
    
    # Generate resume content dynamically
    resume_content = f"""
    Name: John Doe
    Skills: {', '.join(matched_skills[:5])}  # Limit to 5 skills for example
    
    Experience:
    - Example Job Experience
    
    Education:
    - Example Education
    """
    
    return render_template('resume.html', resume_content=resume_content)

@app.route('/download_resume', methods=['POST'])
def download_resume():
    resume_content = request.form['resume_content']
    
    # Example: Create a file and send it for download
    with open('static/generated_resume.txt', 'w') as f:
        f.write(resume_content)
    
    return send_file('static/generated_resume.txt', as_attachment=True, attachment_filename='resume.txt')

if __name__ == '__main__':
    app.run(debug=True)
