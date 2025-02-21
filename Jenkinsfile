pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 -v'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 hello.py'
      }
    }
  }
}
