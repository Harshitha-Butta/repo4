pipeline{
    agent any
    parameters {
    string description: 'Enter the new version :', name: 'version', trim: true
    }
    stages{
        stage('version'){
            steps{
                bat 'py basic.py'
            }
        }
    }
}
