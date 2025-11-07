pipeline {
    agent any
environment {
    TEST_ENV = 'staging'
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
                    . venv/bin/activate
                    pip install --upgrade pip
                '''
            }
        }


        stage('Run API Tests') {
          steps {
            echo "🧪 Running pytest automation suite in project folder..."
            dir('/home/vvdn/PycharmProjects/PythonProject/pytestss') {
            sh '''
                # Activate virtual environment inside project
                source ${VENV}/bin/activate

                # Run tests from correct directory
                pytest tests/ --env=${TEST_ENV} \
                    --junitxml=reports/results.xml \
                    --html=${REPORT_PATH} --self-contained-html
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
