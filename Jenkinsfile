pipeline {
  agent any
  stages {
    stage('Print') {
      steps {
        echo 'this works'
        echo %PATH%
      }
    }
    stage('hello') {
      steps {
        bat 'python3 hello.py'
      }
    }
  }
}
