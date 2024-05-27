
# EduVision: Power your teaching potential 📒

Created for LinceHacks 2024

## Authors

- [@JocelynVelarde](https://github.com/JocelynVelarde)
- [@Diego785xd](https://github.com/Diego785xd)

## Features
- Optimized API costs using gpt4-o
- Light and Dark mode enabled
- Available in all devices

### Classroom Attention
- Use of computer vision tools to monitor sentiment analysis and attention levels of students
- Fetch data on a dynamic dashboard to view different metrics
- Mantain privacy of students using only tags and not saving biometric data
- Generate reports and reccomendations in relation to the results from lessons
- Identify in which section of the class the students where most engaged, and what was the content being displayed

### Generate Content
- Use of generative artificial intelligence to create content for your lessons
- Direct conversation with an assistant to generate the desired content
- Text integration and audios to increase dynamic interaction
- Selection between creating a study plan or lesson content by filling a form
- Visualization of desired topics and pptx creation


## Structure
```bash
streamlit_app 
├─ home.py
├─ .streamlit
│   └─ secrets.toml
├─ algorithms
│  └─ embeedings.py
│  └─ mongodb_genai.py
│  └─ vectorization_mongo.py
├─ gpt4o
│  └─ image_process.py
│  └─ pptx_genai.py
│  └─ simple_text.py
├─ assets
│  └─ files
│  └─ images
├─ pages
│  └─ Chat.py
│  └─ instructions.py
│  └─ Panel.py
├─ utils
├─ AiManager.py
├─ DataManager.py
├─ index.html
├─ vision_main.py
└─ requirements.txt
```

## Tools

- OpenAI API
- Streamlit
- OpenCV
- MongoDB
- Threading
- Queue
- Deepface
- pandas
- numpy

Deployed with: Streamlit Cloud

## Demo

[YouTube](https://www.youtube.com/watch?v=ZPCu1XzHcSM)


## License

[MIT](https://choosealicense.com/licenses/mit/)



