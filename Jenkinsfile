pipeline {
    agent any

    parameters {
        string(defaultValue: "TEST", description: 'What environment?', name: 'userFlag')
        // choices are newline separated
        choice(choices: 'US-EAST-1\nUS-WEST-2', description: 'What AWS region?', name: 'region')
	booleanParam(name: 'debug_build', defaultValue: true, description: '')
	file(name: 'file_build', description: 'file')
	text(name: 'text_build', description: 'text')
	password(name: 'pass_build', description: 'pass')
	run(name: 'run_build', description: 'run')
    }

    stages {
        stage("foo") {
            steps {
		sh "echo ${params.region}"
		sh "echo ${params.userFlag}"
		sh "echo ${params.debug_build}"
            }
        }
    }
}
