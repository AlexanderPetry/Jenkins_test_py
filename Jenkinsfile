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
        set PATH=C:\Users\RobbertjanVerschuren\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0;%PATH%
        bat 'python3 hello.py'
      }
    }
  }
}
