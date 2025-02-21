pipeline {
  agent { docker { image 'python:3.13.2-alpine3.21' } }
  stages {
    stage('Print') {
      steps {
        echo 'this works'
        echo %PATH%
      }
    }
    stage('hello') {
      steps {
        bat 'C:\Users\RobbertjanVerschuren\AppData\Local\Microsoft\WindowsApps\python3.exe hello.py'
      }
    }
  }
}
