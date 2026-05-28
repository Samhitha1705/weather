pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/Samhitha1705/weather.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install requests'
            }
        }

        stage('Run Weather Script') {
            steps {
                sh 'python3 weather.py'
            }
        }
    }
}
