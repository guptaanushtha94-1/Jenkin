pipeline {
    agent any
environment {
    REPORT_PATH = 'reports/report.html'
}

    stages {

        stage('Checkout Code') {
            steps {
                echo "📦 Cloning repository..."
                git branch: 'main', url: 'https://github.com/guptaanushtha94-1/Jenkin.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo "🐍 Creating virtual environment..."
                sh '''
                    python3 -m venv ${VENV:-venv}
                    /var/lib/jenkins/workspace/declarative-pipeline/venv/bin/activate
                    pip install --upgrade pip
                '''
            }
        }


        stage('Run API Tests') {
    steps {
        echo "🧪 Running pytest automation suite in project folder..."
        dir('/home/vvdn/PycharmProjects/PythonProject/pytestss') {
            sh '''
                #!/bin/bash
                # Activate virtual environment from Jenkins workspace
                . ${WORKSPACE}/venv/bin/activate

                echo "✅ Virtual environment activated at ${WORKSPACE}/venv"

                # Optional: install dependencies if needed
                pip install -r requirements.txt || true

                # Run pytest and generate reports
                pytest tests/ \
                    --junitxml=reports/results.xml \
                    --html=reports/report.html --self-contained-html
            '''
        }
    }
}
        stage('Archive Test Reports') {
            steps {
                echo "📊 Archiving test results..."
                junit 'reports/results.xml'
                archiveArtifacts artifacts: 'reports/**', fingerprint: true
                echo "📎 HTML report available at: ${env.BUILD_URL}artifact/${REPORT_PATH}"
            }
        }
    }

        post {
        always {
            echo "🧹 Cleaning up virtual environment..."
            sh 'rm -rf ${VENV} || true'
        }
        }
}
