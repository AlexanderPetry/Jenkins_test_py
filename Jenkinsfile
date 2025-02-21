pipeline {
  agent any
  stages {
    stage('Print') {
      steps {
        echo 'this works'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 hello.py'
      }
    }
  }
}
