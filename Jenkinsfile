pipeline {
  agent any
  stages {
    stage('Print') {
      steps {
        echo 'this works'
      }
    }
    stage('TEST_PYTHON') {
      steps {
        bat 'C:\\Users\\TA\\AppData\\Local\\Programs\\Python\\Python312\\python.exe hello.py'
      }
    }
      stage('RESS_TEST') {
      steps {
        bat 'C:\\Users\\TA\\AppData\\Local\\Programs\\Python\\Python312\\python.exe RESS_test.py'
      }
    }
    stage('MAN_TEST') {
      steps {
        bat 'C:\\Users\\TA\\AppData\\Local\\Programs\\Python\\Python312\\python.exe MAN_Test.py'
      }
    }
    
  }
}
