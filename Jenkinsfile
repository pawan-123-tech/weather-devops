
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
                bat '"C:\\Users\\panka\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"C:\\Users\\panka\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t weather-app .'
            }
        }

        stage('Deploy Weather App') {
            steps {
                bat '"C:\\Users\\panka\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" rm -f weather-container 2>NUL'
                bat '"C:\\Users\\panka\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" run -d --name weather-container -p 5000:5000 weather-app'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat '"C:\\Users\\panka\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" ps'
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
