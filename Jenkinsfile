pipeline {
    pipeline {
        agent any

        stages {
            stage('Setup Python & Install Dependencies') {
                steps {
                    script {
                        if (isUnix()) {
                            sh '''#!/bin/bash
    set -e
    python3 --version || python --version
    python3 -m venv venv || python -m venv venv
    . venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    '''
                        } else {
                            bat '''
    python --version
    python -m venv venv
    call venv\\Scripts\\activate
    pip install --upgrade pip
    pip install -r requirements.txt
    '''
                        }
                    }
                }
            }

            stage('Run Python Script') {
                steps {
                    script {
                        if (isUnix()) {
                            sh '. venv/bin/activate && python main.py'
                        } else {
                            bat 'call venv\\Scripts\\activate && python main.py'
                        }
                    }
                }
            }
        }

        post {
            success {
                archiveArtifacts artifacts: 'performance_chart.png', fingerprint: true
                echo '🎉 Jenkins Pipeline Success!'
            }
            failure {
                echo '❌ Jenkins Pipeline Failed!'
            }
        }
    }
