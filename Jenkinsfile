
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

       stage('Check Project Files') {
    steps {
        bat 'dir'
        bat 'docker --version'
    }
}

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t weather-app .'
            }
        }

        stage('Deploy Weather App') {
            steps {
                bat 'docker rm -f weather-container 2>NUL || exit /b 0'
                bat 'docker run -d --name weather-container -p 5000:5000 weather-app'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'docker ps'
                bat 'curl -f http://localhost:5000/health'
            }
        }
    }

    post {
        success {
            echo 'Weather Information pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check Console Output for details.'
        }
    }
}
