# 🔥 Fire Detection System

A real-time AI-powered fire and smoke detection system built with Django and YOLOv8. This application provides instant detection through image uploads and live video streaming with comprehensive logging and reporting capabilities.

## 🌟 Features

- **Image Detection**: Upload images for instant fire and smoke detection
- **Live Video Stream**: Real-time detection from webcam feed
- **Detection Logs**: Complete history of all detections with confidence scores
- **PDF Reports**: Export detection logs as professional PDF reports
- **User Authentication**: Secure login and registration system
- **Dashboard Analytics**: Visual statistics and recent detection alerts
- **Alert System**: Automatic flagging of high-confidence detections

## 🛠️ Tech Stack

- **Backend**: Django 4.2.11
- **AI Model**: YOLOv8 (Ultralytics)
- **Computer Vision**: OpenCV
- **Database**: SQLite (development) / PostgreSQL (production)
- **PDF Generation**: ReportLab
- **Deployment**: Render
- **Server**: Gunicorn

## 📋 Prerequisites

- Python 3.11.9
- pip (Python package manager)
- Git
- Webcam (for live stream feature)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd firedetection_final/firedetection_yolo/firedetection_yolo
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

## 📁 Project Structure

```
firedetection_yolo/
├── detection/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── myapp/                  # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   ├── static/            # CSS, JS files
│   └── templates/         # HTML templates
├── media/                  # Uploaded images and results
├── staticfiles/           # Collected static files
├── best.pt                # YOLO model weights
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── runtime.txt           # Python version
```

## 🎯 Usage

### Image Detection

1. Navigate to **Image Detection** from the dashboard
2. Click "Choose File" and select an image
3. Click "Detect Fire" to analyze
4. View results with confidence scores and annotated image

### Live Stream Detection

1. Navigate to **Live Stream** from the dashboard
2. Click "Start Stream" to begin webcam detection
3. Real-time detection results will be displayed
4. Click "Stop Stream" to end

### View Detection Logs

1. Navigate to **Logs** from the dashboard
2. View all detection history with timestamps
3. Export logs as PDF for reporting

## 🔧 Configuration

### Environment Variables

Create a `.env` file or set environment variables:

```bash
SECRET_KEY=your-secret-key
DEBUG=True  # Set to False in production
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Detection Thresholds

Modify in `myapp/views.py`:

```python
# Image detection confidence threshold
results = model(input_path, conf=0.4, iou=0.4, imgsz=640)

# Video stream confidence threshold
results = model(frame, conf=0.15, iou=0.4, imgsz=640)

# Alert threshold (for marking high-confidence detections)
alert_sent = confidence > 0.4  # 40% threshold
```

## 🌐 Deployment to Render

### 1. Prepare for Deployment

Ensure these files exist:
- `requirements.txt`
- `runtime.txt`
- `build.sh`
- `render.yaml`

### 2. Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

### 3. Deploy on Render

1. Go to [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Root Directory**: `firedetection_yolo/firedetection_yolo`
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate`
   - **Start Command**: `gunicorn detection.wsgi:application`
5. Set Environment Variables:
   - `PYTHON_VERSION`: `3.11.9`
   - `SECRET_KEY`: (auto-generate)
   - `DEBUG`: `False`
6. Click "Create Web Service"

Your app will be live at `https://your-app-name.onrender.com`

## 📊 Database Models

### DetectionLog

Stores all fire/smoke detection events:

```python
- detection_type: 'fire' or 'smoke'
- confidence: Detection confidence (0-100%)
- image_path: Path to detected image (optional)
- detected_at: Timestamp
- alert_sent: Boolean flag for high-confidence detections
```

## 🎨 Features in Detail

### Dashboard
- Total detection count
- Fire vs smoke statistics
- Recent detection alerts
- Quick access to all features

### Image Detection
- Supports common image formats (JPG, PNG, etc.)
- Real-time processing with YOLO
- Annotated result images
- Confidence score display

### Live Stream
- Real-time webcam feed
- Continuous detection
- Automatic logging
- Low-latency processing

### Detection Logs
- Paginated log view
- Filterable by type
- Sortable by date/confidence
- PDF export functionality

## 🔒 Security

- User authentication required for all features
- CSRF protection enabled
- Secure password hashing
- Environment-based secret key management
- Production-ready settings for deployment

## 📝 API Endpoints

- `/` - Dashboard (requires login)
- `/login/` - User login
- `/register/` - User registration
- `/logout/` - User logout
- `/image-detect/` - Image detection page
- `/video-stream/` - Live stream page
- `/video-feed/` - Video stream endpoint
- `/logs/` - Detection logs
- `/export-logs-pdf/` - Export logs as PDF
- `/api/stats/` - Dashboard statistics API

## 🐛 Troubleshooting

### Static Files Not Loading

```bash
python manage.py collectstatic --no-input
```

### Database Issues

```bash
python manage.py migrate --run-syncdb
```

### YOLO Model Not Found

Ensure `best.pt` is in the project root directory.

### Webcam Not Working

- Check camera permissions
- Ensure no other application is using the camera
- Try different camera index in `cv2.VideoCapture(0)`

## 📦 Dependencies

```
Django==4.2.11
ultralytics==8.3.70
opencv-python-headless==4.10.0.84
reportlab==4.2.5
numpy>=1.26,<3
psycopg2-binary==2.9.9
gunicorn==23.0.0
whitenoise==6.6.0
requests==2.31.0
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- YOLOv8 by Ultralytics
- Django Framework
- OpenCV Community
- ReportLab for PDF generation

## 📞 Support

For support, email your-email@example.com or open an issue in the repository.

## 🔮 Future Enhancements

- [ ] Email notifications for fire detection
- [ ] Mobile app integration
- [ ] Multi-camera support
- [ ] Cloud storage for detection images
- [ ] Advanced analytics dashboard
- [ ] SMS alert system
- [ ] Integration with fire alarm systems

---

**Made with ❤️ for fire safety**
