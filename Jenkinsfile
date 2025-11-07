pipeline {
    agent any

    environment {
        REPORT_PATH = 'reports/report.html'
        VENV = 'venv'
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
                    # Clean up any old venv
                    rm -rf ${VENV}

                    # Create new virtual environment
                    python3 -m venv ${VENV}
                    chmod -R 755 ${VENV}

                    # Activate and install pip safely
                    . ${VENV}/bin/activate
                    pip install --upgrade pip --break-system-packages

                    # Install dependencies if requirements.txt exists
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt --break-system-packages
                    fi
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                echo "🧪 Running pytest automation suite..."
                sh '''
                    # Run tests using venv’s Python
                    ${VENV}/bin/python -m pytest tests/ \
                        --junitxml=reports/results.xml \
                        --html=${REPORT_PATH} --self-contained-html
                '''
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
