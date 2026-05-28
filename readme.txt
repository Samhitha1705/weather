WEATHER APP DEVOPS PROJECT (FULL STEPS)
🟢 STEP 1: Create Project Folder (Linux)
mkdir weather-project
cd weather-project
🟢 STEP 2: Create Python file
nano weather.py
🟢 STEP 3: Write Weather Script
import requests
import os

API_KEY = "YOUR_API_KEY"

CITY = os.getenv("CITY", "Bangalore")

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print("\nWeather Report")
print("----------------------")

if data["cod"] == 200:
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Weather:", data["weather"][0]["main"])
    print("Humidity:", data["main"]["humidity"], "%")
else:
    print("Error:", data["message"])
🟢 STEP 4: Test locally (Linux)
CITY=Chennai python3 weather.py

✔ This confirms API works

🟢 STEP 5: Install Git (if not done)
git init
git add .
git commit -m "weather project"
🟢 STEP 6: Push to GitHub
git remote add origin https://github.com/yourusername/weather.git
git branch -M main
git push -u origin main
🟢 STEP 7: Install Jenkins (Ubuntu)
sudo systemctl start jenkins
sudo systemctl enable jenkins

Open:

http://localhost:8080
🟢 STEP 8: Create Jenkins Freestyle Job

Go to:

New Item → Weather-job → Freestyle
🟢 STEP 9: Git setup in Jenkins

Under:
Source Code Management

Git repo URL:
https://github.com/yourusername/weather.git
Branch:
*/main
🟢 STEP 10: Add Build Step (IMPORTANT)

Go to:

👉 Build Steps → Execute shell

Paste:

rm -rf venv

python3 -m venv venv

./venv/bin/pip install requests

CITY=Bangalore ./venv/bin/python weather.py
🟢 STEP 11: Run Jenkins build

Click:
👉 Build Now

Check:
👉 Console Output

🟢 STEP 12: Make it dynamic (Jenkins input)

Enable:

✔ This project is parameterized
✔ Add String Parameter:

Name: CITY
Default: Bangalore

Then update build step:

rm -rf venv

python3 -m venv venv

./venv/bin/pip install requests

./venv/bin/python weather.py

Now Jenkins UI will ask:

CITY = ________
🟢 STEP 13: Final Flow (what you built)
GitHub → Jenkins → Python → Weather API → Output
