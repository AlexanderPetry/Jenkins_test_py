pipeline {
  agent { docker { image 'python:3.13.2-alpine3.21' } }
  stages {
    stage('Print') {
      steps {
        echo 'this works'
      }
    }
    stage('hello') {
      steps {
        bat 'python3 hello.py'
      }
    }
  }
}
