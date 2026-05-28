pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Samhitha1705/weather.git'
            }
        }

        stage('Run Weather Script') {
            steps {
                sh 'python3 weather.py'
            }
        }
    }
}
