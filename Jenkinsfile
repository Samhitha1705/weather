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

        stage('Sonar Analysis') {
            steps {
                withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
                    sh '''
                    sonar-scanner \
                    -Dsonar.host.url=http://localhost:9000 \
                    -Dsonar.token=$SONAR_TOKEN
                    '''
                }
            }
        }
    }
}
